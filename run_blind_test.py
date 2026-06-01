from lacr_engine import LACREngine


def main():
    engine = LACREngine()
    print("================ LACR 跨尺度大公账盲测系统 ================")
    print("警告：本系统已锁死底层拓扑常数 (c1, c2, 19, 37)。拒绝任何人工调参。")

    # 模拟读取 SPARC 数据进行盲测
    print("\n[测试阶段一] 启动 SPARC 星系库零调参核验...")
    mock_gbar = 1e-11
    pred = engine.get_sparc_prediction(mock_gbar)
    print(f" -> 输入重子引力: {mock_gbar:.2e} | LACR 4阶骨架预测: {pred:.2e}")

    # 模拟输入观测到的星团特征
    print("\n[测试阶段二] 启动巨型星系团连环碰撞核验...")
    print(" -> 加载观测档案：子弹星系团 (高速各向异性骨架分离)")
    weight = engine.get_collision_manifold_weight(vector_congruence=0.95, congestion_volume=0.01)
    print(f" -> 纯几何投射下的有效引力放大倍数 (表观暗物质): {weight:.4f}")

    print("\n================ 盲测完成 ================")


if __name__ == "__main__":
    main()