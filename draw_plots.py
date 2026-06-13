import numpy as np
import matplotlib.pyplot as plt
from numba import njit  # 需要先 pip install numba
from scipy.ndimage import map_coordinates

plt.rcParams.update({
    'font.size': 11,
    'axes.linewidth': 1.2,
    'xtick.major.width': 1.0,
    'ytick.major.width': 1.0,
    'figure.dpi': 300,
})


@njit
def poisson_sor_3d(source, dx, omega=1.84, max_iter=3000, tol=1e-7):
    """
    3D Poisson solver: ∇²φ = source, with φ=0 at boundaries.
    Uses point SOR on a regular grid.
    Returns phi and residual history.
    """
    N = source.shape[0]
    phi = np.zeros_like(source)
    inv_dx2 = 1.0 / (dx * dx)
    res_history = []

    for it in range(max_iter):
        max_res = 0.0
        # Loop over interior points
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                for k in range(1, N - 1):
                    # 7-point stencil
                    lap = (phi[i + 1, j, k] + phi[i - 1, j, k] +
                           phi[i, j + 1, k] + phi[i, j - 1, k] +
                           phi[i, j, k + 1] + phi[i, j, k - 1] - 6.0 * phi[i, j, k]) * inv_dx2
                    residual = source[i, j, k] - lap

                    # 核心修正处：由 += 改为 -=，确保系统处于负反馈收敛状态
                    phi[i, j, k] -= omega * residual / (6.0 * inv_dx2)
                    max_res = max(max_res, abs(residual))

        # Compute L2 norm of residual over interior
        if it % 10 == 0:
            res_grid = np.zeros_like(source)
            for i in range(1, N - 1):
                for j in range(1, N - 1):
                    for k in range(1, N - 1):
                        lap = (phi[i + 1, j, k] + phi[i - 1, j, k] +
                               phi[i, j + 1, k] + phi[i, j - 1, k] +
                               phi[i, j, k + 1] + phi[i, j, k - 1] - 6.0 * phi[i, j, k]) * inv_dx2
                        res_grid[i, j, k] = source[i, j, k] - lap
            l2 = np.sqrt(np.mean(res_grid[1:-1, 1:-1, 1:-1] ** 2))
            res_history.append(l2)

        if max_res < tol:
            print("SOR converged at iter", it, ", max_res =", max_res)
            break
    else:
        print("SOR reached max_iter", max_iter, ", max_res =", max_res)

    return phi, np.array(res_history)


def build_source_bullet(N, L):
    """Construct source for Bullet-like collision."""
    x = np.linspace(-L / 2, L / 2, N)
    y = np.linspace(-L / 2, L / 2, N)
    z = np.linspace(-L / 2, L / 2, N)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

    vx_left = np.exp(-((X + 1.2) ** 2 + Y ** 2 + Z ** 2) / 0.8)
    vx_right = -1.2 * np.exp(-((X - 1.5) ** 2 + Y ** 2 + Z ** 2) / 0.8)
    vy = 0.3 * np.exp(-(X ** 2 + (Y - 0.5) ** 2 + Z ** 2) / 1.0)
    vz = 0.2 * np.exp(-(X ** 2 + Y ** 2 + (Z - 0.3) ** 2) / 1.0)

    Jx = vx_left + vx_right
    Jy = vy
    Jz = vz

    dJy_dz = np.gradient(Jy, z, axis=2)
    dJz_dy = np.gradient(Jz, y, axis=1)
    dJx_dz = np.gradient(Jx, z, axis=2)
    dJz_dx = np.gradient(Jz, x, axis=0)
    dJy_dx = np.gradient(Jy, x, axis=0)
    dJx_dy = np.gradient(Jx, y, axis=1)

    curl_x = dJz_dy - dJy_dz
    curl_y = dJx_dz - dJz_dx
    curl_z = dJy_dx - dJx_dy

    S = Jx * curl_x + Jy * curl_y + Jz * curl_z
    S = S / np.max(np.abs(S)) * 0.5
    return S


def build_source_abell520(N, L):
    """Source for Abell 520."""
    x = np.linspace(-L / 2, L / 2, N)
    y = np.linspace(-L / 2, L / 2, N)
    z = np.linspace(-L / 2, L / 2, N)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

    Jx = (np.exp(-((X + 1.0) ** 2 + (Y - 1.0) ** 2 + Z ** 2) / 0.6) -
          1.3 * np.exp(-((X - 1.2) ** 2 + (Y + 0.8) ** 2 + Z ** 2) / 0.6))
    Jy = (0.5 * np.exp(-((X - 0.8) ** 2 + (Y + 1.2) ** 2 + Z ** 2) / 0.7) -
          0.7 * np.exp(-((X + 0.9) ** 2 + (Y - 0.9) ** 2 + Z ** 2) / 0.7))
    Jz = 0.4 * np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / 1.2) * np.sin(2 * np.pi * X / L) * np.cos(2 * np.pi * Y / L)

    dJy_dz = np.gradient(Jy, z, axis=2)
    dJz_dy = np.gradient(Jz, y, axis=1)
    dJx_dz = np.gradient(Jx, z, axis=2)
    dJz_dx = np.gradient(Jz, x, axis=0)
    dJy_dx = np.gradient(Jy, x, axis=0)
    dJx_dy = np.gradient(Jx, y, axis=1)

    curl_x = dJz_dy - dJy_dz
    curl_y = dJx_dz - dJz_dx
    curl_z = dJy_dx - dJx_dy

    S = Jx * curl_x + Jy * curl_y + Jz * curl_z
    S = S / np.max(np.abs(S)) * 0.5
    return S


def gas_density_bullet(N, L):
    x = np.linspace(-L / 2, L / 2, N)
    y = np.linspace(-L / 2, L / 2, N)
    z = np.linspace(-L / 2, L / 2, N)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    gas = (0.9 * np.exp(-((X + 0.8) ** 2 + Y ** 2 + Z ** 2) / 1.2) +
           1.1 * np.exp(-((X - 1.8) ** 2 + Y ** 2 + Z ** 2) / 1.0))
    return gas


def gas_density_abell520(N, L):
    x = np.linspace(-L / 2, L / 2, N)
    y = np.linspace(-L / 2, L / 2, N)
    z = np.linspace(-L / 2, L / 2, N)
    X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
    gas = (np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / 2.5) * 0.4 +
           1.3 * np.exp(-((X + 2.2) ** 2 + (Y - 1.8) ** 2 + Z ** 2) / 1.2) +
           1.3 * np.exp(-((X - 2.2) ** 2 + (Y + 1.8) ** 2 + Z ** 2) / 1.2))
    return gas


def main():
    N = 128
    L = 6.0
    dx = L / N
    omega = 1.84

    print("=== Bullet Cluster simulation ===")
    S_bullet = build_source_bullet(N, L)
    phi_bullet, res_bullet = poisson_sor_3d(S_bullet, dx, omega=omega, max_iter=2000, tol=1e-7)

    print("=== Abell 520 simulation ===")
    S_abell = build_source_abell520(N, L)
    phi_abell, res_abell = poisson_sor_3d(S_abell, dx, omega=omega, max_iter=2000, tol=1e-7)

    # ---- Plotting ----
    fig1, ax1 = plt.subplots(figsize=(6, 4.5))
    ax1.semilogy(np.arange(0, len(res_bullet)) * 10, res_bullet, color='#1f77b4', lw=2.0,
                 label='SOR (ω=1.84)')
    ax1.axhline(1e-7, color='#d62728', ls='--', lw=1.2, label='Convergence Criterion (<10⁻⁷)')
    ax1.set_xlabel('Iteration Step')
    ax1.set_ylabel('Residual L₂ Norm')
    ax1.set_xlim(0, 1500)
    ax1.set_ylim(1e-9, 10)
    ax1.grid(True, which='both', linestyle=':', alpha=0.5)
    ax1.legend()
    plt.tight_layout()
    plt.savefig('figure_sor_convergence.pdf', bbox_inches='tight')
    plt.close(fig1)
    print("[成功] 图1保存为 figure_sor_convergence.pdf")

    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(11, 5))
    mid = N // 2
    x_coord = np.linspace(-L / 2, L / 2, N)

    # Bullet
    gas_b = gas_density_bullet(N, L)[:, :, mid].T
    phi_b = phi_bullet[:, :, mid].T
    ax2a.imshow(gas_b, extent=[-L / 2, L / 2, -L / 2, L / 2], origin='lower', cmap='Blues', alpha=0.85)
    ax2a.contour(x_coord, x_coord, phi_b, levels=5, colors='#d62728', linewidths=1.5)
    ax2a.set_xlabel('X (Mpc)')
    ax2a.set_ylabel('Y (Mpc)')
    ax2a.text(-2.8, 2.5, '(a) Bullet Cluster Topology (Normal Phase)',
              fontsize=11, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

    # 显式创建图例线，防止 contour 传空值导致的 label 遗失
    line = plt.Line2D([0], [0], color='#d62728', lw=1.5, label='0-form Gravity Field')
    ax2a.legend(handles=[line], loc='lower left')

    # Abell 520
    gas_a = gas_density_abell520(N, L)[:, :, mid].T
    phi_a = phi_abell[:, :, mid].T
    ax2b.imshow(gas_a, extent=[-L / 2, L / 2, -L / 2, L / 2], origin='lower', cmap='Purples', alpha=0.85)
    ax2b.contour(x_coord, x_coord, phi_a, levels=5, colors='#d62728', linewidths=1.5)
    ax2b.set_xlabel('X (Mpc)')
    ax2b.set_ylabel('Y (Mpc)')
    ax2b.text(-2.8, 2.5, '(b) Abell 520 Topology (Anomalous Phase)',
              fontsize=11, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))
    ax2b.legend(handles=[line], loc='lower left')

    plt.subplots_adjust(left=0.08, right=0.96, bottom=0.12, top=0.95, wspace=0.22)
    plt.savefig('figure_cluster_topology.pdf', bbox_inches='tight')
    plt.close(fig2)
    print("[成功] 图2保存为 figure_cluster_topology.pdf")


if __name__ == '__main__':
    main()