import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def find_data_frequency(df):
    df["Milliseconds"] = df["Milliseconds"] / 1e3
    timestaps = df["Milliseconds"].values
    dt = timestaps[1:] - timestaps[:-1]
    return 1 / dt.mean()

def find_variance(df):
    return df.var()

def find_data_mean_variance(data):
    mean = np.mean(data)
    variance = np.var(data)
    return mean, variance

###############################################################################

# Read data from csv file
df_acc = pd.read_csv('imu_stationary_oppo/Accelerometer.csv')

# Accelerometer data
timestaps_acc = df_acc["Milliseconds"].values / 1e3
acc_x = df_acc["X"].values
acc_y = df_acc["Y"].values
acc_z = df_acc["Z"].values #- 9.81

print("Accelerometer data frequency: ", find_data_frequency(df_acc))

acc_var = find_variance(df_acc)
print("Accelerometer data variance: \n", acc_var)

print("Accelerometer X data mean and variance: \n", find_data_mean_variance(acc_x))
print("Accelerometer Y data mean and variance: \n", find_data_mean_variance(acc_y))
print("Accelerometer Z data mean and variance: \n", find_data_mean_variance(acc_z))

################################################################################

## Gyro data
df_gyro = pd.read_csv('imu_stationary_oppo/Gyroscope.csv')
timestaps_gyro = df_gyro["Milliseconds"].values / 1e3
gyro_x = df_gyro["X"].values
gyro_y = df_gyro["Y"].values
gyro_z = df_gyro["Z"].values

print("Gyro data frequency: ", find_data_frequency(df_gyro))

gyro_var = find_variance(df_gyro)
print("Gyro data variance: \n", gyro_var)

print("Gyro X data mean and variance: \n", find_data_mean_variance(gyro_x))
print("Gyro Y data mean and variance: \n", find_data_mean_variance(gyro_y))
print("Gyro Z data mean and variance: \n", find_data_mean_variance(gyro_z))
