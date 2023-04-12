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

    while abs(first_split - second_split) > eps:
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
        sum *= 2
        sum += (func(left) + func(right))
        prev_result = result
        result = (h * sum) / 2

    print(result, n)


def simpson_method(left, right, function, epsilon):
    n = 2
    h = (right - left) / (2 * n)

    prev_sum = 0
    tmp_sum = float(function(left)) + \
              float(function(right))

    while abs(tmp_sum - prev_sum) > epsilon:
        prev_sum = tmp_sum
        tmp_sum = float(function(left)) + \
                  float(function(right))

        for step in range(1, 2 * n):
            if step % 2 != 0:
                tmp_sum += 4 * float(function(left + step * h))
            else:
                tmp_sum += 2 * float(function(left + step * h))

        tmp_sum *= h / 3
        n *= 2
        h /= 2

    print(tmp_sum, step)



rectangle_method(5, 10, f, 0.00001)
trapezoidal_rule(5, 10, f, 0.000001)
simpson_method(5, 10, f, 0.000000001)
