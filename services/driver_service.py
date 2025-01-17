from database.database import Database
from utils.validate_int import validate_integer


# TODO: отобразить всех, поиск по Id
class DriverService:
    def __init__(self, db : Database):
        self.db = db

    def add_driver(self):
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        age = input("Введите возраст: ")
        experience = input("Введите стаж: ")

        # Валидация
        validate_integer(age, "Возраст")
        validate_integer(experience, "Стаж")

        self.db.execute('''
        INSERT INTO drivers (name, surname, age, experience)
        VALUES(?,?,?,?)
        ''', (name,surname,age,experience))
        print("Водитель успешно добавлен!")

    def delete_driver(self):
        driver_id = input("Введите Id водителя: ")

        # Валидация
        validate_integer(driver_id, "Id водителя")

        self.db.execute('''
                DELETE FROM drivers
                WHERE id = ?
                ''', (driver_id,))
        print("Водитель успешно удалён")

    def show_all_drivers(self):
        drivers = self.db.fetchall('SELECT * FROM drivers')
        if drivers:
            for driver in drivers:
                print(driver)
        else:
            print("Нет доступных водителей")

    def find_driver(self):
        driver = self.db.fetchall('SELECT * FROM drivers')