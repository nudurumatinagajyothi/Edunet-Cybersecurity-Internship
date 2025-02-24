#pip install opencv-python
import cv2
import os

# Load the image
img = cv2.imread("C:\\Users\\DELL\\Desktop\\virat-kohli.jpg")

# Create a writable copy of the image
img = img.copy()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# ASCII dictionaries for encoding and decoding
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape  # Get image dimensions
n, m, z = 0, 0, 0  # Pixel indices

# Encoding the message
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]  # Encode message into pixel

    # Move to next pixel
    n += 1
    if n >= height:  
        n = 0
        m += 1
    if m >= width:
        print("Error: Image too small to store the message!")
        exit()

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open encrypted image 

# Decryption
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += chr(img[n, m, z])  # Decode character

        # Move to next pixel
        n += 1
        if n >= height:  
            n = 0
            m += 1
        if m >= width:
            break

    print("Decrypted message:", message)
else:
    print("ACCESS DENIED")
