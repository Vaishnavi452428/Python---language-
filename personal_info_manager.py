# Personal Information Manager

# Ask the user for their information
name = input("Enter your name:vaishnavi ")
age = input("Enter your age:23 ")
city = input("Enter your city:tirupati ")
hobbies = input("Enter your hobbies (comma separated):singing,reading books ")

# Format the output
print("\n--- Personal Information ---")
print(f"Name: {vaishnavi}")
print(f"Age: {23}")
print(f"City: {tirupati}")
print("Hobbies:singing,reading books")

# Split hobbies and display them nicely
hobby_list = hobbies.split(",")
for hobby in hobby_list:
    print(f" - {hobby.strip()}")

print("\nThank you for using the Personal Information Manager!")