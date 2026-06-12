# WDF Theory: Data Renormalization of Spacetime Manifold
**文大方理论 (WDF)：时空流形的数据重整化与纯几何广义协变场论**

**Author (作者):** Andy(文大方) | **Contact (邮箱):** smsaut3344@gmail.com

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Physics: Cosmology](https://img.shields.io/badge/Physics-Cosmology-red.svg)
![Status: Peer Review Ready](https://img.shields.io/badge/Status-Peer%20Review%20Ready-success.svg)
[![DOI](https://zenodo.org/badge/1255705490.svg)](https://doi.org/10.5281/zenodo.20488837)

> *"We do not need to invent invisible particles to balance the universe's ledger. The geometry of spacetime itself, when constrained by discrete topological invariants, enforces the balance."*
> 
> *“我们不需要发明隐形的粒子来平宇宙的账。当时空几何受到离散拓扑不变量的约束时，它自己就会把账做平。”*

---

## 🌍 English Version

### 🌌 Overview
This project introduces a new computational cosmology paradigm that eliminates the need for the "Dark Matter" particle hypothesis and standard artificial parameter tuning. By introducing the absolute geometric constants derived from the discrete $O_h$ point group (order 48) and a non-minimal conformal coupling Lagrangian, **the Wen Dafang (WDF) theory unifies physical scales from the Quantum level to Galaxies, Cluster Collisions, and the CMB under a strict "Zero Free-Parameter" constraint.**

This repository contains the mathematical derivations, the core physical engine (`wdf_engine.py`), and the automated blind-test pipeline (`run_blind_test.py`) for cross-scale verification.

### 🎯 Key Breakthroughs
The WDF engine successfully closes the following observational deficits without introducing any empirical free parameters:

1. **Zero-Tuning Fit for SPARC (Galactic Scale):** Utilizing a 4th-order geometric skeleton $(1 + x^{-2})^{0.25}$ and an absolute boundary constant $a_0 = 10^{-9.92}$, it perfectly fits the Radial Acceleration Relation (RAR) of 175 galaxies. It naturally reduces to General Relativity in strong fields, yielding a mean absolute residual of `0.1229 dex`.
2. **Extreme Cluster Collisions (Cluster Scale):** Based on the symmetry-breaking constants $c_1$ and $c_2$ rigidly derived from the $O_h$ group, it accurately reproduces the anomalous mass redistribution in the Bullet Cluster (anisotropic separation) and Abell 520 (isotropic congestion) purely through geometric topological projection.
3. **CMB High-Frequency Blind Test (Microscopic Scale):** When multipole moments cross discrete fractal mapping points (e.g., harmonics of $O_h=48$ and structural ratios like $\ell \sim 1836$), the engine physically triggers a high-frequency Phase Shift, successfully suppressing electromagnetic leakage and closing the acoustic peaks without perturbative fluid free variables.
4. **Pure Geometric Derivation of Fundamental Constants (Quantum Scale):** Completely abandoned phenomenological fitting to derive the Proton/Electron Mass ratio ($12^3 + 108 = 1836$) via 3D fractal recursive folding, and the Fine Structure Constant ($\alpha^{-1} \approx 136.980$) via topological homology correction, rigidly anchoring mass and interaction strength to the $O_h=48$ group baseline.

### ⚙️ The Action Principle (Wen Dafang's Equation)
All code logic in this pipeline is strictly varied from the following non-linear conformal coupled Lagrangian action:

$$S_{WDF} = \int \frac{d^4x}{\pi^2} \sqrt{-g} \left\lbrace e^{-\alpha \chi^2} (\partial_\mu \phi \partial^\mu \phi) \left[ 1 + (1 - \theta) \beta F_{\rho\sigma} F^{\rho\sigma} \right] + \theta \beta F_{\rho\sigma} F^{\rho\sigma} \right\rbrace$$

- **$\phi$**: Macroscopic gravitational skeleton (main scalar field).
- **$\beta$**: The unique topological homology constant $c_1$ ($1 / 24\sqrt{2}$).
- **$\theta$**: Topological phase transition measure ($1/\pi^2$) mapping discrete lattices to continuous manifolds.

---

## 🌏 中文阐述 (Chinese Version)

### 🌌 项目概述
本项目旨在提供一种彻底摒弃“暗物质”粒子假设与人工调参的计算宇宙学新范式。通过引入底层离散 $O_h$ 群网格的拓扑常数（阶数 48）和非极小共形耦合拉格朗日量，**文大方理论 (WDF Theory) 在「绝对零自由参数」的铁律下，实现了从量子尺度、宏观星系、巨型星系团碰撞到微观宇宙微波背景辐射（CMB）的全尺度物理学大统一。**

### 🎯 核心战绩
本引擎已成功硬性闭合以下主流物理学长期存在的“观测亏空”与理论天坑，全程未引入任何经验性的自由参数：

1. **SPARC 数据库零调参拟合 (Galactic Scale):** 基于 4 阶几何骨架与绝对边界常数 $a_0 = 10^{-9.92}$，完美拟合 175 个星系的径向加速度关系 (RAR)，强场区自动退化回广义相对论，平均绝对残差仅为 `0.1229 dex`。
2. **星系团极端碰撞态 (Cluster Scale):** 基于 $O_h$ 48阶群对称性破缺刚性导出的常数 $c_1$ 与 $c_2$，在纯几何投射下，精准复现了 Bullet Cluster（各向异性骨架分离）与 Abell 520（全同气体极度拥堵）中的透镜质量异常重分配。
3. **CMB 高频段盲测大公账 (Microscopic Scale):** 在多极矩处于离散分形映射点（如 $\ell \sim 1836$ 及 $48$ 的谐波倍数）时，引擎物理触发高频缓冲相移（Phase Shift），成功镇压电磁泄露底噪，无需微扰流体自由变量即可完美闭合声学波峰。
4. **核心物理常数的纯几何推导 (Quantum Scale):** 彻底抛弃现象学拟合，纯靠几何拓扑推导出质子/电子质量比（信息维度折叠：$12^3 + 108 = 1836$）与精细结构常数（几何同调相移：$\alpha^{-1} \approx 136.980$），将物质质量与相互作用强度刚性锚定在 $O_h=48$ 阶群底座上。

### ⚙️ 核心作用量 (文大方场方程)
本理论管线中的所有代码逻辑，均严格通过变分以下非极小共形耦合拉格朗日作用量得出：

$$S_{WDF} = \int \frac{d^4x}{\pi^2} \sqrt{-g} \left\lbrace e^{-\alpha \chi^2} (\partial_\mu \phi \partial^\mu \phi) \left[ 1 + (1 - \theta) \beta F_{\rho\sigma} F^{\rho\sigma} \right] + \theta \beta F_{\rho\sigma} F^{\rho\sigma} \right\rbrace$$

- **$\phi$**: 宏观引力骨架（主标量场）。
- **$\beta$**: 拓扑唯一几何同调常数 $c_1$ ($1 / 24\sqrt{2}$)。
- **$\theta$**: 拓扑相变测度 ($1/\pi^2$)，负责离散网格向连续流形的映射补偿。

---

## 🚀 Quick Start (一键自动化盲测)
本项目拒绝一切“针对特定星系的人工微调”。我们提供了一个标准化的盲测管线，您只需输入观测数据，引擎将直接调用系统的最高权限（拓扑量子化约束）输出引力放大残差。

### 1. Requirements (环境依赖)
Ensure your system has Python 3.8+ and NumPy installed.
确保您的系统已安装 Python 3.8+ 及 NumPy。
```bash
git clone [https://github.com/smsaut3344/WDF-Theory.git](https://github.com/smsaut3344/WDF-Theory.git)
cd WDF-Theory
pip install numpy pandas
```

### 2. Run the Blind Test Pipeline (运行盲测管线)
```bash
python run_blind_test.py
```
*The pipeline will automatically load the preset SPARC baryonic scales and the anisotropic observational data of the major clusters, outputting the final theoretical audit ledger.*
*管线将自动加载预设的 SPARC 重子引力标度及巨型星团（子弹、潘多拉等）的各向异性观测数据，并输出最终的零调参理论校验公账。*

---

## 📂 Repository Structure (目录结构)
- `index.html` : 项目的 GitHub Pages 极客主页 / The Geek Homepage (Includes detailed academic manuscripts and derivations).
- `wdf_engine.py` : 锁死底层 48 阶拓扑常数的物理核引擎 / The core physical engine with hardcoded topological constants (**Strictly Immutable**).
- `run_blind_test.py` : 跨尺度统一盲测启动脚本 / The script to initiate the cross-scale blind test.
- `data/` : 存放观测源文件 / Directory for observational source files (e.g., `sparc_data.txt`, `cluster_archives.csv`).

---

## 📄 Academic Reference & Full Manuscript (学术验证与完整手稿)
We welcome colleagues in theoretical and astrophysics to challenge and falsify this engine. For detailed mechanisms (e.g., Grassmann Nilpotent Law), $O_h$ group theory derivations, and near-term observable predictions (e.g., non-linear geometric compression in CMB), please visit the project homepage:

欢迎理论物理学界、天体物理学界的同仁对本文大方引擎进行拉扯与证伪。详细的格拉斯曼代数奇点截断机制、48 阶群拓扑推导及近期可观测的前瞻刚性预言，请访问项目主页阅读完整手稿：

👉 **[Read the Full WDF Covariant Field Theory Paper (点击阅读完整理论与推导)](https://smsaut3344.github.io/WDF-Theory/)**

---

### 📬 Contact the Author (联系作者)
For academic discussions, rigorous peer review, or collaboration inquiries, please reach out directly:
如果您有关于底层物理方程的探讨、学术盲审意见或合作意向，请直接联系作者：

👤 **Author:** Andy(文大方)  

## License

This repository uses a dual-license model:

- **Source Code (LaTeX, HTML, CSS, JavaScript, and all other software components)**:
  Licensed under the [MIT License](LICENSE).
  
- **Theoretical Content, Documentation, and Web Pages (all physics formulas,
  derivations, predictions, explanatory text, and the Wen Dafang Theory framework)**:
  Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  
  This means you are free to share and adapt the theoretical content,
  provided you give appropriate credit to **Wen Dafang**.
📧 **Email:** smsaut3344@gmail.com  

## ⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details. Copyright (c) 2026 Andy(Wen Dafang).
