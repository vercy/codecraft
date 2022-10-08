from boto3.dynamodb.conditions import Key
from unittest.mock import Mock, call
import pytest


class UserAccess:
    def __init__(self, users_table):
        self.users_table = users_table

    def get_users(self, ids):
        result = []
        for user_id in (ids or []):
            response = self.users_table.query(KeyConditionExpression=Key('user_id').eq(user_id))
            result += ((int(item.get('user_id')), item.get('user_name')) for item in response.get('Items'))
        return result


@pytest.mark.parametrize('user_ids, call_count, ret, args, res', [
    (None, 0, [], [], []),
    ([], 0, [], [], []),
    ([123], 1, [{'Items': []}], [call(KeyConditionExpression=Key('user_id').eq(123))], []),
    ([123], 1, [
        {'Items': [{'user_id': 123, 'user_name': 'pikachu'}]}
    ], [
        call(KeyConditionExpression=Key('user_id').eq(123))
    ], [(123, 'pikachu')]),
    ([123, 456], 2, [
        {'Items': [{'user_id': 123, 'user_name': 'pikachu'}]},
        {'Items': [{'user_id': 456, 'user_name': 'eevee'}]}
    ], [
        call(KeyConditionExpression=Key('user_id').eq(123)),
        call(KeyConditionExpression=Key('user_id').eq(456))
     ], [(123, 'pikachu'), (456, 'eevee')]),
])
def test_get_users(user_ids, call_count, ret, args, res):
    users_table = Mock()
    users_table.query.side_effect = ret
    users = UserAccess(users_table)

    result = users.get_users(user_ids)

    assert result == res
    assert users_table.query.call_count == call_count
    assert users_table.query.call_args_list == args

