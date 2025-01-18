from datetime import datetime

def validate_date_string(date_string, date_format="%Y-%m-%d"):
    """
        Проверяет, соответствует ли строка формату даты.

        :param date_string: Строка с датой для проверки.
        :param date_format: Ожидаемый формат даты (по умолчанию: "%Y-%m-%d").
        :return: Возвращает строку, если формат корректный; иначе None.
    """
    try:
        datetime.strptime(date_string, date_format)
        return date_string
    except ValueError:
        print(f"Ошибка: поле '{date_string}' должно быть в формате {date_format}.")
        return None