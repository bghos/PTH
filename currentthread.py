import threading
import time
import datetime
# import datemath

complete = False


def Worker(Text: str):
    counter = 0
    while not complete:
        time.sleep(1)
        counter +=1
        print(f"{Text}:{counter}")


# Worker()

threading.Thread(target=Worker,daemon=True,args=("ABC",)).start()
threading.Thread(target=Worker,daemon=False,args=("DEF",)).start()

input('press enter to exit')
complete = True