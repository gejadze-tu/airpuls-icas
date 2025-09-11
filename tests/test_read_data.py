from pathlib import Path
import numpy as np
from matplotlib.figure import Figure

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from read_data import *


data_dir = Path("../data")

# Retrieve the first file in the directory for testing
def get_file_from_dir(data_dir: Path) -> Path:
    files = sorted([f for f in data_dir.iterdir() if f.is_file()])
    if not files:
        raise IndexError("No files in the directory.")
    return files[0]

def test_read_raw_iq_data(data_file: Path) -> np.ndarray[np.complex128]:
    raw_iq = read_raw_iq_data(data_file)
    assert np.iscomplexobj(raw_iq)
    assert raw_iq.size == (4 * 2 * 1 * 4096)  # adjust if your file size differs
    return raw_iq

def test_process_raw_iq_data(raw_iq):
    processed_iq = process_raw_iq_data(raw_iq)
    assert processed_iq.shape == (4, 2, 1, 4096)
    return processed_iq

def test_plot_processed_iq_data(processed_iq):
    fig = plot_processed_iq_data(processed_iq)
    assert isinstance(fig, Figure)
    return fig

if __name__ == "__main__":
    data_file = get_file_from_dir(data_dir)
    print(f"Testing with file: {data_file}")
    print("\n")

    raw_iq = test_read_raw_iq_data(data_file)
    print(f"Raw IQ Data:\n{raw_iq}")
    print(f"Shape: {raw_iq.shape}")
    print("\n")

    processed_iq = test_process_raw_iq_data(raw_iq)
    print(f"Processed IQ Data:\n{processed_iq}")
    print(f"Shape: {processed_iq.shape}")
    print("\n")

    fig = test_plot_processed_iq_data(processed_iq)