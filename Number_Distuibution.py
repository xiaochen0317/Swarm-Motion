import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab

filename = ['/home/yons/dataverse_files - 副本/datasets/position/data_' + str(i) + '.txt' for i in range(5000)]

num_size1 = []
for i in range(5000):
    data = np.loadtxt(filename[i], skiprows=1, delimiter=',')
    data = np.array(data[100])
    num_size1.append(data.shape[0] // 2)

num_size = np.array(num_size1)

plt.hist(num_size,
         bins=np.arange(num_size.min(), num_size.max(), 5),
         density=False,
         color='steelblue',
         rwidth=1,
         edgecolor='k')

# kde = mlab.GaussianKDE(num_size1)
# x = np.linspace(num_size.min(), num_size.max(), 1000)
# line, = plt.plot(x, kde(x), '#00008B', linewidth=5)
# plt.xlabel('Number of Agents')
# plt.ylabel('Samples')

plt.show()
