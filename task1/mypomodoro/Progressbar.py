
import time
import sys

CLEAR_TO_END = '\033[K'  

def time_format(seconds):
    return time.strftime('%M:%S', time.gmtime(seconds))
#秒轉分鐘  用於下部分


def progress_bar(remaining, total):
    sys.stdout.write(f'\r{CLEAR_TO_END}')
    mins, secs = divmod(remaining, 60)
    sys.stdout.write(f'\r剩餘: {mins:02d}:{secs:02d} / {total//60:02d}:{total%60:02d}')
    sys.stdout.flush()
#計時用
