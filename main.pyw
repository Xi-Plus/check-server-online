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
    winsound.Beep(2000, 250)
    time.sleep(0.25)
    winsound.Beep(2000, 250)
    time.sleep(0.25)
    winsound.Beep(2000, 250)


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
        beeps()
        msg = 'The server is down: {}'.format(e)
        write_log(msg)
        ctypes.windll.user32.MessageBoxW(0, msg, 'Error', 0)

    time.sleep(args.sleep)
