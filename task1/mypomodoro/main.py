# main.py （修正版，重點在 choice '3' 部分）

from datetime import datetime
import threading
import time
import sys

from pomodorothread import PomodoroThread   # 假設已存在
from schedule import ScheduleManager

# 全域 manager（整個程式共用一個日程表）
manager = ScheduleManager()


def print_menu():
    print('\n---hi user---')
    print('1. start Pomodoro (Default 25min + 5min + 4 rounds)')
    print('2. start Custom Pomodoro')
    print('3. Add event')
    print('4. View calendar')
    print('5. Exit')
    return input('> ').strip()


def add_event():
    print("\n--- 新增事件 ---")
    try:
        title = input("要做什麼？ (事件名稱): ").strip()
        if not title:
            print("事件名稱不能空白")
            return

        year   = int(input("年份 (e.g. 2026): "))
        month  = int(input("月份 (1-12): "))
        day    = int(input("日期 (1-31): "))
        hour   = int(input("開始小時 (0-23): "))
        minute = int(input("開始分鐘 (0-59): "))
        duration = int(input("持續時間 (分鐘): "))

        start_dt = datetime(year, month, day, hour, minute)

        # 直接用全域的 manager 實例
        manager.add_event_by_details(title, start_dt, duration)
        print("事件新增成功！")

    except ValueError as e:
        print(f"輸入錯誤：{e}")
        print("請輸入有效數字，並確保日期/時間合理（例如沒有 2 月 30 日）")
    except Exception as e:
        print(f"發生錯誤：{e}")


def main():
    print("歡迎使用 日程表 + 番茄鐘 工具")
    
    while True:
        choice = print_menu()

        if choice == '1':
            thread = PomodoroThread(25*60, 5*60, 4)
            thread.start()
            thread.join()

        elif choice == '2':
            try:
                work_min = int(input("專注時間 (分鐘): "))
                break_min = int(input("休息時間 (分鐘): "))
                rounds = int(input("回合數: "))
                thread = PomodoroThread(work_min*60, break_min*60, rounds)
                thread.start()
                thread.join()
            except ValueError:
                print("請輸入有效數字！")

        elif choice == '3':
            add_event()               # ← 呼叫獨立函數

        elif choice == '4':
            manager.show_all_events()

        elif choice in ('5', 'q', 'exit'):
            print("再見！")
            break

        else:
            print("無效選擇，請輸入 1-5")


if __name__ == '__main__':
    main()
