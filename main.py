# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm \n')

    a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

    print("'a' is the list: ", a)
    print("that has dimension : ", len(a), "\n")

    print("'a[0]' : ", a[0])
    print("Is the first of the two list conteined in a")
    print("a[0] has dimension : ", len(a[0]), "\n")

    print("'a[0][0]' it's a list: ", a[0][0])
    print("The first of the two list-elements conteined in a[0]")
    print("a[0][0] has dimension : ", len(a[0][0]), "\n")

    print("'a[0][0][0]': ", a[0][0][0])
    print("It's an element of the list a[0][0]")
    print("a[0][0][0] it's not an array, list or something.")
    print("It's not a data structure at all. It's data. Has no dimensions but has a value.\n")

    print("Some printed out random example stuff (see source): ")
    print(a[0][0])
    print(a[1][0])

    print(a[0][0][0])
    print(a[1][0][1])

    print("Manipulating 'a'-like data structures in a fancy old-good-c way:")

    for i in range(len(a)):
        for w in range(len(a[0])):
            for k in range(len(a[0][0])):
                print("a[i][w][k]\t", "a[", i, "][", w, "][", k, "]\t", a[i][w][k])

    print("\n")
    print(a)
    print("\n")

    for i in range(len(a)):
        for w in range(len(a[0])):
            for k in range(len(a[0][0])):
                print("overwrite: a[i][w][k]\t", "a[", i, "][", w, "][", k, "]\t", a[i][w][k])

                a[i][w][k] = int(input("with a[i][w][k]: "))

    print("\n")
    print(a)
    print("\n")

    for i in range(len(a)):
        for w in range(len(a[0])):
            print("overwrite: a[0][w][0]\t", "a[", i, "][", w, "][", 0, "]\t", a[i][w][0])
            a[i][w][0] = int(input("with a[0][w][0]: "))

    print("\n")
    print(a)
    print("\n")
