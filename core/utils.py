"""
通用工具函数

提供项目中可复用的辅助函数。
"""

import numpy as np


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """
    将数组归一化到 [0, 1] 范围。

    Parameters
    ----------
    arr : np.ndarray
        输入数组

    Returns
    -------
    np.ndarray
        归一化后的数组
    """
    arr_min = arr.min()
    arr_max = arr.max()
    
    if arr_max - arr_min == 0:
        return np.zeros_like(arr)
    
    return (arr - arr_min) / (arr_max - arr_min)


def wavelength_to_color(wavelength: float) -> str:
    """
    将可见光波长（纳米）转换为近似的十六进制颜色。

    Parameters
    ----------
    wavelength : float
        波长值（380-780 nm 范围内）

    Returns
    -------
    str
        十六进制颜色代码
    """
    # 简化的波长到颜色映射
    if wavelength < 380:
        return "#7F00FF"  # 紫外（显示为紫色）
    elif wavelength < 450:
        return "#4B0082"  # 紫色
    elif wavelength < 495:
        return "#0000FF"  # 蓝色
    elif wavelength < 570:
        return "#00FF00"  # 绿色
    elif wavelength < 590:
        return "#FFFF00"  # 黄色
    elif wavelength < 620:
        return "#FF7F00"  # 橙色
    elif wavelength < 780:
        return "#FF0000"  # 红色
    else:
        return "#8B0000"  # 红外（显示为深红）
