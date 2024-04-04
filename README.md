# Chest Disease Classification from Chest CT Scan Image

# Introduction

Chest CT scan images hold invaluable diagnostic potential in identifying various pulmonary conditions, including malignant tumors. Our project aims to streamline the classification process of these images into four distinct classes: 'adenocarcinoma', 'large cell carcinoma', 'normal', and 'squamous cell carcinoma'. Through the utilization of advanced techniques such as Deep Learning and Data Version Control (DVC), coupled with the robust ResNet50 architecture, I have developed an end-to-end pipeline that ensures efficient and accurate classification of chest CT scan images.

In addition to these methodologies, our project also integrates MLflow, a powerful machine learning lifecycle management tool. MLflow facilitates experiment tracking, model management, and reproducibility, allowing us to monitor and compare multiple models, hyperparameters, and experiments seamlessly. Through the synergy of DVC for data versioning and MLflow for model management, our project ensures transparency, reproducibility, and continuous improvement in the development and deployment of machine learning models.

## Tech Stack Used
1) Python
2) Flask
3) Deep Learning Algorithms
4) Data Version Control (DVC)
5) MLFlow

## Infrastructure
1) DockerHub
2) DagsHub
3) GitHub

## System Design
![image](./assets/SystemDesign.jpg)

## DagsHub Data Pipeline
![image](./assets/DVCPipeline.jpg)

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
#### Dataset Details<a id='dataset-details'></a>
<pre>
Dataset Name            : Chest CT-Scan images Dataset (Adenocarcinoma vs Large cell carcinoma vs Squamous cell carcinoma vs Normal)
Number of Class         : 4
Number/Size of Images   : Total      : 1000 (124 MB)
                          Training   : 700
                          Testing    : 200
                          Validation : 100 
                         
</pre>
## Results<a id='results-'></a>
We have achieved following results with ResNet50 model for detection of Adenocarcinoma,Large cell carcinoma, Squamous cell carcinoma and normal from Brain MRI images.

<pre>
<b> Performance Metrics </b>
Test Accuracy                                    : 89.52%
Test Loss                                        : 31.90%
Sensitivity (Glioma)                             : 100% 
Sensitivity (Meningioma)                         : 99% 
Sensitivity (Pituitary)                          : 100% 
Sensitivity (Normal)                             : 99% 
F1-score                                         : 99.00%
AUC                                              : 1.0
</pre>


## Installation
    
The Code is written in Python 3.9.19. If you don't have Python installed you can find it here. If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip.

## Run Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/jcole313/project.git
```
### Step 2- Create a conda environment after opening the repository
```bash
conda create -p env python=3.9 -y
```
```bash
conda activate env/
```
### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```
### Step 4 - Set Environment variables for MLFlow
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/jcole313/project.mlflow

export MLFLOW_TRACKING_USERNAME=jcole313

export MLFLOW_TRACKING_PASSWORD=71368345455e3aa4cabbe321bbd6c4405a0db448
```
### Step 5. Train application
```bash
python main.py
```
OR
```bash
http://localhost:8080/train
```
### Step 6 - Run the application server
```bash
python app.py
```
### Step 7 - Prediction application
```bash
http://localhost:8080/

```

## Mlflow dagshub connection Keys

```bash
MLFLOW_TRACKING_URI=https://dagshub.com/jcole313/project.mlflow \
MLFLOW_TRACKING_USERNAME=jcole313 \
MLFLOW_TRACKING_PASSWORD=71368345455e3aa4cabbe321bbd6c4405a0db448 \
python script.py
```

## Run DVC Pipeline
### Step 1 - Initialize dvc
```bash
dvc init
```
### Step 2 - Run DVC Pipeline
```bash
dvc repro
```
### Step 3 - See the Tree Structure of Pipeline
```bash
dvc dag
```