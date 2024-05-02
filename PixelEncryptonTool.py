from PIL import Image

def encrypt_image(image_path):
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    # Encrypting the image by swapping pixel values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (g, b, r)  # Example encryption: swapping RGB values

    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_image_path)
    return encrypted_image_path

def decrypt_image(encrypted_image_path):
    img = Image.open(encrypted_image_path)
    pixels = img.load()
    width, height = img.size

    # Decrypting the image by swapping pixel values back
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (b, r, g)  # Example decryption: swapping RGB values back

    decrypted_image_path = encrypted_image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_image_path)
    return decrypted_image_path

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt an image? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Please enter 'encrypt' or 'decrypt'.")
            continue

        image_path = input("Enter the path to the image file: ")

        if choice == 'encrypt':
            encrypted_image_path = encrypt_image(image_path)
            print("Image encrypted successfully. Encrypted image saved as:", encrypted_image_path)
        elif choice == 'decrypt':
            decrypted_image_path = decrypt_image(image_path)
            print("Image decrypted successfully. Decrypted image saved as:", decrypted_image_path)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
