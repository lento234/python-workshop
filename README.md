
# Python workshop

A workshop dedicated to python providing tutorials, challenges and solutions. Covering topics such as numerical computing, just-in-time compilation, plotting, data analysis, and HPC.


## Table of Content


## Workshop outline

1. [01_challenges](01_challenges/README.md): A list of challenges to help you get familiarize with python.
2. [02_tutorials](02_tutorials/README.md)



## Setup and installation


1. Install python (**python 3**) on your computer.

    From [miniconda](https://conda.io/miniconda.html) containing only the essentials such as the `conda` package  manager and `python`. (**Recommended**) 
    
    *or*

    From [anaconda distribution](https://www.anaconda.com/download/) containing all the necessary libaries for scientific research. Warning: very large, includes lots of conda packages by default.
   
2. Download this python tutorial github repository on to your computer.

    *Clone this `github` repository locally to you computer:*
      
        $ git clone https://gitlab.empa.ch/305/python-workshop.git
      
    *Change your directory to the tutorial folder:*
      
        $ cd python-workshop
   
3. Create a new conda environment for this tutorial.

    *Option 1: Manually creating an environment*

        $ conda create --name py-workshop python=3.9 pip
    
    *Option 2: Installing from the `yaml` file included in this repository:*
    
        $ conda env create -f environment.yml
    
4. Activate the conda `py-workshop` environment.

        $ conda activate py-workshop

5. Installing additional packages if need into the conda environment using `pip`.

        $ pip install numpy numba matplotlib jupyterlab
    
6. Starting `JupyterLab` for working with notebooks.

        $ jupyter lab

6. *(Cleanup)* Deactivate your environment when you are done.

        $ conda deactivate 

7. *(Cleanup)* Removing your `py-workshop` environment if you don't want it anymore.

    *You can delete the environment by using the following in a terminal prompt:*

        $ conda env remove --name py-workshop --yes


## References

### Installation and usage

- [git](https://git-scm.com/)
- [Conda](https://conda.io/projects/conda/en/latest/index.html)
- [miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [anaconda (python + libraries)](https://www.anaconda.com/distribution/)
- [pure python](https://www.python.org/downloads/)
- [Visual studio code](https://code.visualstudio.com/)
- [Docker](https://hub.docker.com/)

### Cheatsheet

- [Numpy for matlab users](https://docs.scipy.org/doc/numpy/user/numpy-for-matlab-users.html)
- [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Tutorials

- [Lecture series on scientific python by jrjohansson](https://github.com/jrjohansson/scientific-python-lectures)
- [Python datascience handbook online series](https://jakevdp.github.io/PythonDataScienceHandbook/index.html)
- [Scipy 2019 conference videos](https://www.youtube.com/user/EnthoughtMedia/videos)
- [Scipy 2019 jupyterlab tutorial](https://github.com/jupyterlab/scipy2019-jupyterlab-tutorial)
- [Lecture series on scientific python by jrjohansson](https://github.com/jrjohansson/scientific-python-lectures)
- [Scipy Lecture notes](https://scipy-lectures.org/)
- [Quantitative Big Imaging 2019 by Kevin Mader (ETHZ)](https://github.com/kmader/Quantitative-Big-Imaging-2019)
- [Dask examples tutorial](https://github.com/dask/dask-examples)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

### Jupyter

- [Latex + jupyter](https://github.com/jupyterlab/jupyterlab-latex)
- [Git + jupyter](https://github.com/jupyterlab/jupyterlab-git)
- [ipywidgets + jupyter](https://github.com/jupyter-widgets/ipywidgets)
- [Awesome jupyter notebooks](https://github.com/markusschanta/awesome-jupyter)
- [Dask + jupyter](https://github.com/dask/dask-labextension)

### Scientific libraries

- [Pangeo](https://pangeo.io/)
- [Dask-jobqueue at PBSCluster](https://andersonbanihirwe.dev/talks/dask-jupyter-scipy-2019.html)
- [Awesome python](https://awesome-python.com)
