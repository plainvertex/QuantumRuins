"""
双缝干涉实验 - 交互演示页面

通过调整波长、双缝间距和屏幕距离，观察干涉条纹的变化。
"""

import sys
from pathlib import Path

# 将项目根目录添加到 Python 路径，确保 Streamlit Cloud 可正确导入
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import plotly.graph_objects as go
from core.double_slit import compute_double_slit

st.set_page_config(
    page_title="双缝干涉 - Quantum Playground",
    page_icon="🌊",
    layout="wide",
)

st.title("🌊 双缝干涉实验")
st.markdown("""
这是一个经典的**双缝干涉**交互演示。调整下方参数，实时观察干涉条纹的变化。

> 💡 **物理原理**：当相干光通过两条狭缝时，在屏幕上形成明暗相间的干涉条纹。
> 条纹间距与波长成正比，与双缝间距成反比。
""")

st.divider()

# 参数控制区
st.subheader("⚙️ 实验参数")

col1, col2, col3 = st.columns(3)

with col1:
    wavelength = st.slider(
        "波长 λ",
        min_value=0.3,
        max_value=1.0,
        value=0.5,
        step=0.01,
        help="光的波长（任意单位）。波长越大，条纹间距越大。"
    )

with col2:
    slit_distance = st.slider(
        "双缝间距 d",
        min_value=1.0,
        max_value=5.0,
        value=2.0,
        step=0.1,
        help="两条狭缝之间的距离。间距越大，条纹越密。"
    )

with col3:
    screen_distance = st.slider(
        "屏幕距离 L",
        min_value=5.0,
        max_value=20.0,
        value=10.0,
        step=0.5,
        help="狭缝到观察屏的距离。距离越远，条纹越宽。"
    )

# 计算干涉强度分布
x, intensity = compute_double_slit(
    wavelength=wavelength,
    slit_distance=slit_distance,
    screen_distance=screen_distance,
)

st.divider()

# 绘制干涉图样
st.subheader("📊 干涉强度分布")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x,
    y=intensity,
    mode="lines",
    line=dict(color="#1f77b4", width=1.5),
    name="光强分布",
    hovertemplate="位置: %{x:.2f}<br>强度: %{y:.3f}<extra></extra>"
))

fig.update_layout(
    xaxis_title="屏幕位置 x",
    yaxis_title="归一化强度 I",
    yaxis_range=[0, 1.05],
    hovermode="x unified",
    margin=dict(l=60, r=20, t=40, b=60),
    height=450,
    template="plotly_white",
    xaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(128, 128, 128, 0.2)",
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor="rgba(128, 128, 128, 0.5)",
    ),
    yaxis=dict(
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(128, 128, 128, 0.2)",
    ),
)

st.plotly_chart(fig, use_container_width=True)

# 显示当前参数信息
st.divider()
st.subheader("📋 当前参数")

# 计算条纹间距
fringe_spacing = wavelength * screen_distance / slit_distance

info_col1, info_col2, info_col3, info_col4 = st.columns(4)

with info_col1:
    st.metric("波长 λ", f"{wavelength:.2f}")

with info_col2:
    st.metric("双缝间距 d", f"{slit_distance:.1f}")

with info_col3:
    st.metric("屏幕距离 L", f"{screen_distance:.1f}")

with info_col4:
    st.metric("条纹间距", f"{fringe_spacing:.2f}")

# 物理公式说明
with st.expander("📖 物理公式说明"):
    st.markdown(r"""
    **双缝干涉强度公式**（Fraunhofer 近似）：
    
    $$I(x) = I_0 \cos^2\left(\frac{\pi d x}{\lambda L}\right)$$
    
    其中：
    - $I_0$：最大光强（归一化为 1）
    - $d$：双缝间距
    - $\lambda$：波长
    - $L$：屏幕距离
    - $x$：屏幕上的位置坐标
    
    **相邻明条纹间距**：
    
    $$\Delta x = \frac{\lambda L}{d}$$
    
    **关键规律**：
    - 波长 $\lambda$ 越大 → 条纹间距越大
    - 双缝间距 $d$ 越大 → 条纹间距越小
    - 屏幕距离 $L$ 越大 → 条纹间距越大
    """)
