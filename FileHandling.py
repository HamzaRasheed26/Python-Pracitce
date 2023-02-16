import os.path

def main():

    if(os.path.exists("Data.txt")):
        file = open("Data.txt",'r')
        lines = file.read()
        file.close()
        print(lines)
    else:
        print("File does not Exist")

    file = open("Data.txt", 'a')
    file.write("\nComputer Science")
    file.close()

if __name__ == "__main__":
    main()

