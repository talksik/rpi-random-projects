import time

import os


def robot(text):
    os.system("espeak ' " + text + " ' ")


if __name__ == '__main__':
    while True:

        try:
            robot("Hello world how are you doing today?")
            time.sleep(5)
        except KeyboardInterrupt:
            break

    time.sleep(1)
