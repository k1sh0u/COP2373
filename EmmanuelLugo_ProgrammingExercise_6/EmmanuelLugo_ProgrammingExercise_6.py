'''
Assignment instructions:

Create functions to validate phone numbers, social security numbers and zip codes using regular expressions. Create a main function to get input from a user and then displaying if the phone number, social security number and zip code they entered is valid.

Be sure to test the functions with various inputs, including valid and invalid examples, to ensure the correctness of the regular expressions.

You must also have a technical design document (refer to the Submitting Programming Exercises Module).

Submit both your .py file and .doc/.docx file in this assignment and these files must also be in your repository.


---

Pseudo code:

initialize global variables:

zip_code = 0
phone_number = 0
ssn = 0

Main function
asks the user for their phone number, SSN, zip, one input at a time.
make the function clarify to the user that no dashed should be used, only the numbers.

test functions (for each variable)
tests for a valid entry.

each entry will be tested, one after another.

ex.

Let's say that the first input it wants is the zip.
The user will enter a valid or invalid zip.
The zip_code_test function will then be called within the main function

The test function will test for a valid entry
if invalid, return and ask for another entry.
if valid, the variable is updated, loop exits and function is done.

then the next test function for the next variable.


Takes the new global variable and tests/validates.


Compile function
This function will take all the newly validated variables and for a statement, like:
"Heres what you entered, does everything look good?"

Maybe add a feature for the user to respond if something is wrong and they would like to start over... maybe.

'''

