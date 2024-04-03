# Chest Disease Classification from Chest CT Scan Image

# Introduction

Chest CT scan images hold invaluable diagnostic potential in identifying various pulmonary conditions, including malignant tumors. Our project aims to streamline the classification process of these images into four distinct classes: 'adenocarcinoma', 'large cell carcinoma', 'normal', and 'squamous cell carcinoma'. Through the utilization of advanced techniques such as Deep Learning and Data Version Control (DVC), coupled with the robust ResNet50 architecture, I have developed an end-to-end pipeline that ensures efficient and accurate classification of chest CT scan images.

In addition to these methodologies, our project also integrates MLflow, a powerful machine learning lifecycle management tool. MLflow facilitates experiment tracking, model management, and reproducibility, allowing us to monitor and compare multiple models, hyperparameters, and experiments seamlessly. Through the synergy of DVC for data versioning and MLflow for model management, our project ensures transparency, reproducibility, and continuous improvement in the development and deployment of machine learning models.
## Tech Stack Used
1) Python
2) Flask
3) Deep Learning Algorithms

## Dataset

Dataset for this Project is taken from Kaggle. Here is the Dataset [Link](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images/data).

## Dataset Information

* Images are not in dcm format, the images are in jpg or png to fit the model.
* Data contain 3 chest cancer types which are Adenocarcinoma,Large cell carcinoma, Squamous cell carcinoma , and 1 folder for the normal cell.
* Data folder is the main folder that contain all the step folders inside Data folder are test , train , valid.

* test represent testing set
* train represent training set
* valid represent validation set
* training set is 70%
* testing set is 20%
* validation set is 10%

## Installation

The Code is written in Python 3.9.19. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```

## How to run?

```bash
conda create -p env python=3.9 -y
```

```bash
conda activate ./env
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

### Mlflow dagshub connection uri

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/jcole313/project.mlflow \
MLFLOW_TRACKING_USERNAME=jcole313 \
MLFLOW_TRACKING_PASSWORD=71368345455e3aa4cabbe321bbd6c4405a0db448 \
python script.py
```


### RUN from bash terminal

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/jcole313/project.mlflow

export MLFLOW_TRACKING_USERNAME=jcole313

export MLFLOW_TRACKING_PASSWORD=71368345455e3aa4cabbe321bbd6c4405a0db448

```



### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag