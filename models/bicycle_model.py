import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 2.5  # wheelbase in meters
dt = 0.1  # time step (s)
T = 10   # total simulation time (s)

# Initial state [x, y, theta]
state = np.array([0.0, 0.0, 0.0])

# Constant inputs
v = 2.0              # velocity in m/s
delta = np.radians(20)  # steering angle in radians

# History for plotting
x_hist, y_hist, theta_hist = [], [], []

def bicycle_model(state, v, delta, L):
    x, y, theta = state
    dx = v * np.cos(theta)
    dy = v * np.sin(theta)
    dtheta = v / L * np.tan(delta)
    return np.array([dx, dy, dtheta])

# Simulation loop
for t in np.arange(0, T, dt):
    state += bicycle_model(state, v, delta, L) * dt
    x_hist.append(state[0])
    y_hist.append(state[1])
    theta_hist.append(state[2])

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x_hist, y_hist, label="Vehicle Path")
plt.quiver(x_hist[::10], y_hist[::10], 
           np.cos(theta_hist[::10]), np.sin(theta_hist[::10]),
           scale=10, width=0.005, color='red', label='Heading')
plt.title("Bicycle Model Trajectory with Time-Invarient Inputs")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()