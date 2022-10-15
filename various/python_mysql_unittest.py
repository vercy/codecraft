import json
import mysql.connector
from unittest.mock import Mock, call


class UserAccess:
    def __init__(self, my_sql: mysql.connector.MySQLConnection):
        self.my_sql = my_sql

    def get_users(self, ids):
        if not ids:
            return []

        cursor = self.my_sql.cursor()
        # language=sql
        cursor.execute("select user_id, user_name from users where user_id member of(%s)",
                       [json.dumps(ids)])
        return [(user_id, user_name) for user_id, user_name in cursor.fetchall()]


def test_empty_input():
    my_sql = Mock()

    users = UserAccess(my_sql)
    result = users.get_users(None)

    assert result == []
    assert my_sql.cursor.call_count == 0


def test_no_such_user():
    my_sql = Mock()
    cursor = Mock()
    my_sql.cursor.return_value = cursor

    cursor.fetchall.return_value = []

    users = UserAccess(my_sql)
    result = users.get_users([123])

    assert result == []
    assert my_sql.cursor.call_count == 1
    assert cursor.execute.call_count == 1
    assert cursor.execute.call_args == call(
        "select user_id, user_name from users where user_id member of(%s)",
        ['[123]']
    )
    assert cursor.fetchall.call_count == 1


def test_existing_user():
    my_sql = Mock()
    cursor = Mock()
    my_sql.cursor.return_value = cursor

    cursor.fetchall.return_value = [(123, 'pikachu')]

    users = UserAccess(my_sql)
    result = users.get_users([123])

    assert result == [(123, 'pikachu')]
    assert my_sql.cursor.call_count == 1
    assert cursor.execute.call_count == 1
    assert cursor.execute.call_args == call(
        "select user_id, user_name from users where user_id member of(%s)",
        ['[123]']
    )
    assert cursor.fetchall.call_count == 1


def test_multiple_users():
    my_sql = Mock()
    cursor = Mock()
    my_sql.cursor.return_value = cursor

    cursor.fetchall.return_value = [(123, 'pikachu'), (456, 'eevee')]

    users = UserAccess(my_sql)
    result = users.get_users([123, 456])

    assert result == [(123, 'pikachu'), (456, 'eevee')]
    assert my_sql.cursor.call_count == 1
    assert cursor.execute.call_count == 1
    assert cursor.execute.call_args == call(
        "select user_id, user_name from users where user_id member of(%s)",
        ['[123, 456]']
    )
    assert cursor.fetchall.call_count == 1
