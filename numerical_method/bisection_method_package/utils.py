from .helpers import evaluate, calculate_mid_point


def bisection_method(min: float, max: float, epsilon: float, expression: str) -> float:
    mid_point = calculate_mid_point(min, max)
    if evaluate(min, expression) * evaluate(mid_point, expression) < 0:
        return determine_solution(min, mid_point, mid_point, epsilon, expression)

    return determine_solution(mid_point, max, mid_point, epsilon, expression)


def determine_solution(new_min: float, new_max: float, mid_point: float, epsilon: float, expression: str) -> float:
    new_mid_point = calculate_mid_point(new_min, new_max)
    if abs(new_mid_point - mid_point) < epsilon:
        return new_mid_point
    return bisection_method(new_min, new_max, epsilon, expression)
