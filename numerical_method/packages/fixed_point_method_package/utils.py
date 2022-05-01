from .helpers import evaluate


def fixed_point_method(point: float, epsilon: float, expression: str) -> float or int:
    next_point = evaluate(point, expression)
    if abs(next_point - point) <= epsilon:
        return next_point
    return fixed_point_method(next_point, epsilon, expression)
