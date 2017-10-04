# This is the sample tutorial created during FORENSC class AY1718 of DLSU CCS CT
 # opens the drive D folder in windows. Use /dev/sdb for linux and /dev/disk1 for Mac
import threading
import random

def openDrive():
    drive = open("\\\\.\\D:", 'rb')
    return drive

def readAndWrite(image, drive):
    byte = drive.read(1)
    image.write(byte)
    return byte

def jpgSearch():
    nCtr = 0
    nMax = 10000000
    prev = '0'
    cur = '0'
    sector = 512 # used to designate sectors as 512 bytes, for easier reading since it signified chunks
    imagectr = 0 # counter used to iterate the number of recovered imaes
    jpegMaxSize = 10000000 # arbitrary value to designate the maximum file size of a recovered image so that if it just so happens that a header was found
    pdfMaxSize = 100000000
    docxMaxSize = 100000000
    running = False
    drive = openDrive()
    while nCtr < nMax:
        try:
            drive.seek(nCtr * sector) # iterates per sector
            cur = reader = drive.read(1) # reads the first byte of each sector

            if cur == b'\xFF':
                nextbyte = drive.read(1) # reads the second byte of each sector
                if nextbyte == b'\xD8': # will be true if a JPG file header, FFD8, is detected
                    print("FOUND - ", nCtr)
                    imagectr += 1 # iterate to designate the image number
                    image = open("found\\" + str(imagectr) + ".jpg","wb") # creates a new file in the 'found' folder and allows to write in bytes
                    running = True # used to designate that the writer is running
                    image.write(b'\xFF') # writes the JPG headers to the new file
                    image.write(b'\xD8')
                    mCtr = 0 # mCtr is used as a limiter just in case the new file is not really a JPG file, it stops at 10Mb, can be removed if image files is larger
                    print ("sad")
                    while running and mCtr < jpegMaxSize: # loops until the footer FFD9 is detected or arbitrary limit is reached
                        print(nCtr)
                        cur = readAndWrite(image, drive)
                        if cur == b'\xD9' and prev == b'\xFF': # responsible for checking if the footer FFD9 is found
                            running = False # once the footer is found, running will be set to false to end the loop
                            image.close() # the file would be closed to save the image
                            print("Image Saved")
                        prev = cur # sets the cur value to prev, this is used to detect the 2 bytes for FF and D9
                        mCtr += 1 # this counter is used to iterate until it reaches the arbitrary limit

                    if mCtr >= maxSize: # just in case the arbitrary value is reached, it would safely close the image
                        image.close()
                        print("Image Saved - failed")
        except:
            pass
        nCtr += 1

def pdfSearch():
    # pdfSearch
    nCtr = 0
    nMax = 10000000
    prev = '0'
    cur = '0'
    sector = 512 # used to designate sectors as 512 bytes, for easier reading since it signified chunks
    imagectr = 0 # counter used to iterate the number of recovered imaes
    jpegMaxSize = 10000000 # arbitrary value to designate the maximum file size of a recovered image so that if it just so happens that a header was found
    pdfMaxSize = 100000000
    docxMaxSize = 100000000
    nCtr = 0
    while nCtr < nMax:
        try:
            drive.seek(nCtr * sector) # iterates per sector
            cur = reader = drive.read(1) # reads the first byte of each sector
            if cur == b'\x25':
                nextbyte = drive.read(1)
                if nextbyte == b'\x50':
                    print("FOUND - ", nCtr)
                    imagectr += 1
                    image = open("found\\" + str(imagectr) + ".pdf","wb")
                    running = True
                    image.write(b'\x25')
                    image.write(b'\x50')
                    mCtr = 0
                    while running and mCtr < pdfMaxSize:
                        cur = readAndWrite(image, drive)
                        if cur == b'\x0A': #trailer
                            mCtr += 1
                            cur = readAndWrite(image, drive)
                            if cur == b'\x25':
                                mCtr += 1
                                cur = readAndWrite(image, drive)
                                if cur == b'\x25':
                                    mCtr += 1 # this counter is used to iterate until it reaches the arbitrary limit
                                    cur = readAndWrite(image, drive)
                                    if cur == b'\x45':
                                        mCtr += 1 # this counter is used to iterate until it reaches the arbitrary limit
                                        cur = readAndWrite(image, drive)
                                        if cur == b'\x4F':
                                            mCtr += 1 # this counter is used to iterate until it reaches the arbitrary limit
                                            cur = readAndWrite(image, drive)
                                            if cur == b'\x46':
                                                running = False # once the footer is found, running will be set to false to end the loop
                                                image.close() # the file would be closed to save the image
                                                print("PDF  Saved")
                        mCtr += 1 # this counter is used to iterate until it reaches the arbitrary limit


                    if mCtr >= pdfMaxSize: # just in case the arbitrary value is reached, it would safely close the image
                        image.close()
                        print("PDF Saved - failed")
        except:
            pass
        nCtr += 1


def docxSearch():
    nCtr = 0
    nMax = 10000000
    prev = '0'
    cur = '0'
    sector = 512 # used to designate sectors as 512 bytes, for easier reading since it signified chunks
    imagectr = 0 # counter used to iterate the number of recovered imaes
    jpegMaxSize = 10000000 # arbitrary value to designate the maximum file size of a recovered image so that if it just so happens that a header was found
    pdfMaxSize = 100000000
    docxMaxSize = 100000000
    openDrive()
    while nCtr < nMax:
        try:
            drive.seek(nCtr * sector) # iterates per sector
            cur = reader = drive.read(1) # reads the first byte of each sector
            if cur == b'\x50':
                nextbyte = drive.read(1)
                if nextbyte == b'\x4B':
                    nextbyte = drive.read(1)
                    if nextbyte == b'\x03':
                        nextbyte = drive.read(1)
                        if nextbyte == b'\x04':
                            nextbyte = drive.read(1)
                            if nextbyte == b'\x14':
                                nextbyte = drive.read(1)
                                if nextbyte == b'\x00':
                                    nextbyte = drive.read(1)
                                    if nextbyte == b'\x06':
                                        nextbyte = drive.read(1)
                                        if nextbyte == b'\x00':
    	                                    print("FOUND  DOCX - ", nCtr)
    	                                    imagectr += 1
    	                                    image = open("found\\" + str(imagectr) + ".docx","wb")
    	                                    running = True
    	                                    image.write(b'\x50')
    	                                    image.write(b'\x4B')
    	                                    image.write(b'\x03')
    	                                    image.write(b'\x04')
    	                                    image.write(b'\x14')
    	                                    image.write(b'\x00')
    	                                    image.write(b'\x06')
    	                                    image.write(b'\x00')
    	                                    mCtr = 0
    	                                    while running and mCtr < docxMaxSize:
    	                                        cur = readAndWrite(image, drive)
    	                                        if cur == b'\x50': #trailer
    	                                            mCtr += 1
    	                                            cur = readAndWrite(image, drive)
    	                                            if cur == b'\x4B':
    	                                                mCtr += 1
    	                                                cur = readAndWrite(image, drive)
    	                                                if cur == b'\x05':
    	                                                    mCtr += 1 # this counter is used to iterate until it reaches the arbitrary limit
    	                                                    cur = readAndWrite(image, drive)
    	                                                    if cur == b'\x06':
    	                                                        mCtr += 1
    	                                                        i = 0
    	                                                        while i < 18:
    	                                                            cur = readAndWrite(image, drive)
    	                                                            i += 1

    	                                                        running = False # once the footer is found, running will be set to false to end the loop
    	                                                        image.close() # the file would be closed to save the image
    	                                                        print("DOCX  Saved")

    	                                        mCtr += 1
    	                                    if mCtr >= maxSize: # just in case the arbitrary value is reached, it would safely close the image
    	                                        image.close()
    	                                        print("DOCX Saved - failed")

        except:
            pass
        nCtr += 1

def pngSearch():
    counter = 0

def main():
    print("It works!")
    jpgSearch()
if __name__ == "__main__":
	main()
