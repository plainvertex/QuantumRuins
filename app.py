"""
Quantum Playground - 量子物理交互实验大厅

单页面应用入口，使用自定义路由实现 demo 切换。
Demo 模块从 demos/ 目录自动发现。
"""

import streamlit as st
from demos import build_registry

st.set_page_config(
    page_title="Quantum Playground",
    page_icon="⚛️",
    layout="wide",
)

# --- 动态构建 Demo 注册表 ---
DEMO_REGISTRY = build_registry()
SLUGS = list(DEMO_REGISTRY.keys())
NAMES = [v[0] for v in DEMO_REGISTRY.values()]

# --- 初始化 session_state ---
if "current_demo" not in st.session_state:
    url_slug = st.query_params.get("demo", SLUGS[0] if SLUGS else "home")
    if url_slug not in SLUGS:
        url_slug = SLUGS[0] if SLUGS else "home"
    st.session_state.current_demo = url_slug

def on_demo_change():
    """处理 demo 切换"""
    selected_name = st.session_state.demo_selector
    selected_slug = SLUGS[NAMES.index(selected_name)]
    st.session_state.current_demo = selected_slug
    st.query_params["demo"] = selected_slug

# --- Sidebar: 导航 ---
current_slug = st.session_state.current_demo
current_name = DEMO_REGISTRY[current_slug][0]

st.sidebar.selectbox(
    "选择实验",
    NAMES,
    index=NAMES.index(current_name),
    key="demo_selector",
    on_change=on_demo_change,
)
st.sidebar.markdown("---")

# --- 路由到选中的 demo ---
DEMO_REGISTRY[st.session_state.current_demo][1]()
