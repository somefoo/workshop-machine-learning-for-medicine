# Workshop for the Lecture: Surgical Technology Innovation
## System requirements
* Ubuntu 18.04 or MacOSX. Windows 10 might work as well, but was not tested.
* git ([installation instructions](https://git-scm.com/downloads))
* Python 3.7 or later ([download](https://www.python.org/downloads/))
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/)

## Installation
1. Clone this repository. `git@github.com:somefoo/workshop-machine-learning-for-medicine.git`
2. Go into the cloned folder. `cd workshop-machine-learning-for-medicine`
3. Execute the setup script `python3 setup_env.py`. This will create a new conda environment, install all required packages and download a dataset. If you do not want to use the gpu version of pytorch, call the script as `python3 setup_env.py --cpu`. This will be the case if you are on a laptop or desktop without a strong dedicated graphics card. Sadly, the original server hosting the dataset doesn't exist anymore. Ask me for the original data (we will try to host it ourselves).
4. Activate the conda environment `conda activate workshop`
5. Start a jupyter notebook server `jupyter notebook`.
6. Open chrome or firefox and go to `http://localhost:8888/tree`.
7. Open the `Introduction Tutorial.ipynb` notebook to get started.
8. Continue to the `Skin Cancer Classification.ipynb` notebook.

## Information
This workshop is part of the lecture Surgical Technology Innovation. More information on [SPARC](https://www.sparc.tf.fau.de/) on our websites.

## Source
This workshop is based on the workshop by Paul Maria Scheikl presented at CURAC 2021: [Link](https://github.com/ScheiklP/CURAC-Academy-2021)
