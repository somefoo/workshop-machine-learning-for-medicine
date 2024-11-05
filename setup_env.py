import subprocess
from pathlib import Path
import zipfile

try:
    import requests
except ModuleNotFoundError:
    raise ModuleNotFoundError("[SPARC ERROR]: please install the requests package before continuing.\n \t pip3 install requests")


def download_url(url: str, save_path: Path, chunk_size=128):
    r = requests.get(url, stream=True)
    size = r.headers["content-length"]
    length = int(int(size) / chunk_size)
    with open(str(save_path.absolute()), "wb") as fd, progress(
        total=length * chunk_size, unit_scale=True, unit_divisor=1024, unit="B", desc=save_path.name
    ) as pbar:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
            pbar.update(chunk_size)


if __name__ == "__main__":
    try:
        out = subprocess.check_output(["conda", "--version"])
    except OSError:
        raise RuntimeError("Conda (Miniconda or Anaconda) must be installed. https://docs.conda.io/en/latest/miniconda.html")

    print("[SPARC INFO]: Creating a new conda environment named workshop and installing packages...")
    print(f"[SPARC INFO]: Pytorch will be installed (cpu only support).")

    try:
        subprocess.check_call(
            ["conda", "env", "create", "--file", "conda_cpu.yml"]
        )
    except:
        print("[SPARC WARNING]: Conda environment already exists.")
        

    print("[SPARC INFO]: Done!")
