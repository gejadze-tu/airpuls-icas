from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from data_simulator import simulate_measurements

src_path = Path("../data")
tgt_path = Path("../simulated_data")

if __name__ == "__main__":
    simulate_measurements(src_path, tgt_path, interval=1.0, max_files=5)
    