# Raw IPython history dump (minimally edited)
# 
# This is how ths history dump was produced, read %history? for more info.
# In [102]: %history ~2/
#
#
# Before the lecture
data = np.loadtxt("OshawaWeather2016.csv", skiprows=1, delimiter=',')
a = arange(11, 15)
a
a + array([[0,10]]).transpose()
b = a + array([[0,10]]).transpose()

# Lecture started
a
a > 12
a % 2 == 1
a >  13
(a >  13) + 0
z = a >  13
y = a <14
np.and(x, y)  # There is no "and", see np.logical_and below, or use x * y instead and ~x for logical not.
np.and(z, y)
np
np.logical_and(y, z)
np.logical_and(y, z)
y
z
y + z
y * z
y
idx = array(([1, 3][2,3]])
idx = array([[1, 3][2,3]])
idx = array([[1, 3], [2,3]])
idx
a[idx]
idx
a[idx]
6*7

# iPython restarted

import numpy as np
import matplotlib.pyplot as plt
plot(range(10))
ls
data = np.loadtxt("OshawaWeather2016.csv", skiprows=1, delimiter=',')
data
data.size
data.shape

data[ 1, 0]
clf()
data
day = data[ :,0 ]
day
day.shape
tmax = data[ :,1 ]
tmax.shape
tmax
tmax[:10]
plot(day, maxt)
plot(day, tmax)
plot(day, tmax + 10)
plt.clf()
clf()
plot(day, data[:, 2])
plot(day, data[:, 1])
figure()
clf()
plot(day, data[:, 1:4])
plot(day , tmax[:-1])
data
data + 5
data + arange(3)
data.shape
data + arange(5)
temps = data[:, 1:4]
temps
temps + array([1.2, 0.8, 1.1])
clf()
plt.scatter(day, tmax)
%run -i w2.py
a
b
clf()
plt.scatter(a, 1/a)
plt.scatter(a, 1/a, s=a*100)
plt.scatter(a, 1/a, s=(1-7)*100)
clf()
plt.scatter(a, 1/a, s=(1-7)*100)
plt.scatter(a, 1/a, s=(1-7)*100))
plt.scatter(a, 1/a, s=(a-7)*100)
plt.scatter(a, 1/a, s=(a-5)*100)
plt.scatter(a, 1/a, s=100)
clf()
plt.scatter(a, 1/a, s=(a-7)*100))
plt.scatter(a, 1/a, s=(a-7)*100)

a = arange(1, 6)
clf()
plt.scatter(a, 1/a, s=a*100)
b
b.sum()
a
a.sum()
np.sum(a)
np.sum([1, 2, 4])
np.sum?
data
data.sum()
data.max()
data.max(axis=0)
data.max(axis=1)
data.std(axis=1)
data.mean(axis=0)

a[~z]
%hist
