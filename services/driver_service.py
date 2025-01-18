from database.database import Database
from utils.validate_int import validate_array_integer


class DriverService:
    def __init__(self, db : Database):
        self.db = db

    def add_driver(self):
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        age = input("Введите возраст: ")
        experience = input("Введите стаж: ")


        # Валидация
        validate = [age, experience]
        validate = validate_array_integer(validate)
        if validate is None:
            return


        self.db.execute('''
        INSERT INTO drivers (name, surname, age, experience)
        VALUES(?,?,?,?)
        ''', (name,surname,age,experience))
        print("Водитель успешно добавлен!")

    def delete_driver(self):
        driver_id = input("Введите Id водителя: ")

        # Валидация
        validate = [driver_id]
        validate = validate_array_integer(validate)
        if validate is None:
            return

        self.db.execute('''
                DELETE FROM drivers
                WHERE id = ?
                ''', (driver_id,))
        print("Водитель успешно удалён")

    def show_all_drivers(self):
        drivers = self.db.fetchall('SELECT * FROM drivers')
        if drivers:
            for driver in drivers:
                print(f"Id: {driver[0]}, Имя: {driver[1]}, Фамилия: {driver[2]}, Возраст: {driver[3]}, Стаж: {driver[4]}")
        else:
            print("Нет доступных водителей")

    def show_driver_by_id(self):
        driver_id = input("Введите Id водителя: ")

        # Валидация
        validate = [driver_id]
        validate = validate_array_integer(validate)
        if validate is None:
            return

        driver = self.db.fetchone('SELECT * FROM drivers WHERE id = ?', (driver_id))
        if driver:
            print("Водитель найден")
            print(f"Id: {driver[0]}")
            print(f"Имя: {driver[1]}")
            print(f"Фамилия: {driver[2]}")
            print(f"Возраст: {driver[3]}")
            print(f"Стаж: {driver[4]}")
        else:
            print("Водитель с таким Id не найден")
