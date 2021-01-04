import numpy as np

# get the file from train

trainingData = np.loadtxt('optdigits.tra',dtype='int',delimiter=",")
rowData = trainingData[0,:]
print(rowData)
