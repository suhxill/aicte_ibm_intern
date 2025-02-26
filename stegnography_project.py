import cv2
import os

def embed_message(img, message, password):
    char_to_pixel = {chr(i): i for i in range(256)}
    pixel_to_char = {i: chr(i) for i in range(256)}

    height, width, _ = img.shape
    message_length = len(message)
    index = 0

    for i in range(height):
        for j in range(width):
            for k in range(3):
                if index < message_length:
                    img[i, j, k] = char_to_pixel[message[index]]
                    index += 1
                else:
                    break
            if index >= message_length:
                break
        if index >= message_length:
            break

    cv2.imwrite("encrypted_image.png", img)
    print("Message embedded successfully!")

def extract_message(img, password, message_length):
    pixel_to_char = {i: chr(i) for i in range(256)}

    height, width, _ = img.shape
    extracted_message = ""
    index = 0

    for i in range(height):
        for j in range(width):
            for k in range(3):
                if index < message_length:
                    extracted_message += pixel_to_char[img[i, j, k]]
                    index += 1
                else:
                    break
            if index >= message_length:
                break
        if index >= message_length:
            break

    return extracted_message

def main():
    image_path = "mypic.jpg"
    if not os.path.exists(image_path):
        print("Image file not found!")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("Failed to load the image!")
        return

    message = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    embed_message(img, message, password)

    encrypted_image_path = "encrypted_image.png"
    encrypted_img = cv2.imread(encrypted_image_path)
    if encrypted_img is None:
        print("Failed to load the encrypted image!")
        return

    entered_password = input("Enter passcode for decryption: ")
    if entered_password == password:
        extracted_message = extract_message(encrypted_img, password, len(message))
        print("Decrypted message:", extracted_message)
    else:
        print("Incorrect password! You are not authorized.")

if __name__ == "__main__":
    main()
