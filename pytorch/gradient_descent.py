import torch
from torch.autograd import Variable

w = Variable(torch.Tensor([100.]), requires_grad=True)

for _ in range(10000):
    y = w ** 2 + 1
    y.backward()
    print(y.data, w.grad.data)
    w.data -= 0.001 * w.grad.data
    w.grad.data.zero_()
