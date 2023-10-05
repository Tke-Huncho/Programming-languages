

#Hans Matere SCT 211-0080/2022

def calculateTip(totalBill, tipPercentage, numPeople):
    tipAmount = totalBill * (tipPercentage / 100)
    totalAmount = totalBill + tipAmount
    amountPerPerson = totalAmount / numPeople
    return round(amountPerPerson,2)

def main():
    try:
        totalBill = float(input("Enter the total bill amount: "))
        tipPercentage = int(input("Enter the tip percentage (10, 12, or 15): "))

        if tipPercentage not in [10, 12, 15]:
            print("Invalid tip percentage. Please choose 10, 12, or 15.")
            return

        numPeople = int(input("Enter the number of people splitting the bill: "))

        amountPerPerson = calculateTip(totalBill, tipPercentage, numPeople)

        print("Each person should pay: " +str(amountPerPerson))

    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()




