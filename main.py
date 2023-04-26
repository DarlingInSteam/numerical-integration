import math


def f(x):
    return math.log(x) / math.sqrt(1.2 + 0.3 * x)


def is_runge(sh, shr, eps, r, p):
    return (abs(sh - shr) / ((r ** p) - 1)) < eps


def main(a, b, eps1, eps2):
    print("a = ", a)
    print("b = ", b, end="\n\n")

    print("sh = ", rect_runge(a, b, eps1))
    print("sh = ", rect_runge(a, b, eps2), end="\n\n")

    print("sh = ", simpson_runge(a, b, eps1))
    print("sh = ", simpson_runge(a, b, eps2), end="\n\n")

    print("sh = ", trapezoidal_runge(a, b, eps1))
    print("sh = ", trapezoidal_runge(a, b, eps2), end="\n\n")


def rect_runge(a, b, eps):
    print("l rectangle")
    print("eps = ", eps)
    h = b - a
    r = 2
    sh = rectangle_method(a, b, f, h)
    h /= r
    shr = rectangle_method(a, b, f, h)

    while not is_runge(sh, shr, eps, r, 1):
        sh = rectangle_method(a, b, f, h)
        h /= r
        shr = rectangle_method(a, b, f, h)
    print("h = ", h)
    return sh


def simpson_runge(a, b, eps):
    print("simpson")
    print("eps = ", eps)
    h = (b - a) / 2
    r = 2
    sh = simpson_method(a, b, f, h)
    h /= r
    shr = simpson_method(a, b, f, h)

    while not is_runge(sh, shr, eps, r, 4):
        sh = simpson_method(a, b, f, h)
        h /= r
        shr = simpson_method(a, b, f, h)
    print("h = ", h)
    return sh


def trapezoidal_runge(a, b, eps):
    print("trapezoidal")
    print("eps = ", eps)
    h = (b - a)
    r = 2
    sh = trapezoidal_method(a, b, f, h)
    h /= r
    shr = trapezoidal_method(a, b, f, h)

    while not is_runge(sh, shr, eps, r, 2):
        sh = trapezoidal_method(a, b, f, h)
        h /= r
        shr = trapezoidal_method(a, b, f, h)
    print("h = ", h)
    return sh


def rectangle_method(left, right, func, h):
    res = 0
    n = int((right - left) / h)
    for i in range(n):
        x = left + i * h
        res += h * func(x)
    return res


def simpson_method(left, right, func, h):
    res = 0
    n = int((right - left) / h)
    for i in range(n + 1):
        x = left + i * h
        if i == 0 or i == n:
            res += func(x)
        elif i % 2 == 0:
            res += 2 * func(x)
        else:
            res += 4 * func(x)
    return res * h / 3


def trapezoidal_method(left, right, func, h):
    res = 0
    n = int((right - left) / h)
    x = left

    for i in range(n):
        res += (func(x) + func(x + h)) * h / 2
        x += h

    return res


if __name__ == "__main__":
    main(5, 10, 0.01, 0.001)
