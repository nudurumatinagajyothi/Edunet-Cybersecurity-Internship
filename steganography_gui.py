import cv2
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

# Load image function
def load_image():
    file_path = filedialog.askopenfilename()
    return cv2.imread(file_path), file_path

# Encode message function
def encode_message(img, msg):
    d = {chr(i): i for i in range(256)}
    height, width, _ = img.shape
    n, m, z = 0, 0, 0
    
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        if n >= height:
            n = 0
            m += 1
        if m >= width:
            print("Error: Image too small to store the message!")
            return None
    return img

# Decode message function
def decode_message(img, msg_length):
    message = ""
    n, m, z = 0, 0, 0
    
    for i in range(msg_length):
        message += chr(img[n, m, z])
        n += 1
        if n >= img.shape[0]:
            n = 0
            m += 1
        if m >= img.shape[1]:
            break
    return message

# GUI setup
root = tk.Tk()
root.withdraw()

img, file_path = load_image()
if img is None:
    print("No image selected!")
    exit()

msg = simpledialog.askstring("Input", "Enter secret message:")
password = simpledialog.askstring("Input", "Enter a passcode:", show='*')

encrypted_img = encode_message(img, msg)
if encrypted_img is not None:
    output_path = file_path.replace(".jpg", "_encrypted.jpg")
    cv2.imwrite(output_path, encrypted_img)
    os.system(f"start {output_path}")

pas = simpledialog.askstring("Input", "Enter passcode for decryption:", show='*')
if password == pas:
    decrypted_msg = decode_message(encrypted_img, len(msg))
    print("Decrypted message:", decrypted_msg)
else:
    print("ACCESS DENIED")
