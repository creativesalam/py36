import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

Nsteps, Nwalkers = 100, 250
t = np.arange(Nsteps)

# an (Nsteps x Nwalkers) array of random walk steps
S1 = 0.002 + 0.01 * np.random.randn(Nsteps, Nwalkers)
S2 = 0.004 + 0.02 * np.random.randn(Nsteps, Nwalkers)

# an (Nsteps x Nwalkers) array of random walker positions
X1 = S1.cumsum(axis=0)

X2 = S2.cumsum(axis=0)


# Nsteps length arrays empirical means and standard deviations of both
# populations over time
mu1 = X1.mean(axis=1)
sigma1 = X1.std(axis=1)
mu2 = X2.mean(axis=1)
sigma2 = X2.std(axis=1)

# plot it!
fig, ax = plt.subplots(1)
ax.plot(t, mu1, lw=2, label="mean population 1", color="blue")
ax.plot(t, mu2, lw=2, label="mean population 2", color="yellow")
ax.fill_between(t, mu1 + sigma1, mu1 - sigma1, facecolor="blue", alpha=0.5)
ax.fill_between(t, mu2 + sigma2, mu2 - sigma2, facecolor="yellow", alpha=0.5)
ax.set_title(r"random walkers empirical $\mu$ and $\pm \sigma$ interval")
ax.legend(loc="upper left")
ax.set_xlabel("num steps")
ax.set_ylabel("position")
ax.grid()
plt.savefig("destination_path.eps", format="eps", dpi=10000)


x = np.linspace(0, 30, 30)
y = np.sin(x / 6 * np.pi)
error = 0.5  # np.random.normal(0.1, 0.02, size=y.shape)
y += np.random.normal(0, 0.1, size=y.shape)

plt.plot(x, y, "k-")
plt.fill_between(x, y - error, y + error, alpha=0.7)
plt.savefig("destination_path.svg", format="svg", dpi=1200)



