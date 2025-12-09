"""
高斯波包时间演化 - 核心计算模块

计算初始静止高斯波包随时间演化的概率密度。
给定 σ=1, m=1, ℏ=1 时的波函数表达式。
"""

import numpy as np
from numpy.typing import NDArray


def compute_probability_density(
    x: NDArray[np.floating],
    t: float,
) -> NDArray[np.floating]:
    """
    计算给定时刻的概率密度 |Ψ(x,t)|²

    波函数（概率振幅部分）：
    Ψ(x, t) = (2π)^{-1/4} (1 + it/2)^{-1/2} exp(-x²/(4(1 + t²/4)))

    参数:
        x: 空间坐标数组
        t: 时间

    返回:
        概率密度数组 |Ψ(x,t)|²
    """
    # 计算 |1 + it/2|² = 1 + t²/4
    norm_factor_squared = 1 + t**2 / 4

    # |(1 + it/2)^{-1/2}|² = (1 + t²/4)^{-1/2}
    prefactor = (2 * np.pi) ** (-0.5) * norm_factor_squared ** (-0.5)

    # exp(-x²/(4(1 + t²/4))) 的模平方就是它自身（因为是实数）
    # |exp(-x²/(4(1 + t²/4)))|² = exp(-x²/(2(1 + t²/4)))
    gaussian = np.exp(-x**2 / (2 * norm_factor_squared))

    return prefactor * gaussian


def compute_wavepacket_evolution(
    t_values: list[float],
    x_min: float = -10.0,
    x_max: float = 10.0,
    num_points: int = 500,
) -> tuple[NDArray[np.floating], dict[float, NDArray[np.floating]]]:
    """
    计算多个时刻的概率密度分布

    参数:
        t_values: 时间点列表
        x_min: x 轴最小值
        x_max: x 轴最大值
        num_points: 采样点数

    返回:
        (x数组, {时间: 概率密度数组} 字典)
    """
    x = np.linspace(x_min, x_max, num_points)
    densities = {}

    for t in t_values:
        densities[t] = compute_probability_density(x, t)

    return x, densities
