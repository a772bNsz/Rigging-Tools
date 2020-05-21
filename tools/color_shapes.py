import pymel.core as pm
import webcolors
import json


class ColorShapes:
    def __init__(self):
        self.sel = pm.ls(sl=1)
        self.rgb = []
        self.json_file = __file__.split(".")[0] + ".json"
        self.get = self._get()
        return

    def _assign(self, name, rgb=None):
        self.get.update({name: rgb})
        with open(self.json_file, "w") as f:
            json.dump(self.get, f, indent=4)
        return True

    def _get(self):
        with open(self.json_file) as f:
            return json.load(f)

    def set(self, arg, name="", rgb=None, add=0):
        if add and name:
            rgb = self.get[name]
            self._assign(arg, rgb=rgb)
        elif add and rgb:
            self._assign(arg, rgb=rgb)

        if isinstance(arg, str):
            try:
                self.rgb = self.get[arg]
            except KeyError:
                try:
                    self.rgb = webcolors.name_to_rgb(arg)
                except ValueError:
                    self.rgb = None
                    raise ValueError("'{}' not found".format(arg))
        elif isinstance(arg, list):
            self.rgb = arg

        for s in self.sel:
            s.overrideEnabled.set(1)
            s.overrideRGBColors.set(1)
            s.overrideColorRGB.set(*self.rgb)

        self.rgb = None
        return True
