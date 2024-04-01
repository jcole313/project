# Chest-Disease-Classification-from-Chest-CT-Scan-Image

 - [Data link](https://drive.google.com/file/d/1g8HvYzGfJm6Y5nJ-tEgs98a09hSXHRvf/view?usp=sharing)

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline 
7. Update the main.py
8. Update the dvc.yaml 



## Live matarials docs

[link](https://docs.google.com/document/d/1UFiHnyKRqgx8Lodsvdzu58LbVjdWHNf-uab2WmhE0A4/edit?usp=sharing)


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
conda activate env
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