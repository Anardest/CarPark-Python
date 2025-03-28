from database.database import Database
from utils.validate_int import validate_array_integer

class CarService:
    '''
    Отвечает за взаимодействие с автомобилями в рамках класса Database
    '''
    def __init__(self, db : Database):
        self.db = db

    def add_car(self):
        '''
        Добавляет автомобиль в БД
        :raise ValueError: d

        '''
        brand = input("Введите марку авто: ")
        model = input("Введите модель: ")
        year = input("Введите год производства: ")
        mileage = input("Введите пробег: ")

        # Валидация данных
        # Валидация
        validate = [year]
        validate = validate_array_integer(validate)
        if validate is None:
            return

        # Вставка данных в БД, с автоматическим сохранением
        self.db.execute('''
    INSERT INTO cars (brand, model, year, mileage)
    VALUES(?,?,?,?)
    ''', (brand, model, year, mileage))
        print("Данные успешно сохранены")

    # Удаление авто из БД
    def delete_car(self):
        '''
        Удаляет автомобиль из БД
        '''
        car_id = input("Введите Id автомобиля: ")

        # Валидация
        validate = [car_id]
        validate = validate_array_integer(validate)
        if validate is None:
            return

        self.db.execute('''
        DELETE FROM cars
        WHERE id = ?
        ''', (car_id,))
        print("Автомобиль успешно удалён")

    # Вывести все авто
    def show_all_cars(self):
        cars = self.db.fetchall('SELECT * FROM cars')
        if cars:
            for car in cars:
                print(f"Id: {car[0]}, Марка: {car[1]}, Модель: {car[2]}, Год выпуска: {car[3]}, Пробег: {car[4]}")
        else:
            print("Нет доступных автомобилей")

    # Вывести авто по его Id
    def show_car_by_id(self):
        car_id = input("Введите Id автомобиля: ")

        # Валидация
        validate = [car_id]
        validate = validate_array_integer(validate)
        if validate is None:
            return

        car = self.db.fetchone('SELECT * FROM cars WHERE id = ?',(car_id))
        if car:
            print("Автомобиль найден")
            print(f"Id: {car[0]}")
            print(f"Марка: {car[1]}")
            print(f"Модель: {car[2]}")
            print(f"Год выпуска: {car[3]}")
            print(f"Пробег: {car[4]}")
        else:
            print("Автомобиль с таким Id не найден")