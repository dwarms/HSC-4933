#########################################################
# Darcy Warms # darcywarms@usf.edu                      #
# Lab 2 Functions User Input, and Readable, Usable Code #
#########################################################

heart_rate_samples = {
    "J. Alvarez": [72, 75, 78],
    "M. Chen": [80, 82],
    "R. Okafor": [65, 68, 70, 66],
    "S. Patel": [90, 95, 92, 88, 91],
    "T. Nguyen": [77, 79],
    "L. Kowalski": [68, 70, 69],
    "D. Osei": [98, 101, 95, 99],
    "A. Whitfield": [74, 76, 75, 73],
}


def patient_stats(*readings: int) -> tuple:
    total = 0
    for reading in readings:
        total += reading

    average = total / len(readings)
    minimum = min(readings)
    maximum = max(readings)

    return average, minimum, maximum


patient = input("Enter patient name: ")
readings = heart_rate_samples[patient]

choice = input("Enter all, average, minimum, or maximum: ")

average, minimum, maximum = patient_stats(*readings)

if choice == "all":
    print("Heart rate readings:", readings)
    print("Average:", average)
    print("Minimum:", minimum)
    print("Maximum:", maximum)

elif choice == "average":
    print("Average:", average)

elif choice == "minimum":
    print("Minimum:", minimum)

elif choice == "maximum":
    print("Maximum:", maximum)

else:
    print("Invalid choice")