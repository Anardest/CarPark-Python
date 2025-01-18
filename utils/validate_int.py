
def validate_integer(input_value, field_name):
    """
    Проводит валидацию значения, проебразуя его в int
    :param input_value: Значение, которое нужно проебразовать
    :param field_name: Имя поля, для отображения в ошибке
    :return Преобразованное число, если валиден, иначе None

    :exception ValueError: Ошибка: поле filed_name должно быть целым числом.

    """
    try:
        return int(input_value)
    except ValueError:
        print(f"Ошибка: поле '{field_name}' должно быть целым числом.")
        return None # Прерывает выполнение и передает исключение дальше

def validate_array_integer(input_array):
    '''
    Проводит валидацию каждого элемента массива, преобразуя всё в int.

    :param input_array: Список элементов для проверки
    :return: Преобразованный массив, если все элементы валидны, иначе None
    '''
    converted_array = []
    for element in input_array:
        try:
            converted_element = int(element)
            converted_array.append(converted_element)
        except ValueError:
            print(f"Ошибка: элемент '{element}' не является целым числом")
            return None
    return converted_array
