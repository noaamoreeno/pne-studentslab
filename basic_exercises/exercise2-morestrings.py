text = "  Hello, World! Welcome to Python Programming.  "

def main():
    print("Stripped:", text.strip(" "))
    print("Word count:", len(text.split()))
    print("Title case:", text.capitalize())
    print("Starts with Hello:", text.strip(" ").startswith("Hello"))
    print("End with ing.:", text.strip(" ").endswith("ing."))
    print("Python position:", text.strip(" ").find("Python"))
    print("Joined: ", "-".join(text.split()))

main()