# 教科书级“三联图”：相位分布 → 向量求和
# 从上到下：完全抵消 → 部分抵消 → 相干增强

import numpy as np
import matplotlib.pyplot as plt
from core.utils import set_chinese_font

# Initialize Chinese font support
set_chinese_font()

def draw_case(ax, angles, title):
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.5, 9)
    ax.set_ylim(-2, 2)
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title(title)
    ax.grid(True, linewidth=0.5)

    # 单位圆
    t = np.linspace(0, 2*np.pi, 400)
    ax.plot(np.cos(t), np.sin(t), linewidth=1)

    # 单位向量 e^{i phi}
    vectors = np.exp(1j * angles)
    sum_vec = np.sum(vectors)

    # 画出每一个单位向量（从原点）
    for v in vectors:
        ax.annotate(
            "",
            xy=(v.real, v.imag),
            xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1, alpha=0.6)
        )

    # 合矢量（从偏移点画出，避免遮挡）
    origin_shift = np.array([0, -0.6])
    ax.annotate(
        "",
        xy=(origin_shift[0] + sum_vec.real, origin_shift[1] + sum_vec.imag),
        xytext=(origin_shift[0], origin_shift[1]),
        arrowprops=dict(arrowstyle="->", linewidth=3)
    )

    ax.text(
        origin_shift[0] + sum_vec.real,
        origin_shift[1] + sum_vec.imag,
        rf"$\left|\sum e^{{i\phi}}\right| = {abs(sum_vec):.2f}$",
        fontsize=11,
        ha="left",
        va="bottom"
    )


# ---------- 三种相位分布 ----------

# 1. 均匀分布：完全抵消
angles_uniform = np.linspace(0, 2*np.pi, 8, endpoint=False)

# 2. 中等集中：部分抵消
angles_medium = np.linspace(-np.pi/4, np.pi/4, 8)

# 3. 高度集中：相干增强（π/6 内）
angles_clustered = np.linspace(-np.pi/12, np.pi/12, 8)


# ---------- 画三联图 ----------

fig, axes = plt.subplots(3, 1, figsize=(10, 12))

draw_case(
    axes[0],
    angles_uniform,
    "相位均匀分布（完全相互抵消）"
)

draw_case(
    axes[1],
    angles_medium,
    "相位部分对齐（部分抵消）"
)

draw_case(
    axes[2],
    angles_clustered,
    r"相位高度对齐（相干增强，π/6 内）"
)

plt.tight_layout()
plt.show()
