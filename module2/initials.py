# Salvador Perez-Salgado
# 2023-07-17

# initials.py is an excersice from the Module 2 of the NUS Python for Analytics Course
# The assignment was to create a script that returns the initials from a name

# We clean up the environment
index = 0
initials = ''
# Request the user to input the full name from the keyboard
name = input ("Type in your full name: ")

# Loop the string until we find no more whitespaces
while True:
    # Store initials in this variable
    initials = initials + name[index:index + 1]
    # Split string from the index to the end
    name = name[index:]
    # When find returns -1 no whitespaces were found so we exit the loop
    index = name.find(' ')
    if index == -1 :
        break
    # If a whitespace was found we increase the index
    index = index + 1
    # Show the initials
print ("Your initials are: " + initials)
