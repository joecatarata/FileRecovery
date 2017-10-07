import threading
import os
import pickle

def SearchUsingTrailer(signatures,driveLetter):
    #drive = openDrive()

    print(signatures)
    nCtr = 0
    nMax = 10000000
    cur = '0'
    prev = '0'
    sector = 512
    startSplice = 0
    endSplice = 1
    MaxSize = 10000000
    with open("\\\\.\\"+driveLetter+":", 'rb') as drive:
        while nCtr < nMax:
            drive.seek(nCtr * sector)
            #print("Error reading files")



def main():
    headers = {'jpg': [b'\xFF\xD8',b'\xFF\xD9'],
               'pdf': [b'\x25\x50', b'\x0A\x25\x25\x45\x4F\x46'],
               'docx': [b'\x50\x4B\x03\x04\x14\x00\x06\x00', b'\x50\x4B\x05\x06']}
    filename = 'headers'
    file = open(filename, 'wb')
    pickle.dump(headers, file)
    file = open(filename, 'rb')
    headers = pickle.load(file)
    choices = []

    while True:
        print("Choose which file types will you want to recover")
        print("jpg")
        print("pdf")
        print("docx")
        choice = (input("Enter choice(type the file type): "))

        choices.append(choice)

        AskMore = int(input("Do you want to input more files?[0/1]: "))
        if AskMore == 1:
            continue
        else:
            break

    driveLetter = input("Enter letter of drive to scan: ")
    driveLetter = driveLetter.upper()
    for i in choices:
        if i in headers:
            SearchUsingTrailer(headers.get(i))
        else:
            print("Sorry file is not supported.")





if __name__ == "__main__":
    main()
