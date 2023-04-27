import time

import os


def robot(text):
    print("executing command")
    command = 'espeak --stdin "' + text + '" | aplay -D plughw:2,0 '
    os.system(command)
    return command


if __name__ == '__main__':
    while True:

        try:
            print("initializing")
            command = robot("Hello world how are you doing today?")
            print(command)
            time.sleep(10)
        except KeyboardInterrupt:
            break

    time.sleep(1)
