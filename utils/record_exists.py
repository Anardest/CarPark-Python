from database import Database
def record_exists(db : Database, table, record_id):
    """
        Проверяет, существует ли запись с указанным id в таблице.

        :param db: Класс базы данных.
        :param table: Название таблицы (строка).
        :param record_id: ID записи (целое число).
        :return: True, если запись существует, иначе False.
    """
    return db.fetchone(f"SELECT 1 FROM {table} WHERE id = ?", (record_id,)) is not None