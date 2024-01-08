import os
import time
from pathlib import Path

from tqdm import tqdm


def main():
    """
    Once this is function running, we cannot stop without losing data.
    Or can we?
    """
    important_stuff = []
    for i in tqdm(range(100000), desc="progress"):
        time.sleep(0.005)
        important_stuff.append(i)

    write_results(important_stuff)


def write_results(important_stuff):
    Path("important_stuff.txt").write_text("\n".join(map(str, important_stuff)))


if __name__ == "__main__":
    print("PID:", os.getpid())
    main()
