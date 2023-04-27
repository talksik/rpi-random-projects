import time

from subprocess import Popen, PIPE


def robot(text):
    print("executing command")
    espeak = Popen(
        ['espeak', '--stdin "Hello world how are you doing today?"'], stdout=PIPE)
    aplay = Popen(['aplay', '-D plughw:2,0'], stdin=espeak.stdout, stdout=PIPE)
    espeak.stdout.close()  # enable write error in dd if ssh dies
    out, err = aplay.communicate()


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
