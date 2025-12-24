import time

# =========================
# Render Time - Start Node
# =========================
class RenderTimeStart:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("STRING",),  # execution trigger
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("start_time",)
    FUNCTION = "start"
    CATEGORY = "utils/timer"

    def start(self, trigger):
        start_time = time.time()
        return (start_time,)


# =========================
# Render Time - End Node
# =========================
class RenderTimeEnd:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_time": ("FLOAT",),
                "trigger": ("VHS_FILENAMES",),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("render_time_seconds",)
    FUNCTION = "end"
    CATEGORY = "utils/timer"

    def end(self, start_time, trigger):
        duration = max(0.0, time.time() - start_time)
        print(f"[RenderTime] Render finished in {duration:.2f} seconds")
        return (duration,)


# =========================
# ComfyUI Mappings
# =========================
NODE_CLASS_MAPPINGS = {
    "RenderTimeStart": RenderTimeStart,
    "RenderTimeEnd": RenderTimeEnd,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RenderTimeStart": "⏱️ Render Time Start",
    "RenderTimeEnd": "⏱️ Render Time End",
}
