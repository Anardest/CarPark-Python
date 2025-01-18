from database.database import Database
from utils import *

class TripService:
    def __init__(self, db : Database):
        self.db = db
    def add_trip(self):
        """
            Добавляет поездку в таблицу trips с проверкой наличия машины и водителя.
        """

        # Ввод от пользователя
        car_id = input("Введите Id автомобиля: ")
        driver_id = input("Введите Id водителя: ")
        distance = input("Введите длину поездки: ")
        date = input("Введите дату поездки в формате: yyyy-mm-dd: ")

        # Валидация
        validate = [car_id,driver_id,distance]
        validate = validate_array_integer(validate)
        if validate is None:
            return
        # Валидация даты
        date = validate_date_string(date)
        if date is None:
            return
        car_exists = record_exists(self.db, "cars", car_id)
        driver_exists = record_exists(self.db, "drivers", driver_id)

        # Если такой автомобиль и водитель есть в БД, то добавляем поездку, иначе - ошибка
        if car_exists & driver_exists:
            self.db.execute('''
            INSERT INTO trips (car_id, driver_id, distance, date)
            VALUES(?,?,?,?)
            ''', (car_id, driver_id, distance, date))
            print("Поездка успешно добавлена!")
        else:
            print("Ошибка: таких данных нет в базе!")

    def show_all_trips(self):
        trips = self.db.fetchall('SELECT * FROM trips')
        if trips:
            for trip in trips:
                print(
                    f"Id поездки: {trip[0]}, Id авто: {trip[1]}, Id водителя: {trip[2]}, Длина: {trip[3]}, км, Дата: {trip[4]}")
        else:
            print("Нет доступных поездок")


