import pymel.core as pm


def joint_chain(curve, number=2, name="joint#", root=None):
    pm.select(cl=1)
    pm.rebuildCurve(curve, s=20)
    for i in range(number):
        percent = i / (number - 1.0)
        position = pm.pointOnCurve(curve, pr=percent, p=1, top=1)
        joint = pm.joint(p=position, a=1, n=name.replace("#", str(i+1)))
        if i == 0:
            root = joint
    return root
