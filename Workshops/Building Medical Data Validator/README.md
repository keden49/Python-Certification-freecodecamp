## Project Overview 
This is a Python utility for validating medical record data against specific formatting constraints. The validator checks for correct data types, formats, and value ranges across a collection of patient records.

## Core Components

1. Data Structure

- Medical records are stored as dictionaries with 6 required fields:

- *patient_id*: String matching pattern 'P' or 'p' followed by digits

- *age*: Integer >= 18

- *gender*: String ('male' or 'female', case-insensitive)

- *diagnosis*: String or None

- *medications*: List of strings

- *last_visit_id*: String matching pattern 'V' or 'v' followed by digits

## Functionality

1. find_invalid_records(): Evaluates a single record against all validation rules and returns a list of fields that fail validation.
2. validate(): Main validation function that:
   
   - Verifies input is a list or tuple
   - Checks each element is a dictionary with exactly the required keys
   - Validates each record's data using find_invalid_records()
   - Provides detailed error messages with position indices
   - Returns boolean validation result
  
## Project Takeaways 
1. Algorithms and code structure
2. List comprehensions
3. Dictionaries and sets manipulation
4. Implementing Regular expressions
   


