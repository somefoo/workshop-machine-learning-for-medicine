# Workshop for the Lecture: Surgical Technology Innovation
## System requirements
* Ubuntu 18.04 or MacOSX. Windows 10 might work as well, but was not tested.
* git ([installation instructions](https://git-scm.com/downloads))
* Python 3.7 or later ([download](https://www.python.org/downloads/))
* *optional* [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/)

## Installation
1. Clone this repository. `git@github.com:somefoo/workshop-machine-learning-for-medicine.git`
2. Go into the cloned folder. `cd workshop-machine-learning-for-medicine`
3. Execute the setup script `python3 setup_env.py`. Per default, this will create a virtual environment with all the required packages and download a dataset. If you would rather use a conda/miniconda environment, use `python3 setup_env.py --conda`. By default, both the venv and conda option will install the pytorch for CPU. This will be the case if you are on a laptop or desktop without a strong dedicated graphics card. If you would like to use the GPU version instead, please manually install the correct version from [here](https://pytorch.org/get-started/locally/) **AFTER** executing the setup script and sourcing your environment. Sadly, the original server hosting the dataset doesn't exist anymore. Ask me for the original data (we will try to host it ourselves).
4. Activate the environment; either `source .venv/bin/activate` or the conda environment `conda activate workshop`
5. Start a jupyter notebook server `jupyter notebook`.
6. Open chrome or firefox and go to `http://localhost:8888/tree`.
7. Open the `Introduction Tutorial.ipynb` notebook to get started.
8. Continue to the `Skin Cancer Classification.ipynb` notebook.

## Information
This workshop is part of the lecture Surgical Technology Innovation and Robotics in Surgery and Diagnostics. More information on [SPARC](https://www.sparc.tf.fau.de/) on our websites.

## Source
This workshop is based on the workshop by Paul Maria Scheikl presented at CURAC 2021: [Link](https://github.com/ScheiklP/CURAC-Academy-2021)
