katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:"
        for i in range(len(katz_deli)):
            message += f' {i + 1}. {katz_deli[i]}'
        print(message) 


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {katz_deli.index(name) + 1} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        katz_deli.pop(0)

