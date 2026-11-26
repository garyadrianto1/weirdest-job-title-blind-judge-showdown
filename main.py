import os

LINE = "Senior Apologizer for Elevators That Stop Between Floors"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd()
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
