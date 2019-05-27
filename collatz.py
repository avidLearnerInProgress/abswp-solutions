def collatz(num):
    if num% 2 == 0:
        print(int(num/2))
        return int(num/2)
    else:
        print(int(3 * num + 1))
        return int(3 * num + 1 )

def main(num = 100):
    x = collatz(num)
    while x != 1:
        x = collatz(x)
    

if __name__ == "__main__":
    try:
        value = int(input("Enter any integer > 0: "))
        main(value)
    except Exception as e:
        print("Invalid integer.")
    