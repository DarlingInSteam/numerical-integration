import math


def f(x):
    return math.log(x) / math.sqrt(1.2 + 0.3 * x)


def rectangle_method(left, right, func, eps=0.001):

    def divide_sum(number_of_splits):
        nonlocal left, right, func
        step = (right - left) / float(number_of_splits)
        sum_in_step = sum([func(left + k * step) for k in range(0, number_of_splits)])
        result_in_step = step * sum_in_step
        return result_in_step

    steps = 2
    first_split = divide_sum(steps)
    steps *= 2
    second_split = divide_sum(steps)

    while abs(first_split - second_split) > eps :
        steps *= 2
        first_split = divide_sum(steps)
        steps *= 2
        second_split = divide_sum(steps)

    print(second_split, steps)


def trapezoidal_rule(left, right, func, eps=0.001):
    n = 1
    prev_result = 0
    result = (right - left) * (func(left) + func(right)) / 2

    while abs(result - prev_result) > eps:
        n *= 2
        h = (right - left) / n
        x = left + h
        sum = 0
        for i in range(1, n):
            sum += func(x)
            x += h
        prev_result = result
        result = (result + h * sum) / 2

    print(result, n)


def simpson_rule(left, right, func, eps):
    """
    Calculates the definite integral of a function between left and right limits
    using Simpson's rule with a given precision.
    """
    n = 2  # start with two intervals
    h = (right - left) / n
    prev_result = 0
    result = h / 3 * (func(left) + 4 * func((left + right) / 2) + func(right))
    while abs(result - prev_result) > eps:
        prev_result = result
        n *= 2
        h = (right - left) / n
        x = [left + i * h for i in range(n + 1)]
        y = [func(x[i]) for i in range(n + 1)]
        result = h / 3 * sum([y[0] + 4 * y[i] + 2 * y[i+1] + y[n] for i in range(1, n, 2)])

    print(result, n)


rectangle_method(5, 10, f, 0.00001)
trapezoidal_rule(5, 10, f, 0.001)
simpson_rule(5, 10, f, 0.0001)
