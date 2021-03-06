import tensorflow as tf
import time

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.reshape([x_train.shape[0], -1])
x_train = x_train.astype('float32') / 255
y_train = tf.keras.utils.to_categorical(y_train, num_classes=10)

x_test = x_test.reshape([x_test.shape[0], -1])
x_test = x_test.astype('float32') / 255
y_test = tf.keras.utils.to_categorical(y_test, num_classes=10)

batch_size = 128
epochs = 20
learning_rate = 0.5

# input place holders
X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 10])

# weights & bias for perceptron
W = tf.Variable(tf.random_uniform([784, 10], minval=-0.01, maxval=0.01))
b = tf.Variable(tf.zeros([10]))

hypothesis = tf.nn.sigmoid(tf.matmul(X, W) + b)

# define cost & optimizer
cost = tf.reduce_mean((hypothesis - Y) * (hypothesis - Y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
train = optimizer.minimize(cost)

accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1)), tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    start_time = time.time()

    for step in range(epochs):        
        score = [0, 0]
        loss = [0, 0]

        for i in range(0, x_train.shape[0], batch_size):
            size = batch_size if i + batch_size <= x_train.shape[0] else x_train.shape[0] - i
            
            c, a, _ = sess.run([cost, accuracy, train], feed_dict={X: x_train[i:i+size], Y: y_train[i:i+size]})
            loss[0] += c * size
            score[0] += a * size

        for i in range(0, x_test.shape[0], batch_size):
            size = batch_size if i + batch_size <= x_test.shape[0] else x_test.shape[0] - i
            
            c, a = sess.run([cost, accuracy], feed_dict={X: x_test[i:i+size], Y: y_test[i:i+size]})
            loss[1] += c * size
            score[1] += a * size
            
        print('loss: {:.4f} / {:.4f}\taccuracy: {:.4f} / {:.4f}\tstep {}  {:.2f} sec'.format(loss[0] / x_train.shape[0], loss[1] / x_test.shape[0], score[0] / x_train.shape[0], score[1] / x_test.shape[0], step + 1, time.time() - start_time))
