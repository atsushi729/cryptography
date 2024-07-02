def decrypt(cipher, key):
    # Ensure the key length is at least as long as the ciphertext
    key = key[:len(cipher)]

    # Convert cipher and key to numerical values
    cipher_nums = [ord(char) - ord('A') for char in cipher]
    key_nums = [ord(char) - ord('A') for char in key]

    # Perform modular subtraction
    plaintext_nums = [(c - k + 26) % 26 for c, k in zip(cipher_nums, key_nums)]

    # Convert numerical values back to letters
    plaintext = ''.join(chr(num + ord('A')) for num in plaintext_nums)

    return plaintext


# Example usage
cipher = "TAAMAZIUEQAWTJEWE"
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM"
plaintext = decrypt(cipher, key)
print(f"Cipher: {cipher}")
print(f"Key: {key[:len(cipher)]}")
print(f"Plaintext: {plaintext}")
