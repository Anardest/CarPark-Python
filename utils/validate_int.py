
def validate_integer(input_value, field_name):
    """
    Проверяет, можно ли преобразовать входное значение в целое число.
    Возвращает преобразованное значение или вызывает исключение ValueError.
    :param input_value: Значение, которое нужно проебразовать
    :param field_name: Имя поля, для отображения в ошибке

    :exception ValueError: Ошибка: поле filed_name должно быть целым числом.

    """
    try:
        return int(input_value)
    except ValueError:
        print(f"Ошибка: поле '{field_name}' должно быть целым числом.")
        raise  # Прерывает выполнение и передает исключение дальше