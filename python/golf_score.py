import sys

# .strip() を使うことで、不要な改行や空白を削除 できる。
# sys.stdin.readline()で指定したファイルの中身を一行ずつ取得する
line1 = line1 = sys.stdin.readline().strip() 
required_at_bats = [int(x) for x in line1.split(",")]

line2 = sys.stdin.readline().strip()
player_at_bats = [int(x) for x in line2.split(",")]

# 取得したリストのデータを空のリストに入れ直す

# 規定打数よりも1多ければボギー
# ダブルボギー以上の場合は2 ボギー,3 ボギーのようにオーバーした数をオギーの前につける
# 規定打数ちょうどの場合パー
# 規定打数より1少なければバーディ
# 規定打数よりも2少なければイーグル
# 規定打数4で1打で入れた場合ホールインワン
# 規定打数5でプレイヤーの打数が2打の場合アルバトロス
# 規定打数5でプレイヤーの打数が1の場合コンドル

score_result = []
for required, player in zip(required_at_bats, player_at_bats):
    if required == 5 and player == 2:
        score_result.append("アルバトロス")
    elif required == 5 and player == 1:
        score_result.append("コンドル")
    elif required <= 4 and player == 1:
        score_result.append("ホールインワン")
    elif required - player == 2:
        score_result.append("イーグル")
    elif required - player == 1:
        score_result.append("バーディ")
    elif required == player:
        score_result.append("パー")
    elif player - required == 1:
        score_result.append("ボギー")
    elif player - required >= 2:
        score_result.append(f"{player - required} ボギー")

print(", ".join(score_result))
