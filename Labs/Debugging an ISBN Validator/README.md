# Lab Instructions 

The ISBN (International Standard Book Number) is a unique identifier assigned to commercial books. It can be either 10 or 13 digits long, and the last digit is a check digit calculated from the other digits. Camperbot has tried to build their own ISBN validator. However, they have made a few mistakes along the way.In this lab, you will fix the existing code and make it function properly.
 
# Expected behavior:
When the user runs the program, it will show the prompt Enter ISBN and length: . The user can enter the ISBN code they want to validate in ISBN,length format. The ISBN code should not contain hyphens, followed by its length (10 or 13), separated by a comma.

*Example inputs:* 

1530051126,10 for ISBN-10 codes. 9781530051120,13 for ISBN-13 codes.

*How to find the check digit:*

- You don't have to know the detailed calculation logic in this lab. The functions calculate_check_digit_10 and calculate_check_digit_13 will take care of the calculation and return the expected check digit in string.
- The check digit for ISBN-10 codes can be a number from 0 to 9 or an uppercase letter X.
- The check digit for ISBN-13 codes can be a number from 0 to 9.
- Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

- You should fix the IndentationError in the current code.
- Even if the user does not enter a comma separated value, the program should handle the IndexError without crashing.
- When the user does not enter a comma separated value, they should see the message Enter comma-separated values. in the console, and the program should terminate.
- Even if the user enters a non-numeric value for the length, the program should handle the ValueError without crashing.
- When the user enters a non-numeric value for the length, they should see the message Length must be a number. in the console, and the program should terminate.
- You should fix the off-by-one error in the validate_isbn function.
- You should fix the TypeError in the current code that occurs when the user enters a valid ISBN code.
- You should fix the IndexError in the current code when the user enters a valid ISBN code.
- Even if the user enters an incorrect ISBN code with characters other than numbers, the program should handle the ValueError that occurs without crashing.
- When the user enters an incorrect ISBN code with characters other than numbers, they should see the message Invalid character was found. in the console.
- When the user enters 1530051126,10, they should see the message Valid ISBN Code.
- When the user enters 9781530051120,13, they should see the message Valid ISBN Code.
- Important: you will need to comment out the main() call in the global space for the tests to run properly.


# Tests 
1. You should comment out the call to the main function to allow for the rest of the tests to work properly.
2. You should have a validate_isbn function
3. You should have a calculate_check_digit_10 function.
4. You should have a calculate_check_digit_13 function.
5. You should have a main function.
6. When the user inputs a value that is not a comma separated value, you should see the message Enter comma-separated values. in the console.
7. When the user inputs a non-numeric value for the length, you should see the message Length must be a number. in the console.
8. When the user enters an incorrect ISBN code with characters other than numbers, you should see the message Invalid character was found. in the console.
9. When the user enters 1530051126,10, you should see the message Valid ISBN Code. in the console.
10. When the user enters 9781530051120,13, you should see the message Valid ISBN Code.
11. When the user enters 1530051125,10, you should see the message Invalid ISBN Code..
12. When the user enters 9781530051120,10, you should see the message ISBN-10 code should be 10 digits long.
13. When the user enters 1530051126,13, you should see the message ISBN-13 code should be 13 digits long.
14. When the user enters 15-0051126,10, you should see the message Invalid character was found.
15. When the user enters 1530051126,9, you should see the message Length should be 10 or 13.
16. When the user enters 1530051125,A, you should see the message Length must be a number.
17. When the user enters 1530051125, you should see the message Enter comma-separated values.
18. When the user enters 9971502100,10, you should see the message Valid ISBN Code.
19. When the user enters 080442957X,10, you should see the message Valid ISBN Code.
20. When the user enters 9781947172104,13, you should see the message Valid ISBN Code.
