import name_module
name = input("Enter your name: ")
print(name_module.ispalindrome(name))
print("No of vowels:", name_module.count_the_vowels(name))
print("Frequency of letters:")

frequency = name_module.frequency_of_letters(name)
for letter, count in frequency.items():
    print(f"{letter}-{count}", end=", ")
