import time

# ======================================================
# Render Time - Start Node CONDITIONING
# ======================================================
class RenderTimeStart:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "trigger": ("CONDITIONING",)  # execution trigger
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("start_time",)
    FUNCTION = "start"
    CATEGORY = "utils/timer"

    def start(self, trigger):
        start_time = time.time()
        return (start_time,)


# ======================================================
# Render Time - End Node
# ======================================================
class RenderTimeEnd:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_time": ("FLOAT",),
                "trigger": ("VHS_FILENAMES",)
            }
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("render_time_seconds",)
    FUNCTION = "end"
    CATEGORY = "utils/timer"

    def end(self, start_time, trigger):
        duration = max(0.0, time.perf_counter() - start_time)
        print(f"[RenderTime] Render finished in {duration:.2f} seconds")
        return (duration,)


# ======================================================
# Render Time - Pass Through (Execution Anchor)
# ======================================================
class RenderTimePassThrough:
    """
    Node ini BERFUNGSI PENTING:
    - Memastikan RenderTimeEnd masuk execution graph
    - Mencegah node merah (invalid execution)
    - Tidak mengubah data sama sekali
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input": ("ANY",),
                "trigger": ("ANY",),
            }
        }

    RETURN_TYPES = ("ANY",)
    RETURN_NAMES = ("output",)
    FUNCTION = "run"
    CATEGORY = "utils/timer"

    def run(self, input, trigger):
        return (input,)


# ======================================================
# ComfyUI Node Mappings
# ======================================================
NODE_CLASS_MAPPINGS = {
    "RenderTimeStart": RenderTimeStart,
    "RenderTimeEnd": RenderTimeEnd,
    "RenderTimePassThrough": RenderTimePassThrough,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RenderTimeStart": "⏱ Render Time Start",
    "RenderTimeEnd": "⏱ Render Time End",
    "RenderTimePassThrough": "⏱ Render Time Pass Through",
}
