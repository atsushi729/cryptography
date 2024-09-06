# RSA Key Generation Process

The RSA algorithm is a widely used encryption method that relies on the mathematical properties of prime numbers. Below
is a step-by-step explanation of how RSA key generation works based on the provided Python code.

## Steps in the RSA Algorithm

### 1. Select Two Large Prime Numbers `p` and `q`

- The function `generate_large_prime(bits)` generates two large prime numbers, `p` and `q`. This function uses random
  numbers of the specified bit length and checks for primality using the `isprime` function from the SymPy library.
- For instance, when `bits` is set to 512, each prime number will be approximately 256 bits long.

### 2. Compute the Modulus `n`

- The modulus `n` is calculated by multiplying the two prime numbers:

  ```
  n = p * q
  ```

- This modulus is a fundamental component of both the public and private keys, used in encryption and decryption.

### 3. Compute Euler's Totient Function `φ(n)`

- Euler’s Totient Function `φ(n)` is calculated as:

  ```
  φ(n) = (p - 1) * (q - 1)
  ```

- It represents the number of integers less than `n` that are coprime with `n`.

### 4. Choose the Public Exponent `e`

- A commonly used value for `e` is 65537, which is prime and provides a balance between security and performance.
- `e` must be coprime with `φ(n)`. This is checked using `math.gcd(e, phi_n)` to ensure they share no common factors
  other than 1.

### 5. Compute the Private Exponent `d`

- The private exponent `d` is computed using the modular inverse of `e` modulo `φ(n)`:

  ```
  d = mod_inverse(e, φ(n))
  ```

- This calculation uses the `mod_inverse` function from SymPy.

### 6. Generate the Public and Private Keys

- **Public Key**: `(n, e)`
- **Private Key**: `(n, d)`

### Example Output

Running the provided code produces the following output format:

```plaintext
Public Key: (n_value, 65537)
Private Key: (n_value, d_value)
```

## How RSA Encryption and Decryption Work

- **Encryption**: A sender uses the recipient's public key `(n, e)` to encrypt a message `m`. The ciphertext `c` is
  computed as:

  ```
  c = m^e mod n
  ```

- **Decryption**: The recipient uses their private key `(n, d)` to decrypt the ciphertext `c` and retrieve the original
  message:

  ```
  m = c^d mod n
  ```

### Security

The security of RSA relies on the difficulty of factoring the large number `n` into its prime components `p` and `q`.
