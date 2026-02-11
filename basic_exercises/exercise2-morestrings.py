text = "  Hello, World! Welcome to Python Programming.  "

#The string with leading and trailing spaces removed (use strip())
# The number of words in the string (use split())
# The string with the first letter of each word capitalized (use title())
# Whether the stripped string starts with "Hello" (use startswith())
# Whether the stripped string ends with "ing." (use endswith())
# The position (index) of the word "Python" in the stripped string (use find())
# The words joined back together separated by " - " (use split() and " - ".join())
def main():
    print("Stripped:", text.strip(" "))
    print("Word count:", len(text.split()))
    print("Title case:", text.capitalize())
    print("Starts with Hello:", text.strip(" ").startswith("Hello"))
    print("End with ing.:", text.strip(" ").endswith("ing."))
    print("Python position:", text.strip(" ").find("Python"))
    print("Joined: ", "-".join(text.split()))

main()