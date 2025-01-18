from commands import *
from utils.pagination import display_commands

def main():
    '''
    Точка входа в программу с основным циклом, для выбора команды из словаря commands
    '''
    while True:
        user_input = input("Введите команду или 'help' для списка команд: ").strip()
        if user_input.startswith("help"):
            parts = user_input.split()
            if len(parts) == 2 and parts[1].isdigit():
                display_commands(page=int(parts[1]))
            else:
                display_commands(page=1)  # По умолчанию страница 1
        elif user_input == "exit":
            print("Выход из приложения.")
            break
        elif user_input in commands:
            commands[user_input].execute()
        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")


if __name__ == "__main__":
    main()