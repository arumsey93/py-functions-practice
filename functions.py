def create_person(first_name, last_name, age, occupation):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "occupation": occupation,
    }

melissa = create_person("Melissa", "Bell", 25, "Software Developer")

'''
Define four Python functions named run, swing, slide, and hide_and_seek. Each function should take a child's name as an argument. Each function should print that the child performed the activity.

For example, Jay ran like a fool! or Chantelle slid down the slide!.

The following lists of children should be iterated, and the names sent to the appropriate functions.

running_kids = ["Pam", "Sam", "Andrea", "Will"]
swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]
'''
running_kids = ["Pam", "Sam", "Andrea", "Will"]

# for name in running_kids:
#     print(f"{name} ran like a fool!")

def run():
    for name in running_kids:
        print(f"{name} ran like a fool!")
run()

swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]

# for name in swinging_kids:
#     print(f"{name} slide down the slide!")

def swing():
    for name in swinging_kids:
        print(f"{name} slide down the slide!")
swing()

sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]

# for name in sliding_kids:
#     print(f"{name} committed espionage against the United States!")

def slide():
    for name in sliding_kids:
        print(f"{name} committed espionage against the United States!")
slide()

hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

# for name in hiding_kids:
#     print(f"{name} is hiding from their own death!")

def hide():
    for name in hiding_kids:
        print(f"{name} is hiding from their own death!")
hide()