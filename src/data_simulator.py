import time
import shutil
from pathlib import Path
import re



def simulate_measurements(
    source_dir: Path,
    target_dir: Path,
    interval: float = 1.0,
    max_files: int = None
):

    def alphanum_key(f):
        # Split filename into list of strings and integers for natural sorting
        return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', f.name)]

    source_files = sorted([f for f in source_dir.iterdir() if f.is_file()], key=alphanum_key)
    if not source_files:
        raise ValueError("Source directory must contain at least one file.")

    if max_files is not None:
        source_files = source_files[:max_files]

    # Ensure target directory exists
    target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Starting simulation: copying {len(source_files)} files every {interval} seconds.")
    try:
        while True:
            for src_file in source_files:
                dst_file = target_dir / src_file.name
                shutil.copy(src_file, dst_file)  # copy sets mtime to now
                print(f"Copied {src_file.name} to {dst_file}")
                time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
