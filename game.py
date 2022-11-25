"""
Sam A01337600
Wilson A01266055

"""

import itertools

choices = []
boolean_generator = itertools.cycle([True, False])
for _ in range(20):
    choices.append(next(boolean_generator))

print(choices)




def main():
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

