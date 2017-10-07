import threading
import os
import pickle

def SearchUsingTrailer(signatures,driveLetter):
    #drive = openDrive()
    headtemp = signatures[0]
    header = [headtemp[i:i+1] for i in range(len(headtemp))]
    trailtemp = signatures[1]
    trailer =  [trailtemp[i:i+1] for i in range(len(trailtemp))]

    print(header[-1])
    print(trailer)

    nCtr = 0
    nMax = 10000000
    sector = 512
    MaxSize = 10000000
    index = 0
    found = False
    pHead = '0'
    with open("\\\\.\\"+driveLetter+":", 'rb') as drive:
        print("Opened Drive: " + driveLetter)
        while nCtr < nMax:
            #print(pHead, end="")
            #print(header[index])
            drive.seek(nCtr * sector)
            pHead = cur = drive.read(1)
            while cur == header[index]:
                if header[-1] == cur:
                    print("Found a file!", nCtr)
                    found = True
                    break

                cur = drive.read(1)
                index+=1

            if found:
                #implement write to file
                pass

            index = 0
            nCtr += 1








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
            SearchUsingTrailer(headers.get(i), driveLetter)
        else:
            print("Sorry file is not supported.")





if __name__ == "__main__":
    main()
