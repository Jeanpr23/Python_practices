import sqlite3
import os
from datetime import date

DATABASE_PATH = "database/users.db"

def reset_daily_usage(user_id):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    today = str(date.today())

    cursor.execute(
        """
        SELECT last_reset
        FROM users
        WHERE discord_id = ?
        OR visitor_id = ?
        """,
        (
         user_id,
         user_id
        )
    )

    result = cursor.fetchone()

    if result:

        last_reset = result[0]

        if last_reset != today:

            cursor.execute(
                """
                UPDATE users
                SET
                manipulation_uses = 0,
                saturation_uses = 0,
                last_reset = ?
                WHERE discord_id = ?
                OR visitor_id = ?

                """,
                (
                    today,
                    user_id,
                    user_id
                )
            )

    connection.commit()
    connection.close()

def can_use(user_id, feature):

    reset_daily_usage(user_id)


    user = get_user(user_id)

    if not user:
        return False

    # Premium
    if user[4] == 1:
        return True

    if feature == "manipulation":

        return user[5] < 5

    if feature == "saturation":

        return user[6] < 5

    return False

def add_usage(user_id, feature):

    connection = sqlite3.connect(
        DATABASE_PATH

    )

    cursor = connection.cursor()

    if feature == "manipulation":

        cursor.execute(
            """
            UPDATE users 
            SET manipulation_uses = manipulation_uses + 1
            WHERE discord_id = ?
            OR visitor_id = ?
            """,
            (
                user_id,
                user_id

            )
        )

    if feature == "saturation":

        cursor.execute(
            """
            UPDATE users
            SET saturation_uses = saturation_uses + 1
            WHERE discord_id = ?
            OR visitor_id = ?
            """,
            (
                user_id,
                user_id
            )
        )

    connection.commit()

    connection.close()

def create_database():

    os.makedirs(
        "database",
        exist_ok=True
    )

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,

        discord_id TEXT,

        visitor_id TEXT,

        username TEXT,

        premium INTEGER DEFAULT 0,

        manipulation_uses INTEGER DEFAULT 0,

        saturation_uses INTEGER DEFAULT 0,

        last_reset TEXT

   )
   """)

    connection.commit()

    connection.close()


def get_user(user_id):


    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE discord_id = ?
        OR visitor_id = ?
        """,
        (
            user_id,
            user_id
        )
    )


    user = cursor.fetchone()

    connection.close()

    return user

def create_user(discord_id=None, username=None, visitor_id=None):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR IGNORE INTO users
        (
            discord_id,
            visitor_id,
            username,
            last_reset

        )
        VALUES (?, ?, ?, date('now'))
        """,

        (

            discord_id,
            visitor_id,
            username
        )
    )


    connection.commit()

    connection.close()

def is_premium(user_id):

    user = get_user(user_id)

    if user:

        return user[4] == 1

    return False


def get_usage(user_id, feature):

    reset_daily_usage(user_id)

    user = get_user(user_id)


    if not user:

        return 0

    if feature == "manipulation":

        return user[5]

    if feature == "saturation":

        return user[6]

    return 0