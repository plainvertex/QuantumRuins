import numpy as np
import matplotlib.pyplot as plt
from core.utils import set_chinese_font

# -------------------------------
# 参数（你可以随便改，只要保持 m/(2ħt) 这个系数的数量级合理）
# -------------------------------
m = 1.0
hbar = 1.0
t = 1.0
x_t = 0.0

# 选择一段 x 区间（连续）
x = np.linspace(-2.0, 2.0, 800)

# 相位函数 phi(x)
phi = m * (x_t - x)**2 / (2.0 * hbar * t)

# 映射到单位圆上的复数 z(x) = e^{i phi(x)}
z = np.exp(1j * phi)

# 选两个“相邻的 x 点”来强调“相邻位置”
idx0 = 360
idx1 = idx0 + 1

z0 = z[idx0]
z1 = z[idx1]

# -------------------------------
# 画图：单位圆 + 连续轨迹 + 相邻点高亮
# -------------------------------
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-1.25, 1.25)
ax.set_ylim(-1.25, 1.25)
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)
ax.set_xlabel("Re")
ax.set_ylabel("Im")
ax.grid(True, linewidth=0.5)

# 单位圆
tt = np.linspace(0, 2*np.pi, 400)
ax.plot(np.cos(tt), np.sin(tt), linewidth=1)

# 连续轨迹：z(x) 在单位圆上“滑动”的路径
ax.plot(z.real, z.imag, linewidth=2)

# 高亮两个相邻点
ax.scatter([z0.real, z1.real], [z0.imag, z1.imag], s=60, zorder=5)

# 从原点指向这两个点的箭头（更直观：它们都是单位向量）
ax.annotate("", xy=(z0.real, z0.imag), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1.5))
ax.annotate("", xy=(z1.real, z1.imag), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1.5))

# 标注：相邻 x 对应相邻相位点
ax.text(z0.real*1.08, z0.imag*1.08, r"$x$", ha="center", va="center")
ax.text(z1.real*1.08, z1.imag*1.08, r"$x+\Delta x$", ha="center", va="center")

title = "相位连续变化：相邻 x → 单位圆上相邻位置"
ax.set_title(title)

plt.show()
