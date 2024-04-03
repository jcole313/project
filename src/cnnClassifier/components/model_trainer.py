import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from cnnClassifier.entity.config_entity import TrainingConfig
from pathlib import Path
import shutil
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import ModelCheckpoint,EarlyStopping
from tensorflow.keras.applications import resnet

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    def train_valid_generator(self):
        
        datagenerator_kwargs = dict(
            dtype='float32',
            preprocessing_function=resnet.preprocess_input
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            class_mode = 'categorical'
        )

        valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagen.flow_from_directory(
            directory=self.config.validation_data,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
                **datagenerator_kwargs
            )
            
        self.train_generator = train_datagen.flow_from_directory(
            directory=self.config.training_data,
            **dataflow_kwargs
        )

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        
        destination_dir = path.parent.parent.parent / "model"
        if not destination_dir.exists():
            destination_dir.mkdir(parents=True)

        # Copy the file to the destination directory
        destination_file = destination_dir / "model.h5"
        shutil.copyfile(path, destination_file)


    
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.checkpointer = ModelCheckpoint(filepath=str(self.config.trained_model_path),
                            monitor='val_loss', verbose = 1,
                            save_best_only=True)
        self.early_stopping = EarlyStopping(verbose=1, patience=15)
        
        self.model.fit(self.train_generator,
                    steps_per_epoch = self.steps_per_epoch,
                    epochs = self.config.params_epochs,
                    verbose = 1,
                    validation_data = self.valid_generator,
                    callbacks = [self.checkpointer, self.early_stopping])

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
