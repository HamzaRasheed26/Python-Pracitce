num = [0,0,0]

for i in range(0,3):
    num[i] = int(input("Enter Number :"))

if(num[0] > num[1] and num[0] > num[2]):
    print(num[0], " is Largest")
elif(num[1] > num[0] and num[1] > num[2]):
    print(num[1], " is Largest")
else:
    print(num[3], " is Largest")
