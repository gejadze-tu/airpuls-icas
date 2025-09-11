import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def read_raw_iq_data(data_file_path: Path) -> np.ndarray[np.complex128]:
    with open(data_file_path, 'rb') as f:
        array = np.fromfile(f, dtype=np.int16)
    raw_iq = array[::2] + 1j * array[1::2]
    raw_iq = raw_iq.astype(np.complex128)
    return raw_iq

def process_raw_iq_data(raw_iq: np.ndarray[np.complex128]) -> np.ndarray[np.complex128]:
    iq_processed = raw_iq.reshape((4, 2, 1, 4096))
    iq_processed = np.fft.ifftshift(iq_processed)
    return iq_processed

def plot_processed_iq_data(iq_processed: np.ndarray[np.complex128]) -> Figure:
    fig, axes = plt.subplots(4, 2, figsize=(12, 8), sharex=True)
    axes = np.atleast_2d(axes)

    for rx in range(4):
        for tx in range(2):
            ax: Axes = axes[rx, tx]
            ax.plot(np.abs(iq_processed[rx, tx, 0, :]))
            ax.set_title(f'RX{rx+1} - TX{tx+1}')
            ax.set_ylabel('Magnitude')
            ax.grid(True)
            if rx == 3:
                ax.set_xlabel('Subcarrier Index')

    plt.tight_layout()
    plt.show()

    return fig
