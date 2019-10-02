## CNN.py

import numpy as np
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from config import *

# get data
X = np.zeros(1) # final: np.load('path/to/saved np array')
y = np.zeros(1)

# normalize
# define model
model = Sequential()

# first convolutional layer
# Conv2D( number_of_filters, kernal_size, input_shape(just for the input conv layer))
model.add(Conv2D(CNN_N_FILTERS, CNN_KERNEL_SIZE, input_shape = X.shape[1:]))
# layer activaion function
model.add(Activation(CNN_ACTIVATION_FUNCTION))
# layer pooling
model.add(MaxPooling2D(pool_size = CNN_POOL_SIZE))

# second layer
model.add(Conv2D(CNN_N_FILTERS, CNN_KERNEL_SIZE))
model.add(Activation(CNN_CONV_ACTIVATION_FUNCTION))
model.add(MaxPooling2D(pool_size = CNN_POOL_SIZE))

# dense layer on flattened data, 64 nodes
model.add(Flatten())
model.add(Dense(CNN_DENSE_NODE_COUNT))

# output layer
model.add(Dense(CNN_OUTPUT_DENSE_NODE_COUNT))
model.add(Activation(CNN_OUTPUT_ACTIVATION_FUNCTION))

# prepare for training
model.compile(loss = CNN_LOSS_FUNCTION, 
              optimizer = CNN_OPTIMIZER, 
              metrics = CNN_METRICS)

# fit
model.fit(X, y, batch_size = CNN_BATCH_SIZE, epochs = CNN_EPOCHS, validation_split = CNN_VALIDATION_SPLIT)

# summary
model.summary()

# save model
model.save('cnn.model')




