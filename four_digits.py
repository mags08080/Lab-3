#four_digits.py
def four_digits():
  digits = int(input("Enter a 4 digit integer number: "))
  if digits > 999:
    digit1 = digits // 1000
    digit2 = (digits % 1000) // 100
    digit3 = (digits % 100) // 10
    digit4 = digits % 10
    print(f"The individual digits of your input are: {digit1}, {digit2}, {digit3}, {digit4}")
    print(f"The sum of your input is: {digit1 + digit2 + digit3 + digit4}")
  else:
    print("Your input was not four digits. Quitting.")
four_digits()