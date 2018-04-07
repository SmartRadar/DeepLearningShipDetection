# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input
from keras.optimizers import SGD
from keras import metrics


def build_CNN(learning_rate, decay_rate, momentum_value):
    #Build the CNN model by modifying VGGNet to fit the image size
    model = Sequential()
    
    model.add(Conv2D(64, (3, 3), activation='relu', padding = 'same', input_shape = (80, 80, 3)))
    model.add(Conv2D(64, (3, 3), activation='relu', padding = 'same'))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Conv2D(128, (3, 3), activation='relu', padding = 'same'))
    model.add(Conv2D(128, (3, 3), activation='relu', padding = 'same'))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Conv2D(256, (3, 3), activation='relu', padding = 'same'))
    model.add(Conv2D(256, (3, 3), activation='relu', padding = 'same'))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Conv2D(512, (3, 3), activation='relu', padding = 'same'))
    model.add(Conv2D(512, (3, 3), activation='relu', padding = 'same'))
    model.add(Conv2D(512, (3, 3), activation='relu', padding = 'same'))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Flatten())
    model.add(Dense(1, activation='sigmoid'))
    
    #Set up the input size
    img_input = Input(shape=(80, 80, 3))
    output = model(img_input)
    
    #Set up optimizer along with the loss function
    sgd = SGD(lr = learning_rate, decay = decay_rate, momentum = momentum_value, nesterov = True)
    model.compile(loss = 'binary_crossentropy', optimizer = sgd, metrics=[metrics.binary_accuracy])
    
    return model
    
def train_CNN(model, data, labels, batch, epoch_size):
    
    model.fit(data, labels, batch_size=batch, epochs=epoch_size)
    
    return model

def test_CNN(model, data, labels, batch):
    
    print(model.evaluate(data, labels, batch_size=batch))