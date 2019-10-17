## CNN.py
import numpy as np
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from config import *


class CNN():
	def __init__(self):
		self.model = None
# def process_data():
	# get data
	# X = np.zeros((1,)) # final: np.load('path/to/saved np array')
	# y = np.zeros((1,))
	# normalize

	# return X, y

def create_model():
	# test
	# X = np.zeros((1,)) # final: np.load('path/to/saved np array')
	# y = np.zeros((1,))

	# define model
	self.model = Sequential()

	# first convolutional layer
	# Conv2D( number_of_filters, kernal_size, input_shape(just for the input conv layer))
	self.model.add(Conv2D(CNN_N_FILTERS,
		             CNN_KERNEL_SIZE,
		             input_shape = X.shape[1:]))
	# layer activaion function
	self.model.add(Activation(CNN_ACTIVATION_FUNCTION))
	# layer pooling
	self.model.add(MaxPooling2D(pool_size = CNN_POOL_SIZE))

	# second layer
	model.add(Conv2D(CNN_N_FILTERS,
		             CNN_KERNEL_SIZE))
	self.model.add(Activation(CNN_CONV_ACTIVATION_FUNCTION))
	self.model.add(MaxPooling2D(pool_size = CNN_POOL_SIZE))

	# dense layer on flattened data, 64 nodes
	self.model.add(Flatten())
	self.model.add(Dense(CNN_DENSE_NODE_COUNT))

	# output layer
	self.model.add(Dense(CNN_OUTPUT_DENSE_NODE_COUNT))
	self.model.add(Activation(CNN_OUTPUT_ACTIVATION_FUNCTION))

	# prepare for training
	self.model.compile(loss      = CNN_LOSS_FUNCTION, 
	              optimizer = CNN_OPTIMIZER, 
	              metrics   = CNN_METRICS)
	

	def train():
		# fit
		self.model.fit(X, y, batch_size = CNN_BATCH_SIZE, epochs = CNN_EPOCHS, validation_split = CNN_VALIDATION_SPLIT)

	def summary():
		# summary
		self.model.summary()

	def save_model():
		# save model
		self.model.save('cnn.model')
