import sqlite3

class Database:
    '''
    Служит для действий с БД: Создание таблицы, запросы и т.д.
    '''
    def __init__(self, db_name="database/carpark.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_tables()

    def _create_tables(self):
        '''
        Отвечает за создание (Если их нет) таблиц в баз данных.
        Создаёт в БД 3 сущности:
        1. Сущность - "Машины" cars, хранит данные об автомобилях
        2. Сущность - "Водитель" drivers, хранит данные о водителях
        3. Сущность - "Поездки" trips, хранит внешние ключи водителя, автомобиля и данные о поездке
        :return:
        '''
        # Включение поддержки внешних ключей
        self.cursor.execute('PRAGMA foreign_keys = ON')

        # Создание сущности - "Машины"
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER NOT NULL
        )
        ''')

        # Создание сущности - "Водители"
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS drivers(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            age INTEGER NOT NULL,
            experience INTEGER NOT NULL
        )
        ''')
        # Создание сущности - "Поездки"
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS trips(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER NOT NULL,
            driver_id INTEGER NOT NULL,
            distance INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (car_id) REFERENCES cars (id) ON DELETE CASCADE,
            FOREIGN KEY (driver_id) REFERENCES drivers (id) ON DELETE CASCADE
        )
        ''')

        self.connection.commit()  # Сохранение изменений

    def execute(self, query, params=None):
        '''
        Выполняет SQL команду
        :param query: команда на языке SQL
        :param params: Параметры к зпросу
        :return:
        '''
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchall(self, query, params=None):
        '''
        Возвращает все строки результата запроса. Результат возвращается в виде списка кортежей.
        :param query: SQL запрос
        :param params: Параметры к запросу
        :return: Все строки запроса
        '''
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query, params=None):
        '''
        Возвращает одну строку результата запроса. Если строка доступна, возвращается как кортеж.
        :param query: SQL запрос
        :param params: Параметры к запросу
        :return: Одну строку результата
        '''
        if params is None:
            params = ()
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        '''
        Обрывает соединение с базой данных
        :return: None
        '''
        self.connection.close()