from __future__ import absolute_import, division, print_function, unicode_literals

import os

import tensorflow as tf
from tensorflow import keras

print(tf.__version__)

mnist = tf.keras.datasets.mnist
def test_tensorboard():
  (x_train, y_train),(x_test, y_test) = mnist.load_data()
  x_train, x_test = x_train / 255.0, x_test / 255.0

  model = tf.keras.models.Sequential([
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(512, activation=tf.nn.relu),
	tf.keras.layers.Dropout(0.2),
	tf.keras.layers.Dense(10, activation=tf.nn.softmax)
  ])
  model.compile(optimizer='adam',
				loss='sparse_categorical_crossentropy',
				metrics=['accuracy'])
  
  checkpoint_path = "checkpoints/cp-{epoch:04d}.ckpt"
  print("path: %s" % checkpoint_path)
  checkpoint_dir = os.path.dirname(checkpoint_path)

  cp_callback = tf.keras.callbacks.ModelCheckpoint(
    checkpoint_path, verbose=1, save_weights_only=False,
    # Save weights, every epoch.
    period=1)

  #saver_callback = keras.callbacks.ModelCheckpoint(
	#'test/test_save.ckpt', verbose=1, save_weights_only=True, period=1)
  tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=checkpoint_dir, histogram_freq=10, profile_batch=3)

  model.fit(x_train, y_train, epochs=1000000, callbacks=[cp_callback,tensorboard_callback])
  model.evaluate(x_test, y_test)

test_tensorboard()
print("done")