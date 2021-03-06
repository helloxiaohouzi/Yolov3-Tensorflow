#coding=utf-8

from __future__ import print_function
from __future__ import division

import numpy as np
import tensorflow as tf
import os
from yolov3 import yolov3_body
from utils.load_pretrained_weights import load_weights
import config
#from yolovv2 import yolo_inference

weight_path = config._coco_c_weights
saved_path = os.path.join(config._coco_tf_weights, 'yolov3.ckpt')

input_size = 416
num_classes = 80

with tf.Session() as sess:
    inputs = tf.placeholder(tf.float32, [1, input_size, input_size, 3])

    with tf.variable_scope('yolov3'):

        feats = yolov3_body(inputs, num_classes)
    #    feats = yolo_inference(inputs, 3, 80)

    saver = tf.train.Saver(var_list=tf.global_variables(scope='yolov3'))
    load_ops = load_weights(tf.global_variables(scope='yolov3'), weight_path)

    sess.run(load_ops)

    saver.save(sess, save_path=saved_path)

    print('Tensorflow model checkpoint has been to saved to {}'.format(saved_path))

