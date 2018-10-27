import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('mnist/', one_hot=True)



sess = tf.InteractiveSession()

mb_size = 128

input_size  = 784
hidden_size = 30
output_size = 784
drop_prob = 0.9

def sample():
    return np.random.uniform(-1., 1., size=[hidden_size])
X = tf.placeholder(tf.float32,shape=[None,input_size])

W1 = tf.Variable(tf.random_normal([input_size,hidden_size]))
b1 = tf.Variable(tf.random_normal([hidden_size]))

W2 = tf.Variable(tf.random_normal([hidden_size,output_size]))
b2 = tf.Variable(tf.random_normal([output_size]))

H = tf.nn.relu(tf.matmul(X,W1)+b1)
H -= sample()
H += sample()
O = tf.matmul(H,W2)+b2
O = tf.nn.sigmoid(O)
#loss = tf.reduce_sum(tf.nn.sigmoid_cross_entropy_with_logits(labels=X,logits=O))
loss1 = tf.reduce_sum(tf.square(X-O))

H1 = tf.nn.relu(tf.matmul(O,W1)+b1)
H1 -= sample()
H1 += sample()
O1 = tf.matmul(H,W2)+b2
O1 = tf.nn.sigmoid(O1)
loss2 = tf.reduce_sum(tf.square(X-O1))
loss3 = tf.reduce_sum(tf.square(O-O1))
loss = loss1 + loss2 + loss3
train_step = tf.train.AdamOptimizer(0.01).minimize(loss,var_list=[W1,W2,b1,b2])
init_op = tf.global_variables_initializer()
sess.run(init_op)

if not os.path.exists('out_ua/'):
    os.makedirs('out_ua/')

def plot(samples):
    fig = plt.figure(figsize=(4, 4))
    gs = gridspec.GridSpec(4, 4)
    gs.update(wspace=0.05, hspace=0.05)

    for i, sample in enumerate(samples):  # [i,samples[i]] imax=16
        ax = plt.subplot(gs[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_aspect('equal')
        plt.imshow(sample.reshape(28, 28), cmap='Greys_r')

    return fig

i = 0
for it in range(100000):

    X_mb, _ = mnist.train.next_batch(mb_size)
    sess.run(train_step,feed_dict={X:X_mb})
    if it % 1000 is 0:
        out = sess.run(O,feed_dict={X:X_mb})
        cur_loss = sess.run(loss,feed_dict={X:X_mb,O:out})
        out = out[0:16]
        out[8:16] = X_mb[0:8]
        # print(type(out),type(X_mb))
        # print("out ",out[0])
        # print("X   ",X_mb[0])
        fig = plot(out)
        plt.savefig('out_ua/{}.png'.format(str(i).zfill(3)), bbox_inches='tight')
        i += 1
        plt.close(fig)
        print('Iter: {}'.format(it))
        print('loss: {:.4}'.format(cur_loss))
        print()








