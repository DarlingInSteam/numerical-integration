import math


def f(x):
    return math.log(x) / math.sqrt(1.2 + 0.3 * x)


def rectangle_method(left, right, func, eps=0.001):
    def divide_sum(number_of_splits):
        nonlocal left, right, func
        step = (right - left) / float(number_of_splits)
        sum_in_step = sum([func(left + k * step + step/2) for k in range(0, number_of_splits)])
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


def rectangle_method_with_runge(left, right, func, eps=0.001):
    def divide_sum(number_of_splits):
        nonlocal left, right, func
        step = (right - left) / float(number_of_splits)
        sum_in_step = sum([func(left + k * step + step/2) for k in range(0, number_of_splits)])
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

        # Runge rule
        runge_sum = divide_sum(steps * 2)
        error = abs(runge_sum - second_split) / 3
        if error > eps:
            steps *= 2

    print(second_split, steps)


def simpson_method(left, right, function, epsilon):
    n = 2
    h = (right - left) / (2 * n)
    step = 0
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

    print(tmp_sum, step+1)


def simpson_method_with_runge(left, right, function, epsilon):
    n = 2
    h = (right - left) / (2 * n)
    step = 0
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

        # используем метод Рунге для уточнения результата
        double_n = 2 * n
        double_h = h / 2
        double_sum = float(function(left)) + \
                     float(function(right))

        for step in range(1, 2 * double_n):
            if step % 2 != 0:
                double_sum += 4 * float(function(left + step * double_h))
            else:
                double_sum += 2 * float(function(left + step * double_h))

        double_sum *= double_h / 3
        error = abs(tmp_sum - double_sum) / 15

        if error > epsilon:
            n *= 2
            h /= 2

    print(tmp_sum, step)


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


def trapezoidal_rule_with_runge(left, right, func, eps=0.001):
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
        
        # оценка погрешности по методу Рунге
        error = abs(result - prev_result) / 3
        
        # уменьшение шага, если погрешность больше заданной
        if error > eps:
            n *= 2
            h /= 2

    print(result, n)


rectangle_method(5, 10, f, 0.000001)
rectangle_method_with_runge(5, 10, f, 0.000001)
print('')
trapezoidal_rule(5, 10, f, 0.000001)
trapezoidal_rule_with_runge(5, 10, f, 0.000001)
print('')
simpson_method(5, 10, f, 0.0000001)
simpson_method_with_runge(5, 10, f, 0.0000001)