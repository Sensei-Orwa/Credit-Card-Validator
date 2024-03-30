#CREDIT CARD VALIDATOR

#Remove any "-" or " "
#Add all digits in the odd places from right to left
#Double every second digit from right to left
#id the result is a two digit number, add the two numbers to get a single digit
#Sum the totals of step 2 & 3
#If sum is divisible by 10, the credit card # is valid

sum_odd_digits = 0
sum_even_digits = 0
Total = 0

#Step 1
card_number = input("Enter credit card number: ")
card_number = card_number.replace(" ", "").replace("-", "")
print(card_number)