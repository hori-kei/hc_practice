import datetime
import sys


# sys.argvはコマンドをターミナルで打ったときにそれをリストで返してくれる
# 例えばpython3 calendar.py -m 3 → ["calendar.py", "-m", "3"]
# だから今回の制作課題の場合[0]にファイル名,[1]にオプション,[2]に月を選択する。このようになる。
def get_year_month():
    """ ターミナルで記述されたものから年・月を取得する """
    # 引数なし → 現在の年月を取得
    if len(sys.argv) == 1: # つまりターミナルでpython calendar.pyとしたとき
        today = datetime.date.today() # 今日の年、月、日を取得 →例)2025-02-26
        return today.year, today.month #年と月を返す

    # `-m` オプションがある場合
    if len(sys.argv) == 3 and sys.argv[1] == "-m":
        month = int(sys.argv[2])  # 文字列を整数に変換
        try:
            if 1 <= month <= 12:
                today = datetime.date.today()
                return today.year, month
            else:
                print(f"{month} is neither a month number (1..12) nor a name")
                sys.exit(1)  # sys.exit(1) は Python プログラムを終了させる ための命令で、sys モジュールに含まれている
        except ValueError:
            print(f"{sys.argv[2]} is neither a month number (1..12) nor a name")
            sys.exit(1)  # sys.exit(1) は Python プログラムを終了させる ための命令で、sys モジュールに含まれている


def get_calendar(year, month):  # ここのyearとmonthにはget_year_monthでreturnした値が入る
    """ 指定された年月のカレンダーを表示する """

    # 1. ヘッダー部分を出力
    print(f"{month}月 {year}".center(20))  # 年月を中央寄せ
    print("月 火 水 木 金 土 日")  # 月曜始まり

    # 2. その月の 1日が何曜日かを取得（0: 月曜, 6: 日曜）
    first_day = datetime.date(year, month, 1)
    start_weekday = first_day.weekday()

    # 3. 月の最終日を求める
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)

    last_day = (next_month - datetime.timedelta(days=1)).day  # 最終日を取得

    # 4. カレンダーの表示用データを作成
    empty_slots = ["   "] * start_weekday  # 1日の前に空白を入れる

    day_slots = []
    for day in range(1, last_day + 1):
    # 各日を2桁で表示し、右側にスペースを1マス追加する（例：" 1 "、"28 "）
        day_slots.append(f"{day:2} ")

    # 空白部分と日付部分を結合して、全体のカレンダーのリストを作る
    calendar_entries = empty_slots + day_slots

    # リストを7個ずつ（1週間分）に分け、各行として出力する
    for i in range(0, len(calendar_entries), 7):
        week_entries = calendar_entries[i: i + 7]
        week_line = "".join(week_entries)
        print(week_line)


# メイン処理
if __name__ == "__main__":
    year, month = get_year_month()
    get_calendar(year, month)

