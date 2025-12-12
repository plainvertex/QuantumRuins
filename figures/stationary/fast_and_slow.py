# 两张“可视化绕圈次数”的新图：
# 上：总绕行 0.03 圈（几乎不转）
# 下：先绕很多整圈 + 最后再转 0.03 圈
# 技巧：人为加入“极小的径向偏移”，把多圈“拉开”为螺旋线

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import numpy as np
import matplotlib.pyplot as plt
from core.utils import set_chinese_font

set_chinese_font()

# ---------- 公共设置 ----------
def setup(ax, title):
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.grid(True, linewidth=0.5)
    ax.set_title(title)

theta = np.linspace(0, 2*np.pi, 400)

fig, axes = plt.subplots(2, 1, figsize=(7, 12))

# ---------- 图 1：绕行 0.03 圈 ----------
turns_small = 0.03
phi1 = np.linspace(0, 2*np.pi*turns_small, 800)

# 基本单位圆
axes[0].plot(np.cos(theta), np.sin(theta), linewidth=1)

# 轨迹（几乎贴着单位圆）
z1 = np.exp(1j * phi1)
axes[0].plot(z1.real, z1.imag, linewidth=3)

# 起点 / 终点
axes[0].scatter([z1.real[0]], [z1.imag[0]], s=60)
axes[0].scatter([z1.real[-1]], [z1.imag[-1]], s=60)
axes[0].text(z1.real[0]*1.05, z1.imag[0]*1.05, "start")
axes[0].text(z1.real[-1]*1.05, z1.imag[-1]*1.05, "end")

setup(
    axes[0],
    "相位绕行 ≈ 0.03 圈（不足一整圈）"
)

# ---------- 图 2：多圈 + 最后 0.03 圈 ----------
full_turns = 3          # “很多圈”
tail_turns = 0.03
total_turns = full_turns + tail_turns

phi2 = np.linspace(0, 2*np.pi*total_turns, 6000)

# 人为加入极小径向偏移：螺旋（仅用于可视化）
epsilon = 0.08
r = 1.0 + epsilon * (phi2 / phi2.max())
z2 = r * np.exp(1j * phi2)

axes[1].plot(np.cos(theta), np.sin(theta), linewidth=1)

axes[1].plot(z2.real, z2.imag, linewidth=2)

# 标注“整圈区域”与“尾巴”
cut = int(len(phi2) * full_turns / total_turns)
axes[1].plot(
    z2.real[:cut], z2.imag[:cut],
    linewidth=2, alpha=0.5, label="多个整圈"
)
axes[1].plot(
    z2.real[cut:], z2.imag[cut:],
    linewidth=3, label="最后 0.03 圈（尾巴）"
)

# 起点 / 终点
axes[1].scatter([z2.real[0]], [z2.imag[0]], s=60)
axes[1].scatter([z2.real[-1]], [z2.imag[-1]], s=60)
axes[1].text(z2.real[0]*1.05, z2.imag[0]*1.05, "start")
axes[1].text(z2.real[-1]*1.05, z2.imag[-1]*1.05, "end")

axes[1].legend()

setup(
    axes[1],
    "多个整圈 + 最后 0.03 圈（以螺旋线可视化）"
)

plt.tight_layout()
plt.show()
