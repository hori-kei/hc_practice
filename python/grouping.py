import random

members = ["A", "B", "C", "D", "E", "F"]
# membersをランダムに入れ替える。
# この時新しい変数に入れ直すとNoneを返すためmembersの元の値を変更する。
random.shuffle(members)
# random.choiceでTrueかFalseを指定できるようにbool型のサブ型の1,0でリストを作る
choice = [2, 3]


def split_group():
    random_choice = random.choice(choice)
    group1 = sorted(members[:random_choice])
    group2 = sorted(members[random_choice:])

    return group1, group2


group1, group2 = split_group()
print("グループ1:", group1)
print("グループ2:", group2)
