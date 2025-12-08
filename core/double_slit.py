"""
双缝干涉物理计算内核

实现双缝干涉实验的强度分布计算，基于 Fraunhofer 衍射近似。
"""

import numpy as np


def compute_double_slit(
    wavelength: float,
    slit_distance: float,
    screen_distance: float,
    num_points: int = 2000,
) -> tuple[np.ndarray, np.ndarray]:
    """
    计算双缝干涉实验中屏幕上的光强分布。

    使用 Fraunhofer 衍射近似，计算两束相干光在屏幕上的干涉强度分布。
    
    物理模型说明：
    - 两个狭缝作为相干光源，发出同相位的光波
    - 光波到达屏幕上某点时，由于路程差产生相位差
    - 相位差导致干涉，形成明暗相间的条纹
    
    干涉强度公式（简化模型）：
        I(x) = cos²(π * d * x / (λ * L))
    
    其中：
        - d: 双缝间距
        - λ: 波长
        - L: 屏幕距离
        - x: 屏幕上的位置坐标

    Parameters
    ----------
    wavelength : float
        光的波长（单位：任意长度单位，需与其他参数一致）。
        典型值范围：0.3 - 1.0（可理解为微米量级）。
    slit_distance : float
        两条狭缝之间的距离（单位：与波长相同）。
        典型值范围：1.0 - 5.0。
    screen_distance : float
        狭缝到观察屏的距离（单位：与波长相同）。
        典型值范围：5.0 - 20.0。
    num_points : int, optional
        屏幕上采样点的数量，默认为 2000。
        更多的点数会产生更平滑的曲线。

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        返回一个元组 (x, intensity)：
        - x: 屏幕坐标数组，范围基于衍射角度自动计算
        - intensity: 归一化后的光强分布（0 到 1 之间）

    Examples
    --------
    >>> x, I = compute_double_slit(wavelength=0.5, slit_distance=2.0, screen_distance=10.0)
    >>> print(f"屏幕范围: [{x.min():.2f}, {x.max():.2f}]")
    >>> print(f"强度范围: [{I.min():.2f}, {I.max():.2f}]")
    """
    # 计算屏幕坐标范围
    # 使用足够大的范围以显示多个干涉条纹
    # 条纹间距约为 λL/d，我们显示约 10 个条纹
    fringe_spacing = wavelength * screen_distance / slit_distance
    x_range = 10 * fringe_spacing
    
    # 生成屏幕坐标数组
    x = np.linspace(-x_range, x_range, num_points)
    
    # 计算相位差
    # δ = 2π * d * sin(θ) / λ ≈ 2π * d * x / (λ * L) (小角度近似)
    phase_difference = np.pi * slit_distance * x / (wavelength * screen_distance)
    
    # 计算干涉强度（双缝干涉公式）
    # I = I₀ * cos²(δ/2) = I₀ * cos²(π * d * x / (λ * L))
    intensity = np.cos(phase_difference) ** 2
    
    # 强度已经自动归一化到 [0, 1] 范围（cos² 的值域）
    
    return x, intensity
