# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
import numpy as np
X = np.random.normal(0, 0.1, size=(1000,1000))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')
'''
X =
 [[ 0.03971632  0.1091806   0.02087538 ... -0.04724034 -0.02313917
  -0.04170723]
 [-0.05683428  0.13267907  0.0716697  ...  0.0249755   0.00635562
  -0.03324387]
 [ 0.11083923  0.02097163  0.0650704  ...  0.05223163  0.01660092
  -0.0963056 ]
 ...
 [ 0.0080442  -0.29195767  0.09447347 ... -0.00945001  0.02444364
   0.06078854]
 [-0.08511726  0.0516405  -0.07531466 ... -0.08881466 -0.15460645
  -0.14352218]
 [-0.02907349  0.06337012 -0.01998184 ...  0.13549456  0.14170456
  -0.07637288]]

X has dimensions: (1000, 1000)
X is an object of type: <class 'numpy.ndarray'>
The elements in X are of type: float64
The elements in X have a mean of: -5.992226013045382e-05
The maximum value in X is: 0.457953781722654
The minimum value in X is: -0.503799689755834
X has 500798 negative numbers
X has 499202 positive numbers
'''