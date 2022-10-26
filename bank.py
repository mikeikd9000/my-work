# Prompt user for input
user_input = input("Greetings: ").lower().strip()

if user_input.startswith("hello"):
    print ("$0")
elif user_input.startswith("h"):
    print ("$20")
else:
    print ("$100")