import numpy as np
import matplotlib.pyplot as plt
import core.utils
# ---- parameters ----
m = 1.0
hbar = 1.0
t = 0.15
x_t = 0.0
sigma = 1.0

x = np.linspace(-sigma, sigma, 2000)

# phase and derivative
phi = m * (x_t - x)**2 / (2*hbar*t)
dphi = (m/(hbar*t)) * (x - x_t)          # phi'(x)
abs_dphi = np.abs(dphi)                   # |phi'(x)|

# stationary point
x_stat = x_t
phi_stat = m * (x_t - x_stat)**2 / (2*hbar*t)

# ---- plot with two y-axes ----
fig, ax1 = plt.subplots(figsize=(9, 5))

ax1.set_xlabel("$x_t-x$")
ax1.set_ylabel(r"$\phi(x)$")
ax1.plot(x, phi, linewidth=2, label=r"$\phi(x)$")
ax1.grid(True, linewidth=0.5)

# mark stationary point (where |phi'| is minimal)
ax1.axvline(x_stat, linestyle="--", linewidth=1)
ax1.scatter([x_stat], [phi_stat], zorder=5)
ax1.text(
    x_stat + 0.03,
    phi_stat + 0.05*(phi.max()-phi.min()),
    r"$|\phi'(x)|$ minimal at $x=x_t$",
    ha="left", va="bottom"
)

ax2 = ax1.twinx()
ax2.set_ylabel(r"$|\phi'(x)|$")
ax2.plot(x, abs_dphi, linewidth=2, linestyle="--", label=r"$|\phi'(x)|$")

# combine legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

ax1.set_title(r"相位函数与相位变化速率: $\phi(x)$ and $|\phi'(x)|$")
plt.tight_layout()
plt.show()
