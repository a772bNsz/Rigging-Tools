import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self):
        self.controls = self.skin_joints = []
        self.root_joint = self.end_joint = None

    def ik_spline(self):
        self.end_joint = self.root_joint.getChildren(ad=1)[0]
        pm.joint(self.root_joint, e=1, oj="xzy", sao="xup", ch=1, zso=1)
        hdl, eff, crv = pm.ikHandle(n="neck_HDL",
                                    sj=self.root_joint,
                                    ee=self.end_joint,
                                    sol="ikSplineSolver")
        eff.rename("neck_EFF")
        crv.rename("neck_CRV")
        crv.inheritsTransform.set(0)
        pm.select(cl=1)
        return hdl, crv

    def setup_controls(self):
        """
        placed to joint position
        custom attributes
        named correctly
        rotate order
        hierarchy
        """
        self.controls = controls = OrderedDict()
        controls["head_CON"] = {
            "snapTo": self.end_joint,
            "rotateOrder": 2,  # zxy
            "parent": "head_neck_GRP"
        }
        controls["neck_CON"] = {
            "snapTo": self.root_joint,
            "rotateOrder": 1,  # yzx
            "parent": "head_neck_GRP"
        }

        map(lambda x: pm.group(n=x, w=1), ["dontTouch_GRP", "head_neck_GRP"])

        for k, v in controls.items():
            con = pm.spaceLocator(n=k)
            ofs = pm.group(con, n=k.replace("CON", "OFS"))

            con.rotateOrder.set(v["rotateOrder"])
            ofs.rotateOrder.set(v["rotateOrder"])

            try:
                pm.matchTransform(ofs, v["snapTo"])
                pm.parent(ofs, v["parent"], a=1)
            except:
                pass

        pm.parent("head_neck_GRP", "root_transform_CON")
        pm.parent("root_transform_CON", w=1)

        neck_loc = pm.spaceLocator(n="neckChest_const_LOC")
        pm.matchTransform(neck_loc, "chest_CON")
        pm.parentConstraint(neck_loc, "head_neck_GRP", mo=1)
        pm.parent(neck_loc, "chest_CON")
        neck_loc.hide()
        pm.select(cl=1)
        return controls

    def _advanced_twist(self):
        # bind joints
        neck_base_bind, neck_end_bind = bind_joints = pm.duplicate(
            self.root_joint,
            self.end_joint,
            po=1)

        neck_base_bind.rename("neck_base_bind_JNT")
        neck_end_bind.rename("neck_end_bind_JNT")

        map(lambda x: x.rotate.set(0, 0, 0), bind_joints)

        neck_base_bind.rotateOrder.set(
            self.controls["neck_CON"]["rotateOrder"])
        neck_end_bind.rotateOrder.set(
            self.controls["head_CON"]["rotateOrder"])

        pm.parent(neck_end_bind, w=1)

        pm.skinCluster(bind_joints, "neck_CRV",
                       tsb=1, mi=2, n="neck_bind_SCL")

        pm.parentConstraint("neck_CON", neck_base_bind, mo=1)
        pm.parentConstraint("head_CON", neck_end_bind, mo=1)

        # advanced spline twist settings
        neck_hdl = pm.PyNode("neck_HDL")
        neck_hdl.dTwistControlEnable.set(1)
        neck_hdl.dWorldUpType.set(4)  # object rotation up (start/end)
        neck_hdl.dWorldUpAxis.set(1)
        neck_hdl.dWorldUpVectorY.set(-1)
        neck_hdl.dWorldUpVectorEndY.set(1)
        neck_hdl.dWorldUpVectorEndZ.set(-1)

        neck_base_bind.worldMatrix[0] >> neck_hdl.dWorldUpMatrix
        neck_end_bind.worldMatrix[0] >> neck_hdl.dWorldUpMatrixEnd

        pm.select(cl=1)
        return bind_joints

    def _squash_stretch(self):
        # math nodes
        math_nodes = map(lambda x: pm.createNode("floatMath", n=x), [
            "globalScale_neckNormalize_DIV",
            "neck_stretchPercent_DIV",
            "neck_sqrtStretch_POW",
        ])

        curve_info = pm.arclen("neck_CRV", ch=1).rename("neckInfo")

        math_nodes[0].operation.set(3)
        curve_info.arcLength >> math_nodes[0].floatA
        pm.PyNode("root_transform_CON").sy >> math_nodes[0].floatB

        math_nodes[1].operation.set(3)
        math_nodes[0].outFloat >> math_nodes[1].floatA
        math_nodes[1].floatB.set(curve_info.arcLength.get())

        math_nodes[2].operation.set(6)
        math_nodes[1].outFloat >> math_nodes[2].floatA
        math_nodes[2].floatB.set(0.5)

        # drive result joints
        result_chain = pm.PyNode(self.root_joint)
        result_chain = [result_chain] + result_chain.getChildren(ad=1)
        for jnt in result_chain:
            math_nodes[1].outFloat >> jnt.sx
        return True

    def guts(self):
        """
        advanced twist
        squash and stretch
        global scale
        """
        self._advanced_twist()
        self._squash_stretch()

        children = [
            "neck_HDL",
            "neck_CRV",
            "neck_base_bind_JNT",
            "neck_end_bind_JNT",
            self.root_joint
        ]

        pm.parent(children, "head_neck_GRP|dontTouch_GRP")
        pm.setAttr("head_neck_GRP|dontTouch_GRP.visibility", 0)
        pm.select(cl=1)
        return True

    def clean_up(self):
        # lock and hide all - offsets and head_neck_GRP|dontTouch_GRP
        items = ["head_neck_GRP", "head_neck_GRP|dontTouch_GRP"] + \
                [pm.listRelatives(k, p=1)[0] for k in self.controls.keys()]

        for i in items:
            map(lambda x: pm.setAttr((i + ".t" + x), lock=1, keyable=0), "xyz")
            map(lambda x: pm.setAttr((i + ".r" + x), lock=1, keyable=0), "xyz")
            map(lambda x: pm.setAttr((i + ".s" + x), lock=1, keyable=0), "xyz")
            pm.setAttr(i + ".v", lock=1, keyable=0)
        pm.setAttr("head_neck_GRP.v", lock=0, keyable=0)
        pm.setAttr("head_neck_GRP|dontTouch_GRP.v", lock=0, keyable=0)

        # lock and hide scale - head control
        map(lambda x: pm.setAttr(("head_CON.s" + x), lock=1, keyable=0), "xyz")

        # lock and hide translate/scale - neck control
        map(lambda x: pm.setAttr(("neck_CON.t" + x), lock=1, keyable=0), "xyz")
        map(lambda x: pm.setAttr(("neck_CON.s" + x), lock=1, keyable=0), "xyz")
        return True

