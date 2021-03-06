import keras
import keras.optimizers
from keras.datasets import mnist
from keras.initializers import RandomUniform
from keras.layers import Dense, Flatten
from keras.layers import Conv2D
from keras.models import Sequential
from keras.optimizers import SGD

batch_size = 128
epochs = 30
num_classes = 10

# input image dimensions
img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(24,
                 activation='relu',                 
                 bias_initializer='zeros',
                 kernel_initializer=RandomUniform(minval=-0.1, maxval=0.1),
                 kernel_size=(5, 5),
                 strides=(2, 2),
                 input_shape=(img_rows, img_cols, 1)))
model.add(Flatten())
model.add(Dense(512,
                activation='relu',
                kernel_initializer=RandomUniform(minval=-0.01, maxval=0.01),
                bias_initializer='zeros'))
model.add(Dense(num_classes,
                activation='softmax',
                kernel_initializer=RandomUniform(minval=-0.01, maxval=0.01),
                bias_initializer='zeros'))
model.summary()
model.compile(loss='categorical_crossentropy',
              optimizer=SGD(lr=0.1, momentum=0.9, nesterov=True),
              metrics=['accuracy'])

history = model.fit(x_train,
                    y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    shuffle=False,
                    validation_data=(x_test, y_test))
