import cv2

img = cv2.imread(r"C:\Users\RRM2005\OneDrive\My\CS\img.jpg")
# C:\Users\RRM2005\OneDrive\My\CS\img.jpg
# Use raw string to avoid escape sequence issues

decryp = {}

for i in range(255):
    decryp[i] = chr(i)

message = ""
n = 0
m = 0
z = 0

# Get the original passcode and message length
password = input("Enter the original passcode:")
msg_length = int(input("Enter the length of the secret message:"))

pas = input("Enter passcode for Decryption")
if password == pas:
    for i in range(msg_length):
        message += decryp[img[n, m, z]]
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m == img.shape[1]:
                m = 0
                n += 1
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")