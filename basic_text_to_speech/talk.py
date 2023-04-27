import time

from subprocess import call


def robot(text):
    print("executing command")
    call(['espeak', '--stdin', '"Hello world how are you doing today?"', '|', 'aplay', '-D', 'plughw:2,0'])


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
