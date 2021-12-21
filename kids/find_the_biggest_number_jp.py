#  キッズコード　いちばんおおきいかずをみつけよう
#
#  [7, 2, 3, 8, 4] -> 8

# 　かずのりすととおおきいへんすうをつくる
# 　ループでいっこずつかくにん
# 　けっかが大きいへんすう


kazu_list = [7, 2, 3, 8, 4]
ooki = kazu_list[0]

for kazu in kazu_list:
    if ooki < kazu:
        ooki = kazu

print(ooki)
