print("Learn your squares and cubes!")

continuing = "Y"
while continuing == "Y":
    number = int(input("Please enter an integer: "))

    header = print("Number\tSquared\tCubed")
    for i in range(1, number + 1):
        squared = i ** 2
        cubed = i ** 3
        print(f"{i}\t\t{squared}\t\t{cubed}")

    continuing = input("Do you want to continue? Y/N")
if continuing == str("N"):
    print("Done.")



