"""
Demos package - 量子物理交互演示模块

自动发现并加载所有 demo 模块。
每个 demo 文件必须：
1. 文件名以 NN_ 开头（NN 为两位数字，决定顺序）
2. 暴露 get_name() 函数返回中文名称
3. 暴露 show() 函数渲染页面
"""

import importlib
import re
from pathlib import Path
from typing import Callable

# Demo 信息类型: (slug, name, show_func)
DemoInfo = tuple[str, str, Callable[[], None]]


def discover_demos() -> list[DemoInfo]:
    """
    自动发现 demos 目录下的所有 demo 模块。
    
    返回按文件名数字排序的 demo 列表，每项为 (slug, name, show_func)。
    """
    demos_dir = Path(__file__).parent
    demo_pattern = re.compile(r"^(\d+)_(.+)\.py$")
    
    demos: list[tuple[int, str, str, Callable[[], None]]] = []
    
    for file in demos_dir.iterdir():
        if not file.is_file():
            continue
        
        match = demo_pattern.match(file.name)
        if not match:
            continue
        
        order = int(match.group(1))
        slug = match.group(2)
        module_name = file.stem  # e.g., "01_double_slit"
        
        try:
            module = importlib.import_module(f"demos.{module_name}")
            
            if not hasattr(module, "get_name") or not hasattr(module, "show"):
                continue
            
            name = module.get_name()
            show_func = module.show
            demos.append((order, slug, name, show_func))
        except Exception:
            continue
    
    # 按数字排序
    demos.sort(key=lambda x: x[0])
    
    # 返回 (slug, name, show_func)
    return [(slug, name, show_func) for _, slug, name, show_func in demos]


def build_registry() -> dict[str, tuple[str, Callable[[], None]]]:
    """
    构建 demo 注册表。
    
    返回: {slug: (name, show_func), ...}
    """
    demos = discover_demos()
    return {slug: (name, show_func) for slug, name, show_func in demos}
