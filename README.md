# Modified Python Data Science container

This a modified version of the Python Data Science container by [Andrei Maksimov] (https://github.com/andreivmaksimov/python_data_science). The main difference is the inclusion of NLTK and its downloads, as well as use of token authentication in Jupyter; it is otherwise identical. For more information on the original, please see https://github.com/andreivmaksimov/python_data_science/blob/master/README.md

The Docker contains:
 - NumPy
 - Pandas
 - Sklearn
 - Matplotlib
 - Seaborn
 - pyyaml
 - h5py
 - Jupyter
 - Tensorflow
 - Keras
 - OpenCV 3
 - NLTK

The container is built on top of a [Ubuntu 16.04 Docker container](https://hub.docker.com/_/ubuntu/).

### Running the container

Create a folder ```notebooks``` (for example) to store Jupyter Notebooks:
```sh
mkdir notebooks
```

Build Docker and name it ds_container (make sure you're building in the folder containing Dockerfile, and conf/.jupyter/jupyter_notebook_config.py:
```sh
sudo docker build -t ds_container . 
```

Run the Docker container with the following command:
```sh
docker run -it -p 8888:8888 -p 6006:6006 -v $(pwd)/notebooks:/notebooks  ds_container
```
The following parameters are used:
- ```-p 8888:8888``` to export Jupyter Web interface
- ```-p 6006:6006``` to export TensorflowDashboard Web interface
- ```-d``` to run the Docker container in background
- ```-v $(pwd)/notebooks:/notebooks``` to mount the *notebooks* folder inside the container

Original copyright:
&copy; [Andrei Maksimov](https://www.linkedin.com/in/avmaksimov/) / [ProgKids.ru](https://progkids.ru/)
