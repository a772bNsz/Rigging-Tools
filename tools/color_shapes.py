import pymel.core as pm


class ColorShapes:
    def __init__(self):
        self.sel = pm.ls(sl=1)
        self.index = None
        return

    def by_index(self):
        for crv in self.sel:
            for shp in crv.getShapes():
                shp.overrideEnabled.set(1)
                shp.overrideColor.set(self.index)

        rgb = map(lambda x: int(x*255), pm.colorIndex(self.index, q=1))
        self.sel = self.index = None
        return rgb
