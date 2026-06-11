#A CHECK IF TWO FILE, PHOTO HAS CHANGED 
import hashlib


#

#--------------------------------------------------------------------

#LETS CREATE A FUNCTION FIRST THAT RETURN A HASH VALUE OF A FILE 
def hash_file(file_location):
    #WE CHOOSE A SHA256 HASH
    h = hashlib.new("sha256")
    #rb MEAN READ BINARY
    with open(file_location, "rb") as file:
        #CREATE A WHILE LOOP THAT WILL READ THE FILE UNTIL ITS EMPTY
        while True:
            chunk = file.read(1024)
            if chunk == b"":
                break
            h.update(chunk)
    return h.hexdigest()



#NOW HERE COME THE MAIN POINT OF THE CODE

#TWO FILE OR PHOTO OR ANYTHING PUT THEM AND SEE IF THERE IS ANY DIFFERENT EVEN IF ONE PIXEL CHANGE IN THE SECOND FILE THE HASH WILL CHANGE AND DETECT THAT
def check_changed(file1, file2):
    hash1 = hash_file(file1) #USING THE FIRST VALUE DEF
    hash2 = hash_file(file2)
    if hash1 == hash2:
        #IF THE HASH MATCH PRINT THIS OR YOU CAN WRITE ANY MASSEGE YOU LIKE
        print("nothing changed no modification happen")
    else:
        #IF THEY DIDNT PRINT THIS
        print("file has changed most likley\ncheck for the reason")
#!WARINING 
#THESE TWO PHOTO OF COURSE ARE NOT THERE FOR YOU TO RUN THESE ARE EXAMPLE TO UNDERSTAND 
#PUT THE FILE OR THE PHOTO PATH LIKE THIS 
#THESE ARE PHOTO FROM MY DEVICE CHANGE THEM TO FILE FROM YOUR DEVICE
check_changed("Screenshot (773).png", "imtext.png")

