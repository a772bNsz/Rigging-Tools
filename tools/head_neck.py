import pymel.core as pm
from collections import OrderedDict


class Rig:
    def __init__(self, root):
        self.controls = []

        neck_chain = [root] + root.getChildren(ad=1)[::-1]
        i = 1
        for jnt in neck_chain[1:-1]:
            jnt.rename("neck_mid{}_result_JNT".format(i))
            i += 1
        self.root_joint = neck_chain[0].rename("neck_base_result_JNT")
        self.end_joint = neck_chain[-1].rename("neck_end_result_JNT")

    def ik_spline(self):
        self.end_joint = self.root_joint.getChildren(ad=1, type="joint")[0]
        pm.joint(self.root_joint, e=1, oj="xzy", sao="xup", ch=1, zso=1)
        self.end_joint.jointOrient.set(0, 0, 0)
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

            pm.matchTransform(ofs, v["snapTo"], pos=1)
            pm.parent(ofs, v["parent"], a=1)

        pm.parent("head_neck_GRP", "root_transform_CON")
        pm.parent("root_transform_CON", w=1)

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

        pm.parent(neck_end_bind, neck_base_bind)
        pm.joint(neck_base_bind, e=1, oj="yxz", sao="xup", ch=1, zso=1)
        neck_end_bind.jointOrient.set(0, 0, 0)
        pm.parent(neck_end_bind, w=1)

        neck_base_bind.rotateOrder.set(
            self.controls["neck_CON"]["rotateOrder"])
        neck_end_bind.rotateOrder.set(
            self.controls["head_CON"]["rotateOrder"])

        pm.skinCluster(bind_joints, "neck_CRV",
                       tsb=1, mi=2, n="neck_bind_SCL")

        pm.matchTransform("neck_OFS", neck_base_bind, rot=1)
        # pm.matchTransform("head_OFS", neck_end_bind, rot=1)
        pm.parentConstraint("neck_CON", neck_base_bind)
        pm.parentConstraint("head_CON", neck_end_bind)

        # advanced spline twist settings
        neck_hdl = pm.PyNode("neck_HDL")
        neck_hdl.dTwistControlEnable.set(1)
        neck_hdl.dWorldUpType.set(4)  # object rotation up (start/end)
        neck_hdl.dWorldUpAxis.set(1)
        neck_hdl.dWorldUpVectorY.set(0)
        neck_hdl.dWorldUpVectorZ.set(-1)
        neck_hdl.dWorldUpVectorEndY.set(0)
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
        return math_nodes

    @staticmethod
    def _stretchable_neck(target, control, name):
        stretch_toggle = \
            pm.createNode("blendTwoAttr", n=name + "_stretchToggle")

        source, = target.inputs(p=1)
        source >> stretch_toggle.input[1]
        stretch_toggle.input[0].set(stretch_toggle.input[1].get())
        stretch_toggle.output >> target

        attr = "stretchable"
        attribute_exists = pm.attributeQuery(attr, node=control, exists=1)
        if not attribute_exists:
            pm.addAttr(control, ln="stretchable",
                       k=1, at="float", min=0, max=1, dv=1)

        control.stretchable >> stretch_toggle.attributesBlender
        return True

    def guts(self):
        """
        advanced twist
        squash and stretch
        global scale
        """
        self._advanced_twist()
        math_nodes = self._squash_stretch()

        stretch_percent = math_nodes[1].floatA
        params = {
            "target": stretch_percent,
            "control": pm.PyNode("head_CON"),
            "name": "neck"
        }
        self._stretchable_neck(**params)

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

    @staticmethod
    def connect(control):
        const_loc = pm.spaceLocator(n="neck{}_const_LOC".format(
            control.split("_", 1)[0].capitalize()))
        pm.matchTransform(const_loc, "neck_OFS")

        connection_nodes = [
            const_loc,
            pm.parentConstraint(const_loc, "neck_OFS")]

        pm.parent(const_loc, control)
        const_loc.hide()
        return connection_nodes

    def space_switch(self, controls):
        # SPACE LOCATORS
        space_locators = []
        for con in controls:
            name = con.split("_")[0].capitalize()
            space_locators += [
                pm.spaceLocator(n="head{}_space_LOC".format(name))]
            pm.matchTransform(space_locators[-1], "head_CON")

        # SPACE ATTRIBUTES
        pm.addAttr("head_CON", ln="rotationSpace", at="enum", k=1,
                   en=":".join(map(lambda x: x.split("_")[0], controls)))
        pm.addAttr("head_CON", ln="translationSpace", at="enum", k=1,
                   en=":".join(map(lambda x: x.split("_")[0], controls)))

        # ROTATION SPACE SET DRIVEN KEY
        ori_const = pm.orientConstraint(space_locators, "head_OFS", mo=1)
        rotation_space_values = [c.split("_")[0] for c in controls]

        for dv in rotation_space_values:
            # key all weights to 0
            map(lambda x:
                pm.setDrivenKeyframe(
                    x,
                    cd="head_CON.rotationSpace",
                    dv=rotation_space_values.index(dv),
                    v=0,
                    itt="auto",
                    ott="step"),
                ori_const.listAttr(st="*_space_*"))

            # key weight matching driven value to 1
            weight = ori_const.listAttr(
                st="head{}_space_LOC*".format(dv.capitalize()))[0]

            pm.setDrivenKeyframe(
                weight,
                currentDriver="head_CON.rotationSpace",
                driverValue=rotation_space_values.index(dv),
                value=1,
                itt="auto",
                ott="step"
            )

        # TRANSLATION SPACE SET DRIVEN KEY
        pt_const = pm.pointConstraint(space_locators, "head_OFS", mo=1)
        translation_space_value = [c.split("_")[0] for c in controls]

        for dv in translation_space_value:
            # key all weights to 0
            map(lambda x:
                pm.setDrivenKeyframe(
                    x,
                    cd="head_CON.translationSpace",
                    dv=translation_space_value.index(dv),
                    v=0,
                    itt="auto",
                    ott="step"),
                pt_const.listAttr(st="*_space_*"))

            # key weight matching driven value to 1
            weight = pt_const.listAttr(
                st="head{}_space_LOC*".format(dv.capitalize()))[0]

            pm.setDrivenKeyframe(
                weight,
                currentDriver="head_CON.translationSpace",
                driverValue=translation_space_value.index(dv),
                value=1,
                itt="auto",
                ott="step"
            )

            for loc, con in zip(space_locators, controls):
                pm.parent(loc, con, a=1)
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

        # hide all space locators
        pm.hide(pm.ls("head*_space_LOC"))
        return True

