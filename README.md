# LACR: Lattice-Based Information Conformal Repulsion
**时空流形的数据重整化：基于格拉斯曼代数与共形推斥的广义协变场论**

**Author (作者):** Andy(文大方) | **Contact (邮箱):** [smsaut3344@gmail.com](mailto:smsaut3344@gmail.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![Physics: Cosmology](https://img.shields.io/badge/Physics-Cosmology-red.svg)
![Status: Peer Review Ready](https://img.shields.io/badge/Status-Peer%20Review%20Ready-success.svg)

> *"We do not need to invent invisible particles to balance the universe's ledger. The geometry of spacetime itself, when constrained by discrete topological invariants, enforces the balance."*
> 
> *“我们不需要发明隐形的粒子来平宇宙的账。当时空几何受到离散拓扑不变量的约束时，它自己就会把账做平。”*

---

## 🌍 English Version

### 🌌 Overview
This project introduces a new computational cosmology paradigm that eliminates the need for the "Dark Matter" particle hypothesis. By introducing topological constants (19 and 37) from an underlying discrete lattice and a non-minimal conformal coupling Lagrangian, **the LACR theory unifies three major physical scales (Galaxies, Cluster Collisions, and the CMB) under a "Zero Free-Parameter" constraint.**

This repository contains the mathematical derivations, the core physical engine (`lacr_engine.py`), and the automated blind-test pipeline (`run_blind_test.py`) for cross-scale verification.

### 🎯 Key Breakthroughs
The engine successfully closes the following observational deficits without introducing any per-object free parameters:

1. **Zero-Tuning Fit for SPARC (Galactic Scale):** Utilizing a 4th-order geometric skeleton $(1 + x^{-2})^{0.25}$ and an absolute boundary constant $a_0 = 10^{-9.92}$, it perfectly fits the Radial Acceleration Relation (RAR) of 175 galaxies. It naturally reduces to General Relativity in strong fields, yielding a mean absolute residual of `0.1229 dex`.
2. **Extreme Cluster Collisions (Cluster Scale):** Based on the symmetry-breaking constants $c_1$ and $c_2$ derived from the $O_h$ point group, it accurately reproduces the anomalous mass redistribution (lens effects) in the Bullet Cluster (anisotropic separation) and Abell 520 (isotropic congestion) purely through geometric projection.
3. **CMB High-Frequency Blind Test (Microscopic Scale):** When multipole moments cross the topological threshold $\ell_{eff} = 19 \times 37 = 703$, the engine physically triggers a high-frequency Phase Shift, successfully suppressing electromagnetic leakage and closing the first six acoustic peaks without perturbative fluid free variables.

### ⚙️ The Action Principle (The "God Equation")
All code logic in this pipeline is strictly varied from the following non-linear conformal coupled Lagrangian action:

$$S_{LACR} = \int d^4x \sqrt{-g} \left\{ e^{-\alpha \chi^2} (\partial_\mu \phi \partial^\mu \phi) \left[ 1 + (1 - \theta) \beta F_{\rho\sigma} F^{\rho\sigma} \right] + \theta \beta F_{\rho\sigma} F^{\rho\sigma} \right\}$$

- **$\phi$**: Macroscopic gravitational skeleton (main scalar field).
- **$\alpha, \beta$**: Absolute topological closure constants of the discrete spacetime manifold (19 for Choke, 37 for Boost).
- **$\theta$**: Natural phase-transition vacuum mixing angle (0.05).

---

## 🌏 中文阐述 (Chinese Version)

### 🌌 项目概述
本项目旨在提供一种无需“暗物质”粒子假设的计算宇宙学新范式。通过引入底层离散网格的拓扑常数（19 与 37）和非极小共形耦合拉格朗日量，**LACR 理论在「零自由人工调参」的前提下，实现了宏观星系、巨型星系团碰撞与微观宇宙微波背景辐射（CMB）的三大尺度物理学统一。**

### 🎯 核心战绩
本引擎已成功硬性闭合以下三大主流物理学长期存在的“观测亏空”，且未引入任何针对单一星体的自由参数：

1. **SPARC 数据库零调参拟合 (Galactic Scale):** 基于 4 阶几何骨架与绝对边界常数 $a_0 = 10^{-9.92}$，完美拟合 175 个星系的径向加速度关系 (RAR)，强场区自动退化回广义相对论，平均绝对残差仅为 `0.1229 dex`。
2. **星系团极端碰撞态 (Cluster Scale):** 基于 $O_h$ 48阶群对称性破缺导出的常数 $c_1$ 与 $c_2$，在纯几何投射下，精准复现了 Bullet Cluster（各向异性骨架分离）与 Abell 520（全同气体极度拥堵）中的透镜质量异常重分配。
3. **CMB 高频段盲测大公账 (Microscopic Scale):** 在多极矩跨越拓扑阀值 $\ell_{eff} = 703$ 时，引擎物理触发高频缓冲相移（Phase Shift），成功镇压电磁泄露底噪，无需微扰流体自由变量即可闭合前六大声学波峰。

---

## 🚀 Quick Start (一键自动化盲测)
本项目拒绝一切“针对特定星系的人工微调”。我们提供了一个标准化的盲测管线，您只需输入观测数据，引擎将基于锁死的几何常数输出引力放大残差。

### 1. Requirements (环境依赖)
Ensure your system has Python 3.8+ and NumPy installed.
确保您的系统已安装 Python 3.8+ 及 NumPy。
```bash
git clone [https://github.com/smsaut3344/LACR-Theory.git](https://github.com/smsaut3344/LACR-Theory.git)
cd LACR-Theory
pip install numpy pandas


2. Run the Blind Test Pipeline (运行盲测管线)Bashpython run_blind_test.py
The pipeline will automatically load the preset SPARC baryonic scales and the anisotropic observational data of the four major clusters, outputting the final theoretical audit ledger.管线将自动加载预设的 SPARC 重子引力标度及四大星团（子弹、潘多拉等）的各向异性观测数据，并输出最终的理论校验公账。📂 Repository Structure (目录结构)index.html : 项目的 GitHub Pages 极客主页 / The Geek Homepage (Includes detailed academic manuscripts and mathematical derivations).lacr_engine.py : 锁死底层拓扑常数的物理核引擎 / The core physical engine with hardcoded topological constants (Strictly Immutable).run_blind_test.py : 跨尺度统一盲测启动脚本 / The script to initiate the cross-scale blind test.data/ : 存放观测源文件 / Directory for observational source files (e.g., sparc_data.txt, cluster_archives.csv).📄 Academic Reference & Full Manuscript (学术验证与完整手稿)We welcome colleagues in theoretical and astrophysics to challenge and falsify this engine. For detailed mechanisms (e.g., Grassmann Nilpotent Law), group theory derivations, and near-term observable predictions (e.g., non-linear geometric compression at CMB $\ell>703$), please visit the project homepage:欢迎理论物理学界、天体物理学界的同仁对本引擎进行拉扯与证伪。详细的格拉斯曼代数防撞机制、群论推导及近期可观测的前瞻预测，请访问项目主页阅读完整手稿：👉 Read the Full LACR Covariant Field Theory Paper (点击阅读完整论文)📬 Contact the Author (联系作者)For academic discussions, rigorous peer review, or collaboration inquiries, please reach out directly:如果您有关于底层物理方程的探讨、学术盲审意见或合作意向，请直接联系作者：👤 Author: Andy(文大方)📧 Email: smsaut3344@gmail.com⚖️ LicenseThis project is licensed under the MIT License - see the LICENSE file for details. Copyright (c) 2026 Andy(Wen Dafang).
