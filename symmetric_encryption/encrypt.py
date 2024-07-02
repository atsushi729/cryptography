def encrypt(plaintext: str, key: str) -> str:
    # Ensure the key length is at least as long as the plaintext
    key = key[:len(plaintext)]

    # Convert plaintext and key to numerical values
    plaintext_nums = [ord(char) - ord('A') for char in plaintext]
    key_nums = [ord(char) - ord('A') for char in key]

    # Perform modular addition
    cipher_nums = [(p + k) % 26 for p, k in zip(plaintext_nums, key_nums)]

    # Convert numerical values back to letters
    cipher_text = ''.join(chr(num + ord('A')) for num in cipher_nums)

    return cipher_text


# Example usage
plaintext = "ATSUSHIHATAKEYAMA"
key = "THISISANEXAMPLEKEYINCOMPUTERSECURITYEXAM"
cipher = encrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Key: {key[:len(plaintext)]}")
print(f"Cipher: {cipher}")
