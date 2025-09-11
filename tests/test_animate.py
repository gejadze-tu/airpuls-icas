from pathlib import Path
from matplotlib.animation import FuncAnimation

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from animate import *

data_dir = Path("../data")

def test_animate_iq_data(data_dir: Path):

    files = sorted([f for f in data_dir.iterdir() if f.is_file()])
    ani = animate_iq_data(files, interval=500)
    assert isinstance(ani, FuncAnimation)

if __name__ == "__main__":
    test_animate_iq_data(data_dir)