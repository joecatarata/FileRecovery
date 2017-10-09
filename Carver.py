import threading
import os
import pickle

def SearchUsingTrailer(signatures,driveLetter,fileType):
    #drive = openDrive()
    headtemp = signatures[0]
    header = [headtemp[i:i+1] for i in range(len(headtemp))]
    trailtemp = signatures[1]
    trailer =  [trailtemp[i:i+1] for i in range(len(trailtemp))]
    print(header)
    print(trailer)
    nCtr = 0
    fileCtr = 0
    nMax = 10000000
    sector = 512
    maxSize = 10000000
    index = 0
    found = False
    pHead = '0'
    trailIndex = 0
    done = False
    with open("\\\\.\\"+driveLetter+":", 'rb') as drive:
        print(nCtr)
        print("Opened Drive: " + driveLetter)
        while nCtr < nMax:
            #print(pHead, end="")
            #print(header[index])
            drive.seek(nCtr * sector)
            pHead = cur = drive.read(1)
            cur = pHead
            while cur == header[index]:
                if cur == header[-1] and index == len(header)-1: #if current is equal to the last byte of the passed header
                    print("Found a potential file!")
                    print(cur, end="")
                    print(header[-1])
                    found = True
                    break
                cur = drive.read(1)
                index+=1

            if found:
                fileCtr += 1
                newFile = open("recovered\\"+str(fileCtr)+"."+fileType,"wb")
                curSize = 0
                trailIndex = 0
                foundTrailer = False
                done = False
                cur = pHead
                for i in header:
                    newFile.write(i)
                pHead = drive.read(1)
                done = False
                while done == False and curSize < maxSize:
                    trailIndex = 0
                    newFile.write(pHead)
                    while pHead == trailer[trailIndex]:
                        if pHead == trailer[-1] and trailIndex == len(trailer)-1:
                            print("Pumasok")
                            done = True
                            break
                        pHead = drive.read(1)
                        newFile.write(pHead)
                        trailIndex += 1
                        curSize += 1
                    #    print(trailIndex, end="")
                    if not done:
                        pHead = drive.read(1)
                        curSize += 1
                        trailIndex = 0
                newFile.close()
                if curSize >= maxSize:
                    print("False positive")
                #implement write to file
            trailIndex = 0
            index = 0
            nCtr += 1
            found = False

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
            SearchUsingTrailer(headers.get(i), driveLetter, i)
        else:
            print("Sorry file is not supported.")





if __name__ == "__main__":
    main()
