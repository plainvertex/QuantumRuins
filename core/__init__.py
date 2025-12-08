"""
Quantum Playground - 物理计算核心模块

此模块包含各种量子物理实验的计算内核，
所有计算函数独立于 UI，仅使用 numpy 进行数值计算。
"""

from .double_slit import compute_double_slit

__all__ = ["compute_double_slit"]
