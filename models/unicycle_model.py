import numpy as np
import matplotlib.pyplot as plt

state = np.array([0.0, 0.0, 0.0])
T = 20
dt = 0.1
linear_vel = 0.5
angular_vel = 0.5

x_hist, y_hist, theta_hist = [], [], []

def unicycle_model(state, v, w):
    theta = state[2]
    x_dot = v * np.cos(theta)
    y_dot = v * np.sin(theta)
    t_dot = w
    return np.array([x_dot,y_dot,t_dot])

for t in np.arange(0,T,dt):
    state += unicycle_model(state,linear_vel,angular_vel) * dt
    x_hist.append(state[0])
    y_hist.append(state[1])
    theta_hist.append(state[2])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_hist, y_hist, label="Vehicle Path")
plt.quiver(x_hist[::10], y_hist[::10],
           np.cos(theta_hist[::10]), np.sin(theta_hist[::10]),
           scale=10, width=0.005, color='red', label='Heading')
plt.title("Unicycle Model with Time-Invarient Inputs")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()





