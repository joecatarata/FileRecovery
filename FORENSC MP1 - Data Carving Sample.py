# This is the sample tutorial created during FORENSC class AY1718 of DLSU CCS CT
 # opens the drive D folder in windows. Use /dev/sdb for linux and /dev/disk1 for Mac


def jpgSearch():
	nCtr = 0
	nMax = 10000000
	prev = '0'
	cur = '0'
	sector = 512 # used to designate sectors as 512 bytes, for easier reading since it signified chunks
	imagectr = 0 # counter used to iterate the number of recovered imaes
	maxSize = 10000000 # arbitrary value to designate the maximum file size of a recovered image so that if it just so happens that a header was found
	drive = open("\\\\.\F:", 'rb')
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
					while running and mCtr < maxSize: # loops until the footer FFD9 is detected or arbitrary limit is reached
						cur = reader = drive.read(1) # reads one byte at a time from the possible JPG file
						image.write(cur) # write the byte from the JPG file read
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

#async def main:
		
if __name__ == "__main__":
	main()
