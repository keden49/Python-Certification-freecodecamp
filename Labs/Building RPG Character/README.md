## PROJECT STRUCTURE
```
Building RPG Character/
├── RPG_Character.ipynb       # Main Google notebook
├── README.md                 # This documentation file
└── test file
```

## PROJECT OVERVIEW
This project contains a Python implementation of an RPG (Role-Playing Game) character creation system. The system allows users to create characters with customizable stats while enforcing validation rules.

## FEATURES

-Character name validation (string, length, format)

-Stat point allocation (Strength, Intelligence, Charisma)

-Visual stat representation using symbols

-Comprehensive input validation

## CORE FUNCTIONALITY

Character Stats System

-Total Points: Characters start with 7 total stat points

-Stat Range: Each stat must be between 1-4 points

-Visual Display: Stats shown with filled (●) and empty (○) dots

## VALIDATION RULES

1. Name Requirements:

- Must be a string

- Cannot be empty

- Maximum 10 characters

- No spaces allowed

2. Stat Requirements:

- All stats must be integers

- Minimum: 1 point per stat

- Maximum: 4 points per stat

- Total must equal exactly 7 points

## HOW TO USE 
1. Clone this repository(on your terminal)
```bash
git clone https://github.com/keden49/python-freecodecamp.git
```
2. Navigate to project directory
```bash
cd python-freecodecamp/"Building RPG Character"
```
3. Running code
```bash
python
```
```python
from test1 import create_character
```
```python
RPG = create_character('FATHELA', 4, 2, 1)
```
```pyhton
print(RPG)
```
**NOTE: YOU CAN ALTER THE PARAMETERS TO TEST DIFFERENT INPUTS**

EXAMPLE OUTPUT 
```
FATHELA
STR ●●●●○○○○○○  (4 points)
INT ●●○○○○○○○○  (2 points)
CHA ●○○○○○○○○○  (1 point)
```

4. Existing Python
 
```python
exit()
```

## TECHNOLOGIES USED 
-Python 3

-Jupyter Notebook (RPG_Character.ipynb)

-Git/GitHub for version control

## ACKNOWLEGEMENTS 
1. Freecodecamp-The project is part of the FreeCodeCamp Python curriculum

2. Google Colab - For providing a free, cloud-based Jupyter notebook environment that made this project development seamless

3. GitHub - For hosting and version control services


