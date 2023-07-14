from tests.ILS import Ils
from tests.USD import USD
print("welcome to currency converter")
print("please choose an option 1/2:\n 1. dollars to shekels\n 2.shekels to dollars\n")
results = []
def SaveList_to_File(results,results.txt):
    with open(results.txt,'w') as file:
        for item in results:
            file.write(str(item) + "\n")
def CashMachine():
    while True:
        try:
          answer = int(input())
          if answer not in [1, 2]:
               raise ValueError()

          if answer == 1:
            value_to_convert = float(input("please enter an amount to convert\n"))
            converted_value =Ils.calculate(value_to_convert=value_to_convert)
            print(converted_value)
            results.append(converted_value)
          elif answer == 2:
            value_to_convert = float(input("please enter an amount to convert\n"))
            converted_value = USD.calculate(value_to_convert=value_to_convert)
            print(converted_value)
            results.append(USD.calculate(value_to_convert=value_to_convert))

          break
        except ValueError:
            print("Please try again - only allowed to select 1 or 2\n")


CashMachine()


print("would you like to start over?\nY/N?\n")
answer2 = input("")
while True:
    if 'Y' in answer2:
        CashMachine()
    elif 'N' in answer2:
        print("thank you for using our currnecy convertor")
        print(results)
        SaveList_to_File(results,results.txt)

    break
















