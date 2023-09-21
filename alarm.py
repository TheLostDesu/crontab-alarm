from playsound import playsound
import threading

def ask_sum_question(a, b):
    print(f"{a} + {b} = ?")
    while True:
        ans = input()
        if ans.isdigit():
            ans = int(ans)
        
        if(ans == a + b):
            break
        


def loopSound():
    while True:
        playsound("alarm.wav", block=True)


loopThread = threading.Thread(target=loopSound, name='alarm')
loopThread.daemon = True
loopThread.start()

ask_sum_question(1, 1)