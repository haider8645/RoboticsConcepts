import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 2.5   # wheelbase in meters
dt = 0.1  # time step
T = 20    # total simulation time (s)
time = np.arange(0, T, dt)

# Initial state [x, y, theta]
state = np.array([0.0, 0.0, 0.0])

# History for plotting
x_hist, y_hist, theta_hist = [], [], []

def bicycle_model(state, v, delta, L):
    x, y, theta = state
    dx = v * np.cos(theta)
    dy = v * np.sin(theta)
    dtheta = v / L * np.tan(delta)
    return np.array([dx, dy, dtheta])

# Define control inputs as functions of time
def velocity(t):
    # Speed profile: accelerate, then cruise, then decelerate
    if t < 5:
        return 0.5 * t
    elif t < 15:
        return 2.5
    else:
        return max(2.5 - 0.5 * (t - 15), 0)

def steering_angle(t):
    # Steering: S-curve turning left then right
    return np.radians(15 * np.sin(0.3 * t))

# Simulation loop
for t in time:
    v = velocity(t)
    delta = steering_angle(t)
    state += bicycle_model(state, v, delta, L) * dt
    x_hist.append(state[0])
    y_hist.append(state[1])
    theta_hist.append(state[2])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_hist, y_hist, label="Vehicle Path")
plt.quiver(x_hist[::10], y_hist[::10],
           np.cos(theta_hist[::10]), np.sin(theta_hist[::10]),
           scale=10, width=0.005, color='red', label='Heading')
plt.title("Bicycle Model with Time-Varying Inputs")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
