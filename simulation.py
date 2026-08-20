import numpy as np
import matplotlib.pyplot as plt

from noise_monitor import NoiseLevelMonitor


# Create monitor
monitor = NoiseLevelMonitor()

# Simulation parameters
time = np.arange(0, 20, 1)

# Simulated noise values in dB
noise_levels = np.array([
    35, 38, 42, 48, 55,
    61, 65, 72, 78, 83,
    88, 92, 87, 75, 68,
    58, 52, 45, 39, 35
])

# Display simulation results
print("===== Noise Level Monitor Simulation =====")

for t, db in zip(time, noise_levels):
    status = monitor.classify_noise(db)
    print(f"Time = {t:02d}s | Noise = {db:02d} dB | Status = {status}")

# Plot noise level
plt.figure(figsize=(10, 5))

plt.plot(
    time,
    noise_levels,
    marker="o",
    color="blue",
    linewidth=2,
    label="Noise Level"
)

# Reference levels
plt.axhline(40, color="green", linestyle="--", label="40 dB")
plt.axhline(60, color="orange", linestyle="--", label="60 dB")
plt.axhline(85, color="red", linestyle="--", label="85 dB Safe Limit")

plt.xlabel("Time (seconds)")
plt.ylabel("Noise Level (dB)")
plt.title("Noise Level Monitor Simulation")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.savefig("noise_simulation_output.png", dpi=300)

plt.show()
