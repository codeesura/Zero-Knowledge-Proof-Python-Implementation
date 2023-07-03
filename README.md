# Zero-Knowledge Proof (ZKP) Python Implementation

Zero-Knowledge Proofs (ZKP) are a cryptographic concept where one party (the prover) can prove to another party (the verifier) that they know a value, without conveying any information apart from the fact that they know the value. This concept is fundamental in various privacy-preserving technologies, including cryptocurrencies and secure multi-party computations.

The prover does not reveal the actual secret during the interaction, maintaining the secrecy of the information. It's a form of "interactive proof system."

This repository contains a simple implementation of Zero-Knowledge Proofs (ZKP) in Python.

## Table of Contents
1. [Requirements](#requirements)
2. [Usage](#usage)
3. [Example](#example)
4. [License](#license)

## Requirements

The Python version required for this script is Python 3.7+. The script also makes use of the `hashlib`, `os`, and `random` libraries, which are included in the standard Python distribution.

## Usage

The main script is `zkp.py`, which contains the `ZKProof` class. Here's a step-by-step guide on how to use it:

1. **Import the `ZKProof` class from the `zkp.py` script.** This class contains the main methods for generating proofs and verifying them.
2. **Initialize a `ZKProof` object.** When initializing, the object generates a random 'salt' value, used in the hashing process to increase security.
3. **Generate a proof using a secret value.** Call the `generate_proof` method on the object, passing the secret value you want to prove knowledge of. This will return a hashed value of a randomly generated number. This hashed number is a commitment that the prover sends to the verifier.
4. **Verify a guessed value.** To verify a guessed value, call the `verify` method on the object, passing the guessed value. This will return `True` if the hashed guessed value matches the stored hashed value, and `False` otherwise.

## Example

```python
zkp = ZKProof()
x = zkp.generate_proof('secret_value')
print('Proof:', x)
response = input('Enter the value to verify: ')
print('Verified:', zkp.verify(response))
```

In this example, the script will print the hashed proof and wait for a user input. If the input matches the secret value, it will print `Verified: True`; otherwise, it will print `Verified: False`.

## License

This project is licensed under the terms of the [MIT](https://github.com/codeesura/Zero-Knowledge-Proof-Python-Implementation/blob/main/LICENSE) license. You are free to use, modify, and distribute the code under this license.
