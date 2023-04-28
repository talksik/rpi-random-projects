import time

import os


def robot(text):
    print("executing command")
    os.system("espeak -w output.wav \"" + text + "\"")
    os.system("aplay -D plughw:2,0 output.wav")


if __name__ == '__main__':
    while True:
        try:
            print("initializing")
            robot("Hello world how are you doing today?")
            time.sleep(10)
        except KeyboardInterrupt:
            break

    time.sleep(1)
