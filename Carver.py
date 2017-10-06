import threading
import os
import pickle

def openDrive(driveLetter):
    drive = open("\\\\.\\"+driveLetter+":", 'rb')
    return drive
def loadSettings():
    pass

def SearchUsingTrailer(headers, choices):
    pass


def main():
    filename = 'headers'
    file = open(filename, 'rb')
    headers = pickle.load(file)
    print(headers)
    choices = []

    while True:
        print("Choose which file types will you want to recover")
        print("[1] .jpg/.jpeg")
        print("[2] .pdf")
        print("[3] ..docx")
        choice = int(input("Enter choice: "))

        choices.append(choice)

        AskMore = int(input("Do you want to input more files?[0/1]: "))
        if AskMore == 1:
            continue
        else:
            SearchUsingTrailer(headers, choices)


if __name__ == "__main__":
    main()
