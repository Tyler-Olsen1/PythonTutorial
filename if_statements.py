
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else :
    print("You are neither a male nor are you tall")


if is_male and is_tall:
    print("You are a tall male")
else :
    print("You aren't tall AND male")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are male, but not tall")
elif not(is_male) and is_tall:
    print("You are tall, but not male")
else:
    print("You are neither tall nor male")




