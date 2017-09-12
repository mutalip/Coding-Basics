'''
This program will calculate a payroll for a small company. The program pseudo code is:
1. Prompt the user for an employee ID string or "end" to exit
    1a. If user enters zero then go to step 7.
2. Prompt the user for hours worked and for pay rate per hour.
3. Calculate weekly pay:
    3a. If hours are greater than 40 then get overtime hours
    3b. Calculate pay for overtime hours at 1.5 times regular pay
    3c. Calculate pay for regular hours
    3d. Add overtime and regular pay together
4. Save ID number and total weekly pay
5. Add weekly pay to final total
6. Go back to step 1
7. Loop through all employee list and print ID and weekly pay
8. Print total pay
'''

# Data variables
# employeepay[] - this will hold the employee id number and weekly pay and is a Dictionary
# totalpay - this will hold the total pay and is a float
# moreemployees - this is a boolean used to control the loop
# empid - this a string that holds the employee id
# hours - this is an integer that holds the hours worked
# hourpay - this is a float that holds the hourly pay rate
# weeklypay - this is a float holding weekly pay
# overtimepay - this is a float holding the overtime pay

moreemployees = True        # initially set to true
employeepay = {}            # define data structure
totalpay = 0                # set total pay to zero

print("Enter employee ID or Name or END to stop entering employees: ")
while moreemployees:
    # prompt for employee id
    empid = input("Enter employee ID or Name or END: ")
    #check for the word "end"
    if empid.upper() == "END":
        moreemployees = False
    else:
        # prompt for hours worked and hourly pay
        hours = int( input("Enter hours worked: "))
        hourpay = float( input("Enter hourly pay rate: "))

        # calculate overtime if hours > 40
        overtimepay = 0     # assume is zero
        if hours > 40:
            overhours = hours - 40
            overpayrate = hourpay * 1.5
            overtimepay = overhours * overpayrate

        # calculate weekly pay and add to totalpay
        weeklypay = hours * hourpay + overtimepay
        totalpay = totalpay + weeklypay

        # save in dictionary using ID as the index
        employeepay[ empid ] = weeklypay

    print("............. \n")

# we will end up here when END was entered and stopped the loop
print("--------------------------\n")
# the for loop will retrieve each element in the dictionary as an idx (employee id) and val (employee weekly pay)
for idx, val in employeepay.items():
    print(" Employee {0} will be paid ${1:8.2f} this week ".format(idx, val))

print("Total pay is ${0:8.2f}".format(totalpay))
