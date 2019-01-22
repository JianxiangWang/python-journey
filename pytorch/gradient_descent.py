import torch
from torch.autograd import Variable

w1 = Variable(torch.Tensor([40.]), requires_grad=True)
w2 = Variable(torch.Tensor([19.]), requires_grad=True)


def gradient_is_accumulated_when_backward():
    for i in range(1000):
        y = w1 ** 2 + 1
        y.backward()
        print(y.data, w1.grad.data)
        w1.data -= 0.001 * w1.grad.data
        w1.grad.data.zero_()


def accumulate_gradient():
    accumulation_steps = 64.

    for i in range(100000):
        y = w1 ** 2 + w2 ** 4 + 1
        # y /= accumulation_steps
        y.backward()
        if (i + 1) % accumulation_steps == 0:
            print(y.data, w1.data, w1.grad.data)
            w1.data -= 0.001 * w1.grad.data
            w2.data -= 0.001 * w2.grad.data
            w1.grad.data.zero_()
            w2.grad.data.zero_()


if __name__ == '__main__':
    accumulate_gradient()
