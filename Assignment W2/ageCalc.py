
# Hans Matere SCT 211-0080/2022

from datetime import datetime


def calculateAge(year, month, day):

    currentDate = datetime.now()


    age = currentDate.year - year - ((currentDate.month, currentDate.day) < (month, day))

    return age


def main():
    try:
        print("Welcome to the age calculator please fill in the following fields:")
        year = int(input("Input your year of birth: "))
        month = int(input("Input your month of birth in numbers: "))
        day = int(input("Input your day of birth: "))

        age = calculateAge(year, month, day)
        print("Your are " +str(age)+" years, " +str(month)+ " months and " +str(day)+ " days old !")
    except ValueError:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()



