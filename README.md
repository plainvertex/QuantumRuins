# ⚛️ Quantum Playground

一个可交互的量子物理实验集合，使用 Streamlit 构建，旨在通过可视化帮助理解量子力学的基本概念。

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)


## 🧪 已实现的实验

| 实验名称 | 说明 | 状态 |
|---------|------|------|
| **双缝干涉** | 探索波粒二象性的经典实验，观察干涉条纹如何随参数变化 | ✅ 可用 |

## 🚀 本地运行

### 环境要求

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)（推荐）或 pip

### 使用 uv（推荐）

```bash
# 安装依赖并运行
uv sync
uv run streamlit run app.py
```

### 使用 pip

```bash
# 安装依赖
pip install -r requirements.txt

# 启动应用
python -m streamlit run app.py
```

应用将在 `http://localhost:8501` 启动。

### 依赖管理

本项目使用 `pyproject.toml` 管理依赖，`requirements.txt` 由 uv 自动生成：

```bash
# 添加新依赖
uv add <package-name>

```

## ☁️ 部署到 Streamlit Community Cloud

### 步骤 1：推送到 GitHub

确保你的代码已推送到 GitHub 仓库：

```bash
git add .
git commit -m "Initial commit: Quantum Playground"
git push origin main
```

### 步骤 2：连接 Streamlit Cloud

0. 重新生成 requirements.txt（用于 Streamlit Cloud 部署）`uv pip freeze > requirements.txt`
1. 访问 [Streamlit Community Cloud](https://share.streamlit.io/)
2. 使用 GitHub 账号登录
3. 点击 "New app"
4. 选择你的仓库、分支和主文件 (`app.py`)
5. 点击 "Deploy"

### 步骤 3：等待部署完成

Streamlit Cloud 会自动：
- 检测 `requirements.txt` 并安装依赖
- 构建并启动应用
- 提供公开访问的 URL

## 📁 项目结构

```
├── app.py                    # 主入口 - 实验大厅
├── requirements.txt          # Python 依赖
├── README.md                 # 项目说明
├── core/                     # 物理计算核心模块
│   ├── __init__.py
│   ├── double_slit.py       # 双缝干涉计算
│   └── utils.py             # 通用工具函数
└── pages/                    # Streamlit 多页面
    └── 01_double_slit.py    # 双缝干涉交互页面
```

## 🔧 技术栈

- **[Streamlit](https://streamlit.io/)** - Web 应用框架
- **[NumPy](https://numpy.org/)** - 数值计算
- **[Plotly](https://plotly.com/python/)** - 交互式图表

## 📖 物理背景

### 双缝干涉

双缝干涉是量子力学中最著名的实验之一，展示了光的波粒二象性。

**干涉强度公式**（Fraunhofer 近似）：

$$I(x) = I_0 \cos^2\left(\frac{\pi d x}{\lambda L}\right)$$

其中：
- $d$：双缝间距
- $\lambda$：波长
- $L$：屏幕距离
- $x$：屏幕位置

## 📝 License

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！
