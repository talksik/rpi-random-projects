import os


def robot(text):
    print("executing command")
    os.system("espeak -w output.wav \"" + text + "\"")
    os.system("aplay -D plughw:2,0 output.wav")


if __name__ == '__main__':
    robot("Hello, I am your personal assistant")
