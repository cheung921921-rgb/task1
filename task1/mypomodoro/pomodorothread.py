import threading
import time
import Progressbar

class PomodoroThread(threading.Thread):
    def __init__(self, work_seconds, break_seconds,round):
        super().__init__()
        self.work_seconds = work_seconds
        self.break_seconds = break_seconds
        self.round = round
        self.daemon = True  # 主程式結束時自動關閉 thread

    def run(self):
        for i in range(self.round,0,-1):                              #回合
            
            print("目前是第"+str(i) +"輪" )                           
            print(f"\n開始專注：{Progressbar.time_format(self.work_seconds)}")
            
            for i in range(self.work_seconds, 0, -1):                  #工作時間
                Progressbar.progress_bar(i, self.work_seconds)
                time.sleep(1)
            
            print("\n時間到！休息開始...")                              #休息時間
            for i in range(self.break_seconds, 0, -1):
                Progressbar.progress_bar(i, self.break_seconds)
                time.sleep(1)
            
            print("\n休息結束！")
#蕃茄鐘
