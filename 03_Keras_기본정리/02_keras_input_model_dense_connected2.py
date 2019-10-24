# -*- coding: utf-8 -*-
"""02_keras-input-model-dense-connected2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LW-91W72aa5O3gWicsowg5BMZTggbrGK
"""

#https://keras.io/getting-started/functional-api-guide/
#First example: a densely-connected network

from keras.layers import Input, Dense
from keras.models import Model
from keras.layers import TimeDistributed

# Input tensor for sequences of 20 timesteps,
# each containing a 784-dimensional vector
input_sequences = Input(shape=(20, 784))
print(input_sequences.shape)
#(?, 20, 784)

# a layer instance is callable on a tensor, and returns a tensor
output_1 = Dense(64, activation='relu')(input_sequences)
print(output_1.shape)
#

output_2 = Dense(64, activation='relu')(output_1)
print(output_2.shape)

predictions = Dense(10, activation='softmax')(output_2)
print(predictions.shape)
#(?, 20, 784)

# This creates a model that includes
# the Input layer and three Dense layers
model = Model(inputs=input_sequences, outputs=predictions)

# This applies our previous model to every timestep in the input sequences.
# the output of the previous model was a 10-way softmax,
# so the output of the layer below will be a sequence of 20 vectors of size 10.
processed_sequences = TimeDistributed(model)(input_sequences)
print(processed_sequences.shape)
#(?, 20, 784)

model.summary()

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

import numpy as np

data = np.array([[range(784) for _ in range(20)]]) 
print(data)
print(data.shape) #(1, 20, 784)
labels = np.array([[range(10) for _ in range(20)]])
print(labels.shape) #(1, 20, 10)
print(labels)

model.fit(data, labels)  # starts training