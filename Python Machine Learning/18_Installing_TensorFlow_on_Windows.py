# installing TensorFlow on using native PIP on windows
# python -m pip install --upgrade tensorflow

# test the installation
import tensorflow as tf
input_layer = "Mul"
output_layer = "final_result"
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello).decode())
