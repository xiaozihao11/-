 2023/12/25 12:21:25


 21:24:59
import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        print(f"Remaining time: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time up! Your focus session has ended.")

if __name__ == "__main__":
    minutes = int(input("Enter the duration of your focus session in minutes: "))
    countdown(minutes)

