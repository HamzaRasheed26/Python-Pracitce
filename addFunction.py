def add(num1, num2):
    return num1 + num2


def main():
    num1 = input("Enter 1st Number :")
    num2 = input("Enter 2nd Number :")

    print("Sum is :", add(num1 , num2))

print(add(1, 2))
print(add(0.4, 3))
print(add("A", "B"))

if __name__ == "__main__":
    main()
