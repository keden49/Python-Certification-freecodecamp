# Caesar Cipher
The Caesar Cipher is a substitution cipher that encrypts a message by shifting every letter in the plaintext a fixed number of positions down the alphabet. When the shift reaches the end of the alphabet, it "wraps around" back to the beginning. The shift value serves as the secret key used for both encryption and decryption.

## MECHANISM

The Implementation: str.maketrans
This code utilizes the built-in str.maketrans method to handle the transformation efficiently. Instead of processing characters one-by-one, the function generates a translation table a pre-calculated mapping that pairs every character in the original alphabet with its corresponding shifted character.

The Translation Process: translate
Once the mapping table is created, the translate method is applied to the input text. It acts as a high-speed replacement engine, swapping every character in the message according to the rules defined in the translation table. This approach ensures that case sensitivity and non-alphabetic characters are handled consistently and performantly.


```
EXAMPLE

Letter Mapping (Shift = 3)
┌──────────────┬─────────────────┬──────────────────┐
│ Original     │ Shifted         │ Unicode Codes    │
├──────────────┼─────────────────┼──────────────────┤
│ a → d        │ 97 → 100        │ 'a' (97)→'d'(100)│
│ A → D        │ 65 → 68         │ 'A' (65)→'D'(68) │
│ d → g        │ 100 → 103       │ 'd'(100)→'g'(103)│
│ D → G        │ 68 → 71         │ 'D' (68)→'G'(71) │
│ x → a        │ 120 → 97        │ 'x'(120)→'a'(97) │
│ X → A        │ 88 → 65         │ 'X' (88)→'A'(65) │
└──────────────┴─────────────────┴──────────────────┘

```
## FEATURES 

Key Features

-Preserves Case Sensitivity (e.g., "A" → "D" and "a" → "d")

-Maintains Non-Alphabetic Characters (spaces, numbers, and punctuation remain unchanged)

-Built-in Shift Validation (accepts only integers between 1 and 25)

-Optimized Performance (utilizes str.maketrans and translate for high-speed processing)

-Dual-Functionality (includes dedicated functions for both encryption and decryption)

-Wraparound Logic (automatically wraps from "Z" back to "A")
## HOW TO USE 

1. Clone this repository
```bash
git clone https://github.com/keden49/python-freecodecamp.git
```
2. Navigate to the Project Directory(on your terminal)

```bash
cd python-freecodecamp/"Building cipher"
```

3. Running the code(terminal)
```
python 
```
```python
from test import encrypt, decrypt
```

```python
encrypted = encrypt("Hello World", 3) # Encrypt a message
```
```python
print(encrypted)  # "Khoor Zruog"
```
```python
decrypted = decrypt("Khoor Zruog", 3)# Decrypt a message
```
```python
print(decrypted)  # "Hello World"
```
**NOTE: YOU CAN ALTER THE PARAMETERS TO TEST DIFFERENT INPUTS**

4. Existing python
```
exit()
```


##  ACKNOWLEDGEMENTS
-Kevin Jayden: Lead Developer 

-FreeCodeCamp: For the foundational project inspiration and curriculum.

-Python Documentation: For insights into the str.maketrans and translate methods.

