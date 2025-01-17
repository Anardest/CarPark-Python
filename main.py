from commands import *

def main():
    '''
    Точка входа в программу с основным циклом, для выбора команды из словаря commands
    '''
    while True:
        command = input("Введите команду (или 'help' для списка команд): ")
        if command == "help":
            print("Доступные команды:")
            for cmd, desc in command_descriptions.items():
                print(f"{cmd}: {desc}")
        elif command == "exit":
            print("Завершение работы")
            break
        elif command in commands:
            commands[command].execute()
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()