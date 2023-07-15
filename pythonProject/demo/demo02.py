import torch

# 创建输入张量，要求梯度追踪
x = torch.tensor([2.0], requires_grad=True)

# 定义计算图
y = x**2 + 3*x + 1

# 计算梯度
y.backward()

# 打印梯度值
print(x.grad)
