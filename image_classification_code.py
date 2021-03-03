# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:11:36 2021

@author: Divy
"""

import os

import numpy as np

import tensorflow as tf
assert tf.__version__.startswith('2')

from tflite_model_maker import configs
from tflite_model_maker import ExportFormat
from tflite_model_maker import image_classifier
from tflite_model_maker import ImageClassifierDataLoader
from tflite_model_maker import model_spec

import matplotlib.pyplot as plt

# image_path = "Data"
image_path = "Downloads/Dataset"

data = ImageClassifierDataLoader.from_folder(image_path)
# train_data, rest_data = data.split(0.8)
# validation_data, test_data = rest_data.split(0.5)

#Show first 25 images with labels
# plt.figure(figsize=(10,10))
# for i, (image, label) in enumerate(data.gen_dataset().unbatch().take(25)):
#   plt.subplot(5,5,i+1)
#   plt.xticks([])
#   plt.yticks([])
#   plt.grid(False)
#   plt.imshow(image.numpy(), cmap=plt.cm.gray)
#   plt.xlabel(data.index_to_label[label.numpy()])
# plt.show()

# model = image_classifier.create(train_data, validation_data=validation_data)
# model.summary()

train_data, test_data = data.split(0.8)

#SINGLE MODEL
model = image_classifier.create(train_data,dropout_rate=0.1)

#Evaluating model
loss, accuracy = model.evaluate(test_data)

# #Export TFLite file
model.export(export_dir='.')

# #Export LABEL file
model.export(export_dir='.', export_format=ExportFormat.LABEL)


#Post Training optimization
config = configs.QuantizationConfig.create_full_integer_quantization(representative_data=test_data, is_integer_only=True)

#Exporting optimized model
model.export(export_dir='.', tflite_filename='model_quant.tflite', quantization_config=config)