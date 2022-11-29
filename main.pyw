import argparse
import ctypes
import os
import requests
import time
import winsound

BASEDIR = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('url')
parser.add_argument('--sleep', type=int, default=60)
args = parser.parse_args()


def beeps():
    for i in range(5):
        if i > 0:
            time.sleep(0.5)
        winsound.Beep(2000, 500)


log_path = os.path.join(BASEDIR, 'run.log')


def write_log(msg):
    with open(log_path, 'a') as f:
        f.write('{} [{}] {}\n'.format(time.ctime(), os.getpid(), msg))


write_log('start {}'.format(args.url))

while True:
    try:
        res = requests.get(args.url)
        write_log('touch')
    except Exception as e:
        msg = 'The server is down: {}'.format(e)
        write_log(msg)
        beeps()
        ctypes.windll.user32.MessageBoxW(0, msg, 'Error', 0)

    time.sleep(args.sleep)
