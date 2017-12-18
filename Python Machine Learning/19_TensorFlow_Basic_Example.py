import tensorflow as tf

x1 = tf.constant(5)
x2 = tf.constant(6)

res = tf.multiply(x1,x2) # multiplies constants and an abstract tensor
print(res) # 'res' variable holds abstract tensor 

with tf.Session() as sess: # accessing the tensorflow session
    output = sess.run(res)
    # 'output' is a python variable that stores result of 'res' variable when run() in tensorflow session
    print(output)     