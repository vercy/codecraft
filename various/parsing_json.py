import json


in_json = \
    '[\
        {"error": {"cause": "TooManyRequests", "status": 500}},\
        {"attack": 55 , "name": "Eevee", "hp": 55},\
        {},\
        {"error": {"cause": "GOAWAY", "status": 429}},\
        {"error": {"cause": "no such pokemon: \'Gardevr\'", "status": 400}},\
        {"attack": 55, "name": "Pikachu"}\
    ]'


def parse_attacks(js):
    attacks = json.loads(js)
    correctable = [a['error']['cause'] for a in attacks if a.get('error', {}).get('status') == 400]
    if correctable:
        raise RuntimeError(f'Please fix your query: {correctable}')

    def is_throttled(a):
        e = a.get('error', {})
        return not a.get('attack') or e.get('status') == 429 or e.get('cause') == 'TooManyRequests'

    if any(is_throttled(a) for a in attacks):
        raise RuntimeError('The server is busy, please try again later')

    return [a['attack'] for a in attacks]


print(parse_attacks(in_json))
