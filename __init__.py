"""Magik List Prepend: prepend text to selected 1-based list positions."""


class MagikListPrepend:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Text List": ("STRING", {"forceInput": True, "tooltip": "List of strings to modify."}),
                "Add": ("STRING", {"default": "", "multiline": True, "dynamicPrompts": False,
                                   "tooltip": "Exact prefix; include any desired separator."}),
            },
            "optional": {
                "Quadrants": ("INT", {"forceInput": True,
                                      "tooltip": "1-based positions: 1 selects the first string. Unconnected selects all; an empty list selects none."}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prep Text",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "execute"
    CATEGORY = "Magik/Text"
    DESCRIPTION = "Prepend Add to strings selected by 1-based Quadrants indices."

    def execute(self, **inputs):
        return self.prepend(inputs["Text List"], inputs["Add"], inputs.get("Quadrants"))

    def prepend(self, text_list, add, quadrants=None):
        # INPUT_IS_LIST wraps scalar widget values in a list as well.
        if len(add) != 1 or not isinstance(add[0], str):
            raise ValueError("Add must contain exactly one string.")
        if any(not isinstance(text, str) for text in text_list):
            raise TypeError("Text List must contain strings only.")
        if quadrants is None:
            selected = None
        else:
            if any(isinstance(index, bool) or not isinstance(index, int) for index in quadrants):
                raise TypeError("Quadrants must contain integers only.")
            selected = {index for index in quadrants if 1 <= index <= len(text_list)}
        prefix = add[0]
        return ([prefix + text if selected is None or position in selected else text
                 for position, text in enumerate(text_list, start=1)],)


NODE_CLASS_MAPPINGS = {"MagikListPrepend": MagikListPrepend}
NODE_DISPLAY_NAME_MAPPINGS = {"MagikListPrepend": "Magik List Prepend"}
