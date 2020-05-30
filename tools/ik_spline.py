"""
TODO: spine_chain()  # name, segment, position
test = Rig()
test.ik_spline()
test.setup_controls()

# user adjusts spine fk positions if needed
TODO: test.save_controls()

test.guts()
test.clean_up()
"""

import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self):
        self.controls = self.skin_joints = []
        self.root_joint = self.end_joint = None

    def ik_spline(self):
        self.end_joint = self.root_joint.getChildren(ad=1)[0]
        pm.joint(self.root_joint, e=1, oj="xzy", sao="xup", ch=1, zso=1)
        pm.setAttr(self.end_joint.jointOrient, [0, 0, 0])

        hdl, eff, crv = pm.ikHandle(n="spine_HDL",
                                    sj=self.root_joint,
                                    ee=self.end_joint,
                                    sol="ikSplineSolver")
        eff.rename("spine_EFF")
        crv.rename("spine_CRV")
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
        controls["root_transform_CON"] = {
            "rotateOrder": 2,  # zxy
        }
        controls["body_CON"] = {
            "snapTo": self.root_joint,
            "rotateOrder": 2,  # zxy
            "parent": "root_transform_CON"
        }
        controls["hip_CON"] = {
            "snapTo": self.root_joint,
            "rotateOrder": 2,  # zxy
            "parent": "torso_GRP"
        }
        controls["spine1_FK_CON"] = {
            "snapTo": "spine3_result_JNT",
            "rotateOrder": 1,  # yzx
            "parent": "torso_GRP"
        }
        controls["spine2_FK_CON"] = {
            "snapTo": "spine5_result_JNT",
            "rotateOrder": 1,  # yzx
            "parent": "spine1_FK_CON"
        }
        controls["chest_CON"] = {
            "snapTo": self.end_joint,
            "rotateOrder": 2,  # zxy
            "parent": "spine2_FK_CON"
        }

        map(lambda x: pm.group(n=x, w=1), ["dontTouch_GRP", "torso_GRP"])

        for k, v in controls.items():
            con = pm.spaceLocator(n=k)
            ofs = pm.group(con, n=k.replace("CON", "OFS"))

            con.rotateOrder.set(v["rotateOrder"])
            ofs.rotateOrder.set(v["rotateOrder"])

            try:
                pm.matchTransform(ofs, v["snapTo"], pos=1)
                if "FK" in str(ofs):
                    pm.matchTransform(ofs, v["snapTo"])
                pm.parent(ofs, v["parent"], a=1)
            except:
                pass

        pm.parent("torso_GRP", "root_transform_CON")
        pm.parent("root_transform_CON", w=1)
        pm.delete("root_transform_OFS")
        return controls

    def _advanced_twist(self):
        # bind joints
        hip_bind, chest_bind = bind_joints = pm.duplicate(
            self.root_joint,
            self.end_joint,
            po=1)

        hip_bind.rename("hip_bind_JNT")
        chest_bind.rename("chest_bind_JNT")

        map(lambda x: x.rotate.set(0, 0, 0), bind_joints)

        hip_bind.rotateOrder.set(
            self.controls["hip_CON"]["rotateOrder"])
        chest_bind.rotateOrder.set(
            self.controls["chest_CON"]["rotateOrder"])

        pm.parent(chest_bind, w=1)

        pm.skinCluster(bind_joints, "spine_CRV",
                       tsb=1, mi=2, n="spine_bind_SCL")

        pm.parentConstraint("hip_CON", hip_bind, mo=1)
        pm.parentConstraint("chest_CON", chest_bind, mo=1)

        # advanced spline twist settings
        spine_hdl = pm.PyNode("spine_HDL")
        spine_hdl.dTwistControlEnable.set(1)
        spine_hdl.dWorldUpType.set(4)  # object rotation up (start/end)
        spine_hdl.dWorldUpAxis.set(1)
        spine_hdl.dWorldUpVectorY.set(-1)
        spine_hdl.dWorldUpVectorEndY.set(-1)

        hip_bind.worldMatrix[0] >> spine_hdl.dWorldUpMatrix
        chest_bind.worldMatrix[0] >> spine_hdl.dWorldUpMatrixEnd

        pm.select(cl=1)
        return bind_joints

    def _squash_stretch(self):
        # math nodes
        math_nodes = map(lambda x: pm.createNode("floatMath", n=x), [
            "globalScale_spineNormalize_DIV",
            "spine_stretchPercent_DIV",
            "spine_sqrtStretch_POW",
            "spine_stretchInvert_DIV"
        ])

        curve_info = pm.arclen("spine_CRV", ch=1).rename("spineInfo")

        math_nodes[0].operation.set(3)
        curve_info.arcLength >> math_nodes[0].floatA
        pm.PyNode("root_transform_CON").sy >> math_nodes[0].floatB

        math_nodes[1].operation.set(3)
        math_nodes[0].outFloat >> math_nodes[1].floatA
        math_nodes[1].floatB.set(curve_info.arcLength.get())

        math_nodes[2].operation.set(6)
        math_nodes[1].outFloat >> math_nodes[2].floatA
        math_nodes[2].floatB.set(0.5)

        math_nodes[3].operation.set(3)
        math_nodes[3].floatA.set(1)
        math_nodes[2].outFloat >> math_nodes[3].floatB

        # drive result joints
        result_chain = pm.PyNode(self.root_joint)
        result_chain = [result_chain] + result_chain.getChildren(ad=1)
        for jnt in result_chain:
            math_nodes[1].outFloat >> jnt.sx
            math_nodes[3].outFloat >> jnt.sy
            math_nodes[3].outFloat >> jnt.sz
        return

    def guts(self):
        """
        advanced twist
        squash and stretch
        global scale
        """
        self._advanced_twist()
        self._squash_stretch()

        children = [
            "spine_HDL",
            "spine_CRV",
            "hip_bind_JNT",
            "chest_bind_JNT",
            self.root_joint
        ]

        pm.parent(children, "dontTouch_GRP")
        pm.setAttr("dontTouch_GRP.visibility", 0)
        pm.select(cl=1)
        return

    @staticmethod
    def connect(control):
        const_loc = pm.spaceLocator(n="hip{}_const_LOC".format(
            control.split("_", 1)[0].capitalize()))
        pm.matchTransform(const_loc, "hip_CON")
        constraint_node = pm.parentConstraint(const_loc, "torso_GRP", mo=1)
        pm.parent(const_loc, control)
        const_loc.hide()
        pm.select(cl=1)
        return const_loc, constraint_node
    
    def clean_up(self):
        controls = self.controls
        del controls["root_transform_CON"]

        # lock and hide all - offsets and dontTouch_GRP
        items = [pm.PyNode(x) for x in ["torso_GRP", "dontTouch_GRP"]] + \
                [pm.listRelatives(k, p=1)[0] for k in controls.keys()]
        for i in items:
            i = pm.PyNode(i)
            for at in "trs":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
            pm.setAttr(i + ".v", lock=1, keyable=0)
        pm.setAttr("torso_GRP.v", lock=0, keyable=0)
        pm.setAttr("dontTouch_GRP.v", lock=0, keyable=0)

        # lock and hide scale - body, hip, chest
        items = [i+"_CON" for i in ["body", "hip", "chest"]]
        for i in items:
            i = pm.PyNode(i)
            for ax in "xyz":
                pm.setAttr(i.attr("s" + ax), lock=1, keyable=0)

        # lock and hide translate/scale - spine 1 and 2 FK controls
        items = [i+"_FK_CON" for i in ["spine1", "spine2"]]
        for i in items:
            i = pm.PyNode(i)
            for at in "ts":
                for ax in "xyz":
                    pm.setAttr(i.attr(at + ax), lock=1, keyable=0)
        return

