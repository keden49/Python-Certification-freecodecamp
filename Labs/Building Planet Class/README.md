# Build a Planet Class

 OBJECTIVE:
 Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

- You should create a class named Planet.
- The Planet class should have an __init__ method that:
- Has four parameters: self, name, planet_type, and star.
- Raises a TypeError with the message name, planet type, and star must be strings if any of the arguments passed in is not a string type.
- Raises a ValueError with the message name, planet_type, and star must be non-empty strings if any of the arguments passed in is an empty string.
- Assigns the values passed in to the instance attributes name, planet_type, and star.
- The Planet class should have an orbit method that returns a string in the format {name} is orbiting around {star}....
- The Planet class should have a __str__ method that returns a string in the format Planet: {name} | Type: {planet_type} | Star: {star}.
- You should create three instances of the Planet class named planet_1, planet_2, and planet_3.
- You should print each planet object to see the __str__ method output.
- You should call the orbit method on each planet object and print the result.


# Tests

1. You should create a class named Planet.
2. The Planet class should have an __init__ method.
3. The __init__ method should have four parameters: self, name, planet_type, and star, in this order.
4. The __init__ method should raise a TypeError with the message name, planet type, and star must be strings if the first argument passed in is not a string type.
5. The __init__ method should raise a TypeError with the message name, planet type, and star must be strings if the second argument passed in is not a string type.
6. The __init__ method should raise a TypeError with the message name, planet type, and star must be strings if the third argument passed in is not a string type.
7. The __init__ method should raise a ValueError with the message name, planet_type, and star must be non-empty strings if the first argument passed in is an empty string.
8. The __init__ method should raise a ValueError with the message name, planet_type, and star must be non-empty strings if the second argument passed in is an empty string.
9. The __init__ method should raise a ValueError with the message name, planet_type, and star must be non-empty strings if the third argument passed in is an empty string.
10. You should assign name to self.name in the __init__ method.
11. You should assign planet_type to self.planet_type in the __init__ method.
12. You should assign star to self.star in the __init__ method.
13. The Planet class should have an orbit method.
14. The orbit method should return a string in the format {name} is orbiting around {star}....
15. The Planet class should have a __str__ method.
16. The __str__ method should return a string in the format Planet: {name} | Type: {planet_type} | Star: {star}.
17. You should create three instances of the Planet class named planet_1, planet_2, and planet_3.
18. You should print each planet object to see the __str__ method output.
19. You should call the orbit method on each planet object and print the result
