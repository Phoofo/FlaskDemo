# import torch
# import torch.nn as nn
#
# # 设置输入节点、隐藏层节点和输出层节点数量
# input_size = 1000
# hidden_size = 100
# output_size = 10
#
# # 定义神经网络模型
# model = nn.Sequential(
#     nn.Linear(input_size, hidden_size),  # 输入层到隐藏层的线性层
#     nn.ReLU(),  # 隐藏层的激活函数
#     nn.Linear(hidden_size, output_size)  # 隐藏层到输出层的线性层
# )
#
# # 定义损失函数
# criterion = nn.CrossEntropyLoss()
#
# # 定义优化器
# optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
#
# # 生成随机输入数据
# input_data = torch.randn(100, input_size)
#
# # 生成随机分类结果
# target = torch.randint(output_size, (100,))
#
# # 前向传播
# output = model(input_data)
#
# # 计算损失
# loss = criterion(output, target)
#
# # 后向传播
# optimizer.zero_grad()
# loss.backward()
# optimizer.step()

import torch

batch_n = 100  # 一个批次输入数据的数量
hidden_layer = 100
input_data = 1000  # 每个数据的特征为1000
output_data = 10

x = torch.randn(batch_n, input_data)
y = torch.randn(batch_n, output_data)

w1 = torch.randn(input_data, hidden_layer)
w2 = torch.randn(hidden_layer, output_data)

epoch_n = 20
lr = 1e-6

for epoch in range(epoch_n):
    h1 = x.mm(w1)  # (100,1000)*(1000,100)-->100*100
    print(h1.shape)
    h1 = h1.clamp(min=0)
    y_pred = h1.mm(w2)

    loss = (y_pred - y).pow(2).sum()
    print("epoch:{},loss:{:.4f}".format(epoch, loss))

    grad_y_pred = 2 * (y_pred - y)
    grad_w2 = h1.t().mm(grad_y_pred)

    grad_h = grad_y_pred.clone()
    grad_h = grad_h.mm(w2.t())
    grad_h.clamp_(min=0)  # 将小于0的值全部赋值为0，相当于sigmoid
    grad_w1 = x.t().mm(grad_h)

    w1 = w1 - lr * grad_w1
    w2 = w2 - lr * grad_w2
