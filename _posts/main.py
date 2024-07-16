def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    """
    使用二分法求解函数 f 在区间 [a, b] 上的根。
    
    参数:
    f -- 要求解根的函数
    a, b -- 搜索区间的端点，应满足 $f(a)*f(b) < 0$，即函数在区间两端取值异号
    tol -- 容差，当区间宽度小于此值时停止迭代
    max_iter -- 最大迭代次数
    
    返回:
    root -- 函数的近似根
    iterations -- 实际迭代次数
    """
    if f(a) * f(b) >= 0:
        raise ValueError("初始区间 [a, b] 不满足 f(a)*f(b) &lt; 0 的条件，无法应用二分法。")
    
    iterations = 0
    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2  # 计算区间中点
        
        # 根据中点的函数值调整搜索区间
        if f(c) == 0:  # 如果中点就是根，直接返回
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c  # 根在 [a, c] 内
        else:
            a = c  # 根在 [c, b] 内
        
        iterations += 1
    
    if iterations == max_iter:
        print("达到最大迭代次数，可能未收敛到足够精度。")
    
    return (a + b) / 2, iterations  # 返回区间的中点作为近似根和迭代次数

# 示例：求解方程 x**3 - x - 1 = 0 的根
def f(x):
    return x**3 - x - 1

# 选择一个包含根的区间，确保区间两端函数值异号
root, iterations = bisection_method(f, 1, 2)
print(f"方程的近似根为: {root}")
print(f"迭代次数: {iterations}")
