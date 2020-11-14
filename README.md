# HashAttack: A Dictionary Attack Tool for Hashes

## Description & Usage
A simple, yet quite useful and high-speed dictionary attack tool (700,000+ candidates per second), that attacks a supported hash with a user-defined dictionary file's candidates to find the string that matches with its corresponding hash.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/HashAttack-Dictionary-Attack-For-Hashes/main/Images/Example.png" >
<p>Example Execution - HashAttack</p>
</div>

## Supported Hashing Algorithms
- **BLAKE2b**
- **BLAKE2s**
- **MD5**
- **SHA-1**
- **SHA-2 (224-bit)**
- **SHA-2 (256-bit)**
- **SHA-2 (384-bit)**
- **SHA-2 (512-bit)**
- **SHA-3 (224-bit)**
- **SHA-3 (256-bit)**
- **SHA-3 (384-bit)**
- **SHA-3 (512-bit)**
- **SHAKE-128**
- **SHAKE-256**

## Hash Generator: String → Hash Converter (for tests)
HashAttack also comes with a "Hash Generator" program that converts a user-input string to a hash of the selected hashing algorithm, and then automatically copies the generated hash to the clipboard; mainly for the purpose of testing HashAttack conveniently.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/HashAttack-Dictionary-Attack-For-Hashes/main/Images/Example%20(Hash%20Generator).png" >
<p>Example Execution - Hash Generator</p>
</div>

This project was created in Python, for experimental/observational purposes; and can also be aided with my own super fast numbered dictionary generator [**NumNinja**](https://github.com/SHUR1K-N/NumNinja-Number-Dictionary-Generator)  (2M+ lines per second) for numeric attacks.

## Dependencies to PIP-Install
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: http://bit.do/SHUR1KN
