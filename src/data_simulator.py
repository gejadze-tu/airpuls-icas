import time
import shutil
from pathlib import Path


def simulate_measurements(
    source_dir: Path,
    target_dir: Path,
    interval: float = 1.0
):

    source_files = sorted([f for f in source_dir.iterdir() if f.is_file()])
    if not source_files:
        raise ValueError("Source directory must contain at least one file.")
    
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
