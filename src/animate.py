import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.axes import Axes
from pathlib import Path
from read_data import read_raw_iq_data, process_raw_iq_data

def animate_iq_data(data_files: list[Path], interval=500):

    fig, axes = plt.subplots(4, 2, figsize=(10, 6), sharex=True, sharey=True)
    axes = np.atleast_2d(axes)
    lines = [[axes[rx, tx].plot([], [])[0] for tx in range(2)] for rx in range(4)]

    def init():
        for rx in range(4):
            for tx in range(2):
                ax: Axes = axes[rx, tx]
                ax.set_xlim(0, 4096)
                ax.set_ylim(0, pow(2, 13))
                ax.set_title(f'RX{rx+1} - TX{tx+1}')
                ax.grid(True)
                if tx == 0:
                    ax.set_ylabel('Magnitude')
                if rx == 3:
                    ax.set_xlabel('Subcarrier Index')
        return [line for sublist in lines for line in sublist]

    def update(frame):
        raw_iq = read_raw_iq_data(data_files[frame])
        iq_reshaped = process_raw_iq_data(raw_iq)
        for rx in range(4):
            for tx in range(2):
                lines[rx][tx].set_data(np.arange(4096), np.abs(iq_reshaped[rx, tx, 0, :]))
        fig.suptitle(f"Frame {frame}")
        return [line for sublist in lines for line in sublist]

    ani = FuncAnimation(fig, update, frames=len(data_files), init_func=init, blit=False, interval=interval)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    return ani
