import random
import csv
import numpy as np

num = 100
filenames = []
filenames = np.arange(0, num, 1)

random.shuffle(filenames)

train_filenames = filenames[:int(num * 0.85)]
valid_filenames = filenames[int(num * 0.85):int(num * 0.9)]
test_filenames = filenames[int(num * 0.9):]

train_filenames = ','.join([str(filename) for filename in train_filenames])
valid_filenames = ','.join([str(filename) for filename in valid_filenames])
test_filenames = ','.join([str(filename) for filename in test_filenames])

with open('/home/yons/dataverse_files - 副本/datasets/filename1s.txt', 'w', newline='') as f:
    f.write(train_filenames + '\n')
    f.write(valid_filenames + '\n')
    f.write(test_filenames)
    
