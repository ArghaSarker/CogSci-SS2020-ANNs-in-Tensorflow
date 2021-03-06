# -*- coding: utf-8 -*-
"""Intro_Tensors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/anniewit/IANNWTF-2020/blob/main/week03/Intro_Tensors.ipynb
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
# NEXT LINE ONLY FOR COLAB!
# %tensorflow_version 2.x
import tensorflow as tf
import matplotlib.pyplot as plt
# COMMENT OUT THIS LINE FOR COLAB!
#%matplotlib notebook

print(tf.__version__)

"""## Understanding Tensors and Arrays."""

# A NumPy array is an arbitray dimensional matrix to store numbers in
arr = np.reshape(np.arange(9),(3,3))
print(arr)
print(arr.shape)
print("------------------")

# Access dimensions of the shape.
print(arr.shape[0])
print(arr.shape[-1])
print("------------------")

# Reshaping an array.
arr1 = np.reshape(arr, newshape=(9,1))
print(arr1)
arr2 = np.reshape(arr, newshape=(-1,1)) # The -1 makes numpy infer itself the missing dimension.
print(arr2)
print("------------------")

# Indexing allows you to access specific entries of an array.
print(arr[2,1]) # row 2 (third), column 1 (second).
print(arr[1,2]) # row 1 (second), column 2 (third).
print("------------------")

# Slicing allows you to retrieve parts of an array.
print(arr[:,1]) # All rows, collumn 1.
print(arr[0:2,:]) # Rows from 0 (include) to 2 (exclude), all columns.

# Thinking in matrices should be familiar from intro math course. 
# But the exact same things work in higher dimensions!
arr = np.reshape(np.arange(27), (3,3,3))
print(arr)
print(arr.shape)
print("------------------")

# Indexing.
print(arr[0,1,2])
print("------------------")

# Slicing.
print(arr[:,2,:])

# A tensor is kind of like a numpy array.
# Strictly spreaking tensors are operations. 
# You can't simply make a tensor out of a numpy array just like that...
tensor = tf.Tensor(arr)

# but luckily there is an in-built function for that
tensor = tf.convert_to_tensor(arr)
tensor

# But if you define a tensor as an operation, the tensor will store the corresponding result of this operation.
tensor = tf.multiply(42, arr)
print(arr)
print(tensor)

# If your variable is a tensor you can use all the normal math 
# operators as '+','-','*','/' and so on.
print(tensor/42)
print(tf.divide(tensor,42)) # That's the same thing.
print(tensor/42+tensor/42)

# You can also easily convert a tensor back to nunpy.
print(tensor.numpy())

"""## Useful Tensor Operations"""

# creating a 'scalar' (also called rank-0 tensor
#meaning a constant single valued tensor without any axes.
scalar = tf.constant(13)
print(scalar)

# you can also create tensor vectors from lists with one axia
vector = tf.constant([1.0, 2.0, 3.0])
print(vector)

# or matrices with two axes
matrix = tf.constant([[1,2],
                      [3,4],
                      [5,6]])
print(matrix)

# of course you can go on creating tensors with an arbitrary number of axes (dimensions)

"""Indexing of tensors works like standard Python an NumPy indexing rules. You can also use slicing.
You can also acces the shape of a tensor and reshape it similar to how you would do it in NumPy.
"""

a_tensor = tf.constant([[1,2],
                      [3,4],
                      [5,6]])

# accesing shape
print("Original shape of tensor:", a_tensor.shape)
# reshaping
reshaped_tensor = tf.reshape(a_tensor, [-1])
print("New shape:", reshaped_tensor.shape)
# you can also expand dimensions
print(tf.expand_dims(reshaped_tensor, -1).shape)

# more useful operations include stacking
x = tf.constant([1, 4])
y = tf.constant([2, 5])
z = tf.constant([3, 6])
print(tf.stack([x, y, z]))
print(tf.stack([x, y, z], axis=1))

# and a lot more...
# read the docs!
# https://www.tensorflow.org/api_docs/python/tf

# you can easily create tensors containing zeros in any shape
print("zeros")
print(tf.zeros(1))
print(tf.zeros((3,3)))

# or ones
print("\n ones")
print(tf.ones(1))
print(tf.ones((3,3)))

# or random values
print("\n random")
print(tf.random.normal((3,3), mean=0.0, stddev=1.0))
print(tf.random.uniform((3,3)))

"""## Tensorflow Variables

Now you have learned how to create constant valued tensors. But if you think ahead, what you will later want to do when implementing a neural network with tensorflow is defining tensors that will be changed a lot throughout running your program. Think back to how a neural network is trained. We first define its weights and then define how these weights are changed so that our network gets better at doing what it is supposed to do.

The recommended way to define model parameters, like for example the weights of a MLP, is to use the build in Tensorflow class tf. Variable.

A tf.Variable represents a tensor whose value can be changed by running operations on it, modifying its values. Higher level libraries like tf.keras use tf.Variable to store model parameters. 

Documentation: https://www.tensorflow.org/guide/variable
"""

# you can create Variables from tensors
my_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])
my_variable = tf.Variable(my_tensor)

# Variables can be all kinds of types, just like tensors
bool_variable = tf.Variable([False, False, False, True])
complex_variable = tf.Variable([5 + 4j, 6 + 1j])

a = tf.Variable([2.0, 3.0])
print(a)
# you can reassign values but it will stick to the original dtype, float32
a.assign([1, 2]) 
print(a)
# Not allowed as it resizes the variable: 
try:
  a.assign([1.0, 2.0, 3.0])
except Exception as e:
  print(f"{type(e).__name__}: {e}")

# you can also name them
# and you can decide wether your Variable needs or needs not to be trained
step_counter = tf.Variable(1, trainable=False, name="step_counter")
# of course, if we mean to define weights, such a Variable should be trainable
# this becomes important once we talk about automatic differentiation in trainable (Chapter on Gradient Tapes)

"""## All in all
So this was a basic introduction. The get away message is: You can do most of what you do in NumPy in Tensorflow as well. But as tensorflow is specialized in Deep Learning, you will also learn that it offers a lot more. So stay tuned and go on to the next chapters :)
"""