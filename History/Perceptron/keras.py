import keras
from keras.datasets import mnist
from keras.initializers import RandomUniform
from keras.layers import Dense
from keras.models import Sequential
from keras.optimizers import SGD

epochs = 20
num_classes = 10

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Dense(num_classes,
                activation='sigmoid',
                input_shape=(784,),
                kernel_initializer=RandomUniform(minval=-0.01, maxval=0.01, seed=None),
                bias_initializer='zeros'))
model.summary()
model.compile(loss='mean_squared_error',
              optimizer=SGD(lr=0.1),
              metrics=['accuracy'])

history = model.fit(x_train,
                    y_train,
                    batch_size=1,
                    epochs=epochs,
                    validation_data=(x_test, y_test))