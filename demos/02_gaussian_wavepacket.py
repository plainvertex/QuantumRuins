"""
高斯波包时间演化 - 交互演示模块

可视化初始静止高斯波包在不同时刻的概率密度分布。
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from core.gaussian_wavepacket import compute_wavepacket_evolution

def get_name() -> str:
    """返回 demo 的中文名称（含 emoji）"""
    return "📦 高斯波包"

def show():
    """渲染高斯波包演化演示页面"""
    
    # --- Sidebar: 控制面板 ---
    st.sidebar.subheader("📐 模型参数")
    st.sidebar.info("$\\sigma=1$, $m=1$, $\\hbar=1$")
    
    st.sidebar.markdown("---")
    st.sidebar.subheader("⏱️ 时间选择")
    
    input_method = st.sidebar.radio(
        "时间输入方式",
        ["预设时间点", "自定义输入"],
    )
    
    if input_method == "预设时间点":
        preset_options = {
            "短时演化 (0, 1, 2, 3)": [0, 1, 2, 3],
            "中等演化 (0, 2, 4, 6, 8)": [0, 2, 4, 6, 8],
            "长时演化 (0, 5, 10, 15, 20)": [0, 5, 10, 15, 20],
            "细粒度 (0, 0.5, 1, 1.5, 2, 2.5, 3)": [0, 0.5, 1, 1.5, 2, 2.5, 3],
        }
        selected_preset = st.sidebar.selectbox(
            "选择预设",
            list(preset_options.keys()),
        )
        t_values = preset_options[selected_preset]
    else:
        custom_input = st.sidebar.text_input(
            "输入时间点（逗号分隔）",
            value="0, 1, 2, 4, 8",
            help="例如：0, 1, 2, 4, 8",
        )
        try:
            t_values = [float(t.strip()) for t in custom_input.split(",") if t.strip()]
            if not t_values:
                t_values = [0]
                st.sidebar.warning("使用默认值 t=0")
        except ValueError:
            t_values = [0]
            st.sidebar.error("格式错误，使用 t=0")
    
    st.sidebar.markdown("---")
    
    x_range = st.sidebar.slider(
        "x 轴范围",
        min_value=5.0,
        max_value=30.0,
        value=15.0,
        step=1.0,
        help="调整显示的空间范围 [-x, x]",
    )
    
    st.sidebar.markdown("---")
    st.sidebar.caption(f"时间点：{', '.join(f't={t}' for t in sorted(t_values))}")
    
    # --- Main Area: 可视化 ---
    st.title(get_name())
    st.markdown("""
这是一个**高斯波包时间演化**的交互演示。观察初始静止的高斯波包如何随时间扩展。

> 💡 **物理原理**：自由粒子的高斯波包会随时间展宽，这是量子力学中不确定性原理的体现。
> 波包的宽度与时间的关系反映了位置-动量不确定性。
""")

    # 计算概率密度
    x, densities = compute_wavepacket_evolution(
        t_values=sorted(t_values),
        x_min=-x_range,
        x_max=x_range,
        num_points=500,
    )

    st.divider()

    # 绘制概率密度图
    st.subheader("📊 概率密度分布 $|\\Psi(x,t)|^2$")

    colors = px.colors.qualitative.Plotly

    fig = go.Figure()

    for i, t in enumerate(sorted(t_values)):
        color = colors[i % len(colors)]
        fig.add_trace(go.Scatter(
            x=x,
            y=densities[t],
            mode="lines",
            line=dict(color=color, width=2),
            name=f"t = {t}",
            hovertemplate=f"t={t}<br>x: %{{x:.2f}}<br>|Ψ|²: %{{y:.4f}}<extra></extra>",
        ))

    fig.update_layout(
        xaxis_title="位置 x",
        yaxis_title="概率密度 |Ψ(x,t)|²",
        hovermode="x unified",
        margin=dict(l=60, r=20, t=40, b=60),
        height=500,
        template="plotly_white",
        legend=dict(
            title="时间 t",
            yanchor="top",
            y=0.99,
            xanchor="right",
            x=0.99,
        ),
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

    # 观察说明
    st.divider()
    st.subheader("🔍 观察要点")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
**波包展宽**：
- 随着时间增加，波包逐渐变宽
- 峰值高度降低（概率守恒）
- 总概率（曲线下面积）始终为 1
""")

    with col2:
        st.markdown("""
**物理意义**：
- 位置不确定性随时间增大
- 体现了自由粒子的量子扩散
- 初始越局域化，扩散越快
""")

    # --- Main Area: 物理解释 ---
    st.divider()
    st.header("📖 物理原理")

    st.markdown(r"""
**波函数表达式**（$\sigma=1, m=1, \hbar=1$）：

$$\Psi(x, t) = (2\pi)^{-1/4} \left(1 + i\frac{t}{2}\right)^{-1/2} \exp\left(-\frac{x^2}{4(1 + t^2/4)}\right)$$

**概率密度**：

$$|\Psi(x,t)|^2 = \frac{1}{\sqrt{2\pi(1 + t^2/4)}} \exp\left(-\frac{x^2}{2(1 + t^2/4)}\right)$$

这是一个均值为 0、方差为 $\sigma^2(t) = 1 + t^2/4$ 的高斯分布。

**波包宽度随时间变化**：

$$\sigma(t) = \sqrt{1 + \frac{t^2}{4}}$$

- $t=0$ 时：$\sigma(0) = 1$（初始宽度）
- $t \to \infty$ 时：$\sigma(t) \approx t/2$（线性增长）
""")

    st.header("🔬 深入理解")

    st.markdown(r"""
### 不确定性关系

位置不确定性 $\Delta x = \sigma(t)$ 随时间增大，而动量不确定性 $\Delta p$ 保持不变，
始终满足海森堡不确定性原理：

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

### 物理直觉

为什么自由粒子的波包会扩展？

1. **动量叠加**：高斯波包是由不同动量的平面波叠加而成
2. **色散效应**：不同动量分量以不同速度传播
3. **初始局域化代价**：越精确的初始位置，意味着越大的动量分布，因此扩散越快

这个过程是不可逆的——自由粒子的波包只会越来越宽，永远不会自发收缩。
""")
