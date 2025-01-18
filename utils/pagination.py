from commands.dictionaries import *


def display_commands(page=1, commands_per_page=5):
    '''
    Нужна для пагинации списка команд.
    :param page: Первая отображаемая страница по умолчанию (по умолчанию 1)
    :param commands_per_page: Количество команд на страницу (по умолчанию 5)
    '''

    # Преобразуем команды в список пар (ключ, описание)
    command_list = list(command_descriptions.items())
    total_pages = (len(command_list) + commands_per_page - 1) // commands_per_page

    # Проверяем, что страница в допустимом диапазоне
    if page < 1 or page > total_pages:
        print(f"Страница {page} не существует. Укажите от 1 до {total_pages}.")
        return

    # Определяем команды для текущей страницы
    start_index = (page - 1) * commands_per_page
    end_index = start_index + commands_per_page
    page_commands = command_list[start_index:end_index]

    # Выводим команды
    print(f"Страница {page}/{total_pages}")
    for command, description in page_commands:
        print(f"    {command} - {description}")

    # Подсказка для переключения страниц
    print("\nВведите 'help <номер страницы>' для перехода или 'exit' для выхода.")
    print("")