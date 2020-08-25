"""
import sys
pth = r"PATH/rockstar"
if pth not in sys.path:
    sys.path.append(pth)
    print ">> Added:", pth

from tools import transfer_animation as rt

reload(rt)
rt.TransferAnimation()
"""

import pymel.core as pm
import json


class TransferAnimation:
    def __init__(self):
        print ">>"

    @staticmethod
    def get_selection():
        return pm.selected()[0]

    def save_data(self, save_filename, attributes=[]):
        obj = self.get_selection()

        data = self.get_data(obj, attributes)

        with open(save_filename, "w") as save_file:
            json.dump(data, save_file, sort_keys=1, indent=4)

    @staticmethod
    def get_data(obj, attributes):
        animation_data = {}

        for attr in attributes:
            obj_attr = obj.attr(attr)

            keyframes_dict = {}
            key_values = pm.keyframe(obj_attr, q=1, tc=1, vc=1)
            for i, (k, v) in enumerate(key_values):
                ia, oa, iw, ow, itt, ott, lock = \
                    pm.keyTangent(obj_attr, q=1, index=[i], ia=1, oa=1,
                                  iw=1, ow=1, itt=1, ott=1, lock=1)

                keyframes_dict[k] = {
                    "value": v,
                    "inAngle": ia,
                    "outAngle": oa,
                    "inWeight": iw,
                    "outWeight": ow,
                    "inTangentType": str(itt),
                    "outTangentType": str(ott),
                    "lock": lock
                }

            attribute_dict = {
                "weighted": pm.keyTangent(obj_attr, q=1, wt=1)[0],
                "preInfinity": str(pm.setInfinity(obj_attr, q=1, pri=1)[0]),
                "postInfinity": str(pm.setInfinity(obj_attr, q=1, poi=1)[0]),
                "keyframes": keyframes_dict
            }

            animation_data[attr] = attribute_dict
        return animation_data

    def load_data(self, load_filename, start_frame=None):
        obj = self.get_selection()

        with open(load_filename, "r") as read_file:
            data = json.load(read_file)

        self.set_keys(obj, data, start_frame)

    def set_keys(self, obj, data, start_frame=None):
        offset_value = self.get_offset_value(data, start_frame)

        for attr, attribute_dict in data.items():
            obj_attr = obj.attr(attr)
            keyframes = sorted(attribute_dict["keyframes"])

            # set keyframes to their values
            for k in keyframes:
                params = {
                    "time": float(k) - offset_value,
                    "value": attribute_dict["keyframes"][k]["value"]
                }
                pm.setKeyframe(obj_attr, **params)

            # set global attributes on animation curve - weight, post and pre
            pm.keyTangent(obj_attr, e=1, wt=attribute_dict["weighted"])
            pm.setInfinity(obj_attr,
                           pri=attribute_dict["preInfinity"],
                           poi=attribute_dict["postInfinity"])

            # update tangents on each keyframe - locked, angle, weight, type
            for i, k in enumerate(keyframes):
                keyframe_data = attribute_dict["keyframes"][k]

                params = {
                    "l": keyframe_data["lock"],
                    "ia": keyframe_data["inAngle"],
                    "iw": keyframe_data["inWeight"],
                    "oa": keyframe_data["outAngle"],
                    "ow": keyframe_data["outWeight"]
                }
                pm.keyTangent(obj_attr, e=1, index=[i], **params)

                params = {
                    "itt": keyframe_data["inTangentType"],
                    "ott": keyframe_data["outTangentType"],
                }
                pm.keyTangent(obj_attr, e=1, index=[i], **params)
        return

    @staticmethod
    def get_offset_value(data, start_frame=None):
        if start_frame is None:
            return 0

        data_start_frame = float(min([sorted(attribute_dict["keyframes"])[0]
                                      for attribute_dict in data.values()]))
        return data_start_frame - start_frame
