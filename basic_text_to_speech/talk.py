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
            robot("hey Heran?")
            robot("Based on your age, health, and habits, you have 10950 days left")
            robot("Make sure you chant hare krishna more")
            time.sleep(5)

            robot("hey Kam?")
            robot("Hmm, you have time, but make sure to surrender to jesus")
            time.sleep(5)

            robot("hey Arjun")
            robot("You have maybe 12000 days left to live")
            robot("just drink some water")
            time.sleep(5)

        except KeyboardInterrupt:
            break

    time.sleep(1)
