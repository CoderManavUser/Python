import time
def countdown(num):
    if num==0:
        print("T-Minus 0...BLAST! Enjoy your Day in Space")
    else:
        print(num)
        print("*"* num)
        time.sleep(1)
        countdown(num-1)

n=int(input("Enetr your Limit for Space Revolution:"))
countdown(n)
