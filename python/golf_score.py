import sys

# .strip() を使うことで、不要な改行や空白を削除 できる。
# sys.stdin.readline()で指定したファイルの中身を一行ずつ取得する
line1 = sys.stdin.readline().strip()
required_at_bats = [int(x) for x in line1.split(",")]
print(required_at_bats)
line2 = sys.stdin.readline().strip()
player_at_bats = [int(x) for x in line2.split(",")]
print(player_at_bats)
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
score_dict = {
    -4: "コンドル",
    -3: "アルバトロス",
    -2: "イーグル",
    -1: "バーディ",
    0: "パー",
    1: "ボギー"
}

for required, player in zip(required_at_bats, player_at_bats):
    diff = player - required
    if required == 4 and player == 1:
        score_result.append("ホールインワン")
    elif diff >= 2:
        score_result.append(f"{diff}ボギー")
    elif diff in score_dict:
        score_result.append(score_dict[diff])

print(", ".join(score_result))
