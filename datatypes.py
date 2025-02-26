import os

# Correct these values, then run the program.
name = None
height = None
age = None
year12 = None


# DON'T TOUCH BELOW THIS COMMENT
def Check(name, height, age, year12):
    os.system("clear")
    try:
        score = 0
        if not isinstance(name, str):
            print("name var is wrong, it should be a string.")
        else:
            score += 1
        if not isinstance(height, float):
            print("height var is wrong, it should be a float.")
        else:
            score += 1
        if not isinstance(age, int):
            print("age var is wrong, it should be an int.")
        else:
            score += 1
        if not isinstance(year12, bool):
            print("year12 var is wrong, it should be a bool.")
        else:
            score += 1
        if score == 4:
            print("Congratulations you passed 4/4 tests, you can move on.")
        else:
            print(f"You passed {score}/4 tests, try again.")
        input(">")
    except Exception as e:
        print(e)


Check(name, height, age, year12)
