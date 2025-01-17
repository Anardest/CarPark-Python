from database import *
from services import *
import abc


class CommandFactory:
    '''
    Родитель для классов. Имеет в себе экземпляры классов с командами и абстрактный метод,
    для простоты вызова команд. Благодаря этому классу не нужно каждый раз прописывать контекст.
    Нужен для регистрации команд в словарь commands.

    Для регистрации команд нужно:
        1) Прописать логику и действие команды в отдельном файле
        2) Добавить новый класс - наследник CommandFactory в (желательно) commands.py
        3) В классе наследнике ОБЯЗАТЕЛЬНО реализовать абстрактный метод execute
        4) В execute через self.*название сервиса*.*сам метод* вызвать его
        5) Добавить ваш новый класс в словарь commands в файле dictionaries.py
        (При желании добавить описание в command_description)
        6) Готово, теперь ваша команда есть в системе и отобразится в списке всех команд
    Пример:
    class Example(CommandFactory):
        def execute(self):
            self.example_service.example_action()
    '''
    def __init__(self):
        self.db = Database()
        self.car_service = CarService(self.db)
        self.driver_service = DriverService(self.db)
    @abc.abstractmethod
    def execute(self):
        pass