import pandas as pd
import matplotlib.pyplot as plt


def find_data_frequency(df):
    df["Milliseconds"] = df["Milliseconds"] / 1e3
    timestaps = df["Milliseconds"].values
    dt = timestaps[1:] - timestaps[:-1]
    return 1 / dt.mean()

###############################################################################

# Read data from csv file
df_acc = pd.read_csv('imu_stationary_oppo/Accelerometer.csv')

# Accelerometer data
timestaps_acc = df_acc["Milliseconds"].values / 1e3
acc_x = df_acc["X"].values
acc_y = df_acc["Y"].values
acc_z = df_acc["Z"].values - 9.81   # Gravity subtracted

print("Accelerometer data frequency: ", find_data_frequency(df_acc))

# Plot data
plt.figure(1)
plt.plot(timestaps_acc, acc_x, label="X")
plt.plot(timestaps_acc, acc_y, label="Y")
plt.plot(timestaps_acc, acc_z, label="Z")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s^2)")
plt.legend()
# plt.show()

################################################################################

## Gyro data
df_gyro = pd.read_csv('imu_stationary_oppo/Gyroscope.csv')
timestaps_gyro = df_gyro["Milliseconds"].values / 1e3
gyro_x = df_gyro["X"].values
gyro_y = df_gyro["Y"].values
gyro_z = df_gyro["Z"].values

# Plot data
plt.figure(2)
plt.plot(timestaps_gyro, gyro_x, label="X")
plt.plot(timestaps_gyro, gyro_y, label="Y")
plt.plot(timestaps_gyro, gyro_z, label="Z")
plt.xlabel("Time (s)")
plt.ylabel("Angular velocity (rad/s)")
plt.legend()
plt.show()

print("Gyro data frequency: ", find_data_frequency(df_gyro))
