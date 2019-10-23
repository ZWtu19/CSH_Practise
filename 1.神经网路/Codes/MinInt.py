# 导入第三方库  
import numpy as np

# 定义目标函数z = x0**2 + x1**2
def function_1(x):
	return x[0]**2 + x[1]**2

# 定义梯度法  
def numerical_gradient(f, x):
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x) # 生成和x形状相同的数组
    for idx in range(x.size): 
        tmp_val = x[idx]
        # f(x+h)的计算
        x[idx] = tmp_val + h

        fxh1 = f(x)
        # f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        grad[idx] = (fxh1 - fxh2) / (2*h) 
        x[idx] = tmp_val # 还原值
    return grad

# 定义梯度下降法
def gradient_descent(f, init_x, lr=0.01, step_num=100):
	x = init_x
	for i in range(step_num):
		grad = numerical_gradient(f, x) 
		x -= lr * grad
	return x

init_x = np.array([-3.0, 4.0])
gradient_descent(function_1, init_x=init_x, lr=0.1, step_num=100)
