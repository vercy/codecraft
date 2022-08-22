
colors = [
    ('White', '255', '255', '255'),
    ('Silver', '192', '192', '192'),
    ('Gray', '128', '128', '128'),
    ('Black', '0', '0', '0'),
    ('Red', '255', '0', '0'),
    ('Maroon', '128', '0', '0'),
    ('Yellow', '255', '255', '0'),
    ('Olive', '128', '128', '0'),
    ('Lime', '0', '255', '0'),
    ('Green', '0', '128', '0'),
    ('Aqua', '0', '255', '255'),
    ('Teal', '0', '128', '128'),
    ('Blue', '0', '0', '255'),
    ('Navy', '0', '0', '128'),
    ('Fuchsia', '255', '0', '255'),
    ('Purple', '128', '0', '128'),
]


# def get_reds(lst):
#     result = dict()
#     for row in lst:
#         color_name = row[0]
#         r = int(row[1])
#         g = int(row[2])
#         b = int(row[3])
#         if r > 0:
#             result[color_name] = f'#{r:02x}{g:02x}{b:02x}'
#     return result
#
#
# red_blends = get_reds(colors)

red_blends = {name: f'#{int(r):02x}{int(g):02x}{int(b):02x}' for name, r, g, b in colors if int(r) > 0}

for name, code in red_blends.items():
    print(f'{name} -> {code}')

print('Test')

print(f'Red -> {red_blends.get("Red")}')
print(f'Blue -> {red_blends.get("Blue")}')
print(f'White -> {red_blends.get("White")}')
