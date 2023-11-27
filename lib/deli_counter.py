def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        answer = "The line is currently:"
        for index, name in enumerate(katz_deli):
            answer += f" {index + 1}. {name}"

        print(answer)

def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    position = len(katz_deli)
    print(f"Welcome, {new_person}. You are number {position} in line.")


def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print(f"There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)