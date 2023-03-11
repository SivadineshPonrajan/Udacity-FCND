import numpy as np

gps_x_axis = np.loadtxt('config/log/Graph1.txt',delimiter=',',dtype='Float64',skiprows=1)[:,1]
acc_x_axis = np.loadtxt('config/log/Graph2.txt',delimiter=',',dtype='Float64',skiprows=1)[:,1]

print("gps_x_sd = ", np.std(gps_x_axis))
print("acc_x_sd = ", np.std(acc_x_axis))