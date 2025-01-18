from commands.commands import *
from commands.commands import ShowAllDrivers

commands = {
    "add_driver": AddDriver(),
    "delete_driver": DeleteDriver(),
    "add_car": AddCar(),
    "delete_car": DeleteCar(),
    "show_all_cars": ShowAllCars(),
    "show_all_drivers": ShowAllDrivers(),
    "show_driver_by_id": ShowDriverById(),
}
command_descriptions = {
    "exit": "Закрыть приложение",
    "add_driver": "Добавить нового водителя",
    "delete_driver": "Удалить водителя",
    "add_car": "Добавить новый автомобиль",
    "delete_car": "Удалить автомобиль",
    "show_all_cars": "Вывести список всех автомобилей",
    "show_all_drivers": "Вывести список всех водителей",
    "show_driver_by_id": "Вывести водителя через его Id",
    "show_car_by_id": "Вывести автомобиль через его Id"
}