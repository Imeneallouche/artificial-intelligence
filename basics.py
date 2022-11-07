import numpy
from scipy import stats
import sys  # output the drawing
import matplotlib


array = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39,
         80, 82, 32, 2, 8, 6, 25, 36, 27, 61, 31]


# the mean the median and the mode
print("mean of array: ", numpy.mean(array))
print("median of array: ", numpy.median(array))
# mode() returns a ModeResult object that contains the mode number, and how many times the mode number.
print("mode of array: ", stats.mode(array))

# standard Deviation (sigma(X))
print("the standard Deviation: ", numpy.std(array))

# vriance(V(X) = sigma(X)²)
print("variance: ", numpy.var(array))


# BIG DATA creation with  NumPy
BigData = numpy.random.uniform(0, 5, 250)  # 250 elems between 0 and 5
print(BigData)

# Data Vizualisation using matplotlib
# usign histograms
