import psycopg2

import db.db_queries as queries
from db.db_config import config


class DBAdapter():
    def __init__(self):
        self.config = config
        conn = self.__create_connection()
        cursor = conn.cursor()
        cursor.execute(queries.CHECK_ROLL_EXISTS, ('roll',))
        if not cursor.fetchone()[0]:
            self.__initialize_messages()
        conn.commit()
        cursor.close()
        conn.close()

    def __create_connection(self):
        conn = psycopg2.connect(
            database=self.config['database'],
            user=self.config['user'],
            password=self.config['password'],
            host=self.config['host'],
            port=self.config['port']
        )
        return conn

    def __initialize_messages(self):
        # Connection to database
        conn = self.__create_connection()
        cursor = conn.cursor()
        cursor.execute(queries.CREATE_ROLL_TABLE)

        conn.commit()
        cursor.close()
        conn.close()

    def save_roll(self, roll):
        conn = self.__create_connection()
        cursor = conn.cursor()

        print(f'Saving roll...')
        cursor.execute(queries.INSERT_ROLL,
                       (roll.get('author'), roll.get('dices'), roll.get('diceType', 10), 'unresolved', 0, False))

        conn.commit()
        cursor.close()
        conn.close()

    def get_roll(self, author):
        result = None
        repeats = None
        conn = self.__create_connection()
        cursor = conn.cursor()

        cursor.execute(queries.GET_ROLL, (author,))
        rows = cursor.fetchone()

        if not cursor.rowcount == 0:
            result = rows[0]
            repeats = rows[1]

        conn.commit()
        cursor.close()
        conn.close()

        return result, repeats

    def see_roll(self, author):
        conn = self.__create_connection()
        cursor = conn.cursor()

        cursor.execute(queries.SEE_ROLL, (author,))

        conn.commit()
        cursor.close()
        conn.close()

    def reset_table(self):
        conn = self.__create_connection()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM ROLL')

        conn.commit()
        cursor.close()
        conn.close()
