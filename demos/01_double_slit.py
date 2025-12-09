"""
双缝干涉实验 - 交互演示模块

通过调整波长、双缝间距和屏幕距离，观察干涉条纹的变化。
"""

import streamlit as st
import plotly.graph_objects as go
from core.double_slit import compute_double_slit


def get_name() -> str:
    """返回 demo 的中文名称（含 emoji）"""
    return "🌊 双缝干涉"


def show():
    """渲染双缝干涉演示页面"""
    
    # --- Sidebar: 控制面板 ---
    st.sidebar.subheader("⚙️ 实验参数")
    
    wavelength = st.sidebar.slider(
        "波长 λ",
        min_value=0.3,
        max_value=1.0,
        value=0.5,
        step=0.01,
        help="光的波长（任意单位）。波长越大，条纹间距越大。"
    )
    
    slit_distance = st.sidebar.slider(
        "双缝间距 d",
        min_value=1.0,
        max_value=5.0,
        value=2.0,
        step=0.1,
        help="两条狭缝之间的距离。间距越大，条纹越密。"
    )
    
    screen_distance = st.sidebar.slider(
        "屏幕距离 L",
        min_value=5.0,
        max_value=20.0,
        value=10.0,
        step=0.5,
        help="狭缝到观察屏的距离。距离越远，条纹越宽。"
    )
    
    x_range = st.sidebar.slider(
        "x 轴范围",
        min_value=5.0,
        max_value=50.0,
        value=25.0,
        step=1.0,
        help="调整显示的屏幕坐标范围 [-x, x]",
    )
    
    # 计算条纹间距
    fringe_spacing = wavelength * screen_distance / slit_distance
    
    st.sidebar.markdown("---")
    st.sidebar.metric("条纹间距 Δx", f"{fringe_spacing:.2f}")
    
    # --- Main Area: 可视化 ---
    st.title(get_name())
    st.markdown("""
这是一个经典的**双缝干涉**交互演示。调整左侧参数，实时观察干涉条纹的变化。

> 💡 **物理原理**：当相干光通过两条狭缝时，在屏幕上形成明暗相间的干涉条纹。
> 条纹间距与波长成正比，与双缝间距成反比。
""")

    # 计算干涉强度分布
    x, intensity = compute_double_slit(
        wavelength=wavelength,
        slit_distance=slit_distance,
        screen_distance=screen_distance,
        x_range=x_range,
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

    info_col1, info_col2, info_col3, info_col4 = st.columns(4)

    with info_col1:
        st.metric("波长 λ", f"{wavelength:.2f}")

    with info_col2:
        st.metric("双缝间距 d", f"{slit_distance:.1f}")

    with info_col3:
        st.metric("屏幕距离 L", f"{screen_distance:.1f}")

    with info_col4:
        st.metric("条纹间距", f"{fringe_spacing:.2f}")

    # --- Main Area: 物理解释 ---
    st.divider()
    st.header("📖 物理原理")

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

    st.header("🔬 深入理解")

    st.markdown("""
### 历史背景

双缝实验由托马斯·杨（Thomas Young）于1801年首次进行，是证明光具有波动性的关键实验。
这个实验后来成为量子力学中最著名的实验之一，因为它揭示了量子粒子的波粒二象性。

### 量子力学视角

在量子力学中，即使单个光子或电子通过双缝，也会形成干涉图样。这意味着：
- 每个粒子似乎同时通过两条狭缝
- 粒子与自身发生干涉
- 测量会破坏干涉（观测者效应）

这是量子力学中最令人困惑却又最基本的现象之一，被理查德·费曼称为
"包含了量子力学唯一的奥秘"。
""")
