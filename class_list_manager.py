# Class List Manager - Group 1
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]


# ===== Each student adds her function BELOW this line =====

# Written by: Aseel (Task 1)
def count_names(names):
    return len(names)


# Sara - Task 2: search_name


# Alulu - Task 3: sort_names
def sort_names(names):
    return sorted(names)


# Ayan - Task 8: remove_duplicates

def remove_duplicates(names):
    new_names = []
    for name in names:
        if name not in new_names:
            new_names.append(name)
    return new_names


# ===== Each student adds her function ABOVE this line =====


def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)

    print("Number of names:", count_names(names))

    # Other students will add their function calls here
    print("Names in alphabetical order:", sort_names(names))
    print("Names without duplicates:", remove_duplicates(names))

main()
