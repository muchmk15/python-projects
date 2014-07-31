
name = input("What's your name?")
name = name.strip().title()

print("Nice to meet you " + name)

age = input("How old are you?")
print("Interesting, you are " + age + " years old.")

age = int(age)

days_in_year = 365.242
days_old = age * days_in_year

print("You are " + str(days_old) + " days old")


