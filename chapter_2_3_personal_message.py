# changing case in a string with methods

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# using variables in strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")

message = f"Hello, {full_name.title()}!"
print(message)

# adding whitespace to strings with tabs or newlines

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# stripping whitespace

favourite_language = 'python '
print(favourite_language)
favourite_language.rstrip()
print(favourite_language.rstrip())

favourite_language = 'python '
favourite_language = favourite_language.rstrip()
print(favourite_language)

favourite_language = ' python'
favourite_language.rstrip()
favourite_language.lstrip()
favourite_language.strip()

# exercise 2.3 personal message

my_first_name = "Stephanie"
print(f"Hello, {my_first_name}! How are you?")

# exercise 2.4 name cases

my_first_name = "Stephanie"
print(my_first_name.upper())
print(my_first_name.lower())
print(my_first_name.title())

# exercise 2.5 famous quotes

print("\tAlbert Einstein once said, 'A person who never made a mistake never tried anything new.'")
