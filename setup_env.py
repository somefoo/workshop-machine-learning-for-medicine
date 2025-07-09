import subprocess
from pathlib import Path
import argparse


def download_url(url: str, save_path: Path, chunk_size=128):
    try:
        import requests
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "[SPARC ERROR]: please install the requests package before continuing.\n \t pip3 install requests"
        )

    r = requests.get(url, stream=True)
    size = r.headers["content-length"]
    length = int(int(size) / chunk_size)
    with open(str(save_path.absolute()), "wb") as fd, progress(
        total=length * chunk_size,
        unit_scale=True,
        unit_divisor=1024,
        unit="B",
        desc=save_path.name,
    ) as pbar:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
            pbar.update(chunk_size)


def use_conda():
    try:
        out = subprocess.check_output(["conda", "--version"])
    except OSError:
        raise RuntimeError(
            "Conda (Miniconda or Anaconda) must be installed. https://docs.conda.io/en/latest/miniconda.html"
        )

    print(
        "[SPARC INFO]: Creating a new conda environment named workshop and installing packages..."
    )
    print(f"[SPARC INFO]: Pytorch will be installed (cpu only support).")

    try:
        subprocess.check_call(["conda", "env", "create", "--file", "conda_cpu.yml"])
    except:
        print("[SPARC WARNING]: Conda environment already exists.")

    print("[SPARC INFO]: Done!")


def use_venv():
    try:
        import venv
    except ImportError:
        raise ImportError(
            "Python venv module is not available. Please install Python 3.3 or later."
        )

    print(
        "[SPARC INFO]: Creating a new virtual environment named .venv and installing packages..."
    )

    venv.create(".venv", with_pip=True)

    venv_pip_path = Path(".venv") / "bin" / "pip"
    if not venv_pip_path.exists():
        # Try a windows compatible path
        venv_pip_path = Path(".venv") / "Scripts" / "pip.exe"
        if not venv_pip_path.exists():
            raise RuntimeError("[SPARC ERROR]: Could not find the virtual environment.")

    subprocess.check_call(
        [
            str(venv_pip_path),
            "install",
            "livelossplot",
            "torchsummary",
            "numpy",
            "notebook",
            "ipywidgets",
            "pandas",
            "pillow",
            "tqdm",
            "matplotlib",
            "requests",
        ]
    )

    print("[SPARC INFO]: Downloading and installing PyTorch (cpu only support)...")
    subprocess.check_call(
        [
            str(venv_pip_path),
            "install",
            "torch",
            "torchvision",
            "torchaudio",
        ]
    )

    print(
        "[SPARC INFO]: If you would like to use the GPU version of pytorch, please install the correct one manually from here: https://pytorch.org/get-started/locally/"
    )

    print("[SPARC INFO]: Done!")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Setup environment for the workshop.")
    parser.add_argument(
        "--conda",
        action="store_true",
        help="Use conda to create the environment.",
    )
    args = parser.parse_args()

    if args.conda:
        use_conda()
    else:
        use_venv()
