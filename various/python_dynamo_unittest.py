from boto3.dynamodb.conditions import Key
from unittest.mock import Mock, call


class UserAccess:
    def __init__(self, users_table):
        self.users_table = users_table

    def get_users(self, ids):
        result = []
        for user_id in (ids or []):
            response = self.users_table.query(KeyConditionExpression=Key('user_id').eq(user_id))
            result += ((int(item.get('user_id')), item.get('user_name')) for item in response.get('Items'))
        return result


def test_empty_input():
    users_table = Mock()
    users = UserAccess(users_table)

    result = users.get_users(None)

    assert result == []
    assert users_table.query.call_count == 0


def test_no_such_user():
    users_table = Mock()
    users_table.query.return_value = {'Items': []}
    users = UserAccess(users_table)

    result = users.get_users([123])

    assert result == []
    assert users_table.query.call_count == 1
    assert users_table.query.call_args == call(KeyConditionExpression=Key('user_id').eq(123))


def test_valid_user():
    users_table = Mock()
    users_table.query.return_value = {'Items': [{'user_id': 123, 'user_name': 'pikachu'}]}
    users = UserAccess(users_table)

    result = users.get_users([123])

    assert result == [(123, 'pikachu')]
    assert users_table.query.call_count == 1
    assert users_table.query.call_args == call(KeyConditionExpression=Key('user_id').eq(123))


def test_multiple_users():
    users_table = Mock()
    users_table.query.side_effect = [
        {'Items': [{'user_id': 123, 'user_name': 'pikachu'}]},
        {'Items': [{'user_id': 456, 'user_name': 'eevee'}]}
    ]
    users = UserAccess(users_table)

    result = users.get_users([123, 456])

    assert result == [(123, 'pikachu'), (456, 'eevee')]
    assert users_table.query.call_count == 2
    assert users_table.query.call_args_list == [
        call(KeyConditionExpression=Key('user_id').eq(123)),
        call(KeyConditionExpression=Key('user_id').eq(456))
    ]
