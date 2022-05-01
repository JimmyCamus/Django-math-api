from .helpers import evaluate


def newton_rapson_method(point: float, function: str, derivate: str, epsilon: float) -> float:
    function_value = evaluate(point, function)
    derivate_value = evaluate(point, derivate)
    new_point = point - (function_value / derivate_value)

    if abs(new_point - point) < epsilon:
        return new_point

    return newton_rapson_method(new_point, function, derivate, epsilon)
