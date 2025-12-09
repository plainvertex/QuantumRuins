"""
Quantum Playground - 量子物理交互实验大厅

这是一个多页面 Streamlit 应用的主入口，用于展示各种量子物理交互演示。
"""

import streamlit as st

st.set_page_config(
    page_title="Quantum Playground",
    page_icon="⚛️",
    layout="wide",
)

st.title("⚛️ Quantum Playground")
st.subheader("量子物理交互实验室")

st.markdown("""
---

欢迎来到 **Quantum Playground**！

这是一个可交互的量子物理实验集合，旨在通过可视化帮助理解量子力学的基本概念。

### 🧪 可用实验

👈 请从左侧边栏选择实验：

| 实验名称 | 说明 |
|---------|------|
| **双缝干涉** | 探索波粒二象性的经典实验，观察干涉条纹如何随参数变化 |
| **高斯波包演化** | 观察自由粒子高斯波包随时间的量子扩散过程 |

### 🎯 项目特点

- 🔬 **物理准确**：基于真实物理公式的仿真计算
- 🎨 **交互式**：实时调整参数，即时观察结果变化
- 📱 **响应式**：支持桌面和移动设备访问
- 🌐 **云端部署**：无需安装，浏览器直接访问

---

*本项目使用 Streamlit + NumPy + Plotly 构建*
""")

st.sidebar.success("👆 选择一个实验开始探索")
