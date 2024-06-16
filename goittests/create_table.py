from sqlite3 import Error
from connect import create_connection, database

def create_table(conn, create_table_sql):
    """ Создание таблицы из SQL-запроса """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    sql_create_projects_table = """
    CREATE TABLE IF NOT EXISTS projects (
     id integer PRIMARY KEY,
     name text NOT NULL,
     begin_date text,
     end_date text
    );
    """

    sql_create_tasks_table = """
    CREATE TABLE IF NOT EXISTS tasks (
     id integer PRIMARY KEY,
     name text NOT NULL,
     priority integer,
     project_id integer NOT NULL,
     status Boolean default False,
     begin_date text NOT NULL,
     end_date text NOT NULL,
     FOREIGN KEY (project_id) REFERENCES projects (id)
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            # создание таблицы проектов
            create_table(conn, sql_create_projects_table)
            # создание таблицы задач
            create_table(conn, sql_create_tasks_table)
        else:
            print("Ошибка! Невозможно создать подключение к базе данных.")
