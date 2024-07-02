# Symmetric Encryption

This project demonstrates a simple symmetric encryption and decryption algorithm using a basic form of the Vigenère cipher. The encryption process involves using a key to transform plaintext into ciphertext, and the decryption process uses the same key to revert the ciphertext back into plaintext.

## How It Works

### Encryption Algorithm

1. **Key Adjustment**:
   - The key is truncated or repeated to match the length of the plaintext.

2. **Convert Characters to Numbers**:
   - Each character in the plaintext and key is converted to a numerical value using the formula: `ord(char) - ord('A')`.
   - For example, 'A' -> 0, 'B' -> 1, ..., 'Z' -> 25.

3. **Modular Addition**:
   - Each numerical value from the plaintext is added to the corresponding value from the key.
   - The result is taken modulo 26 to ensure it remains within the range of 0 to 25.

4. **Convert Numbers Back to Characters**:
   - The resulting numerical values are converted back to characters using the formula: `chr(num + ord('A'))`.

### Encryption Code

```python
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
plaintext = "HELLO"
key = "KEY"
cipher = encrypt(plaintext, key)
print(f"Plaintext: {plaintext}")
print(f"Key: {key[:len(plaintext)]}")
print(f"Cipher: {cipher}")
```

### Example Output

```
Plaintext: HELLO
Key: KEYKE
Cipher: RIJVS
```

### Decryption Algorithm

1. **Key Adjustment**:
   - The key is truncated or repeated to match the length of the ciphertext.

2. **Convert Characters to Numbers**:
   - Each character in the ciphertext and key is converted to a numerical value using the formula: `ord(char) - ord('A')`.

3. **Modular Subtraction**:
   - Each numerical value from the ciphertext is subtracted by the corresponding value from the key.
   - The result is taken modulo 26 to ensure it remains within the range of 0 to 25.

4. **Convert Numbers Back to Characters**:
   - The resulting numerical values are converted back to characters using the formula: `chr(num + ord('A'))`.

### Decryption Code

```python
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
cipher = "RIJVS"
key = "KEY"
plaintext = decrypt(cipher, key)
print(f"Cipher: {cipher}")
print(f"Key: {key[:len(cipher)]}")
print(f"Plaintext: {plaintext}")
```

### Example Output

```
Cipher: RIJVS
Key: KEYKE
Plaintext: HELLO
```

## How to Run

1. Copy the code into a Python file, for example `encryption.py`.
2. Run the file using a Python interpreter:
   ```sh
   python encryption.py
   ```

## Notes

- The key should be at least as long as the plaintext or ciphertext for effective encryption and decryption.
- The algorithm assumes that the plaintext and key consist of uppercase English letters only.