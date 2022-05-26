# Author: Matthew Spiller
# Data Modified: April 28, 2022

# University Administration Tuition Income Calculator
# Description: Calculates the revenue earned by a university based on the average tuition amount and the predicted enrolment each year. It is assumed that tuition will grow at a fixed rate based on the average growth from previous years (based on the initial tuition inputs).

CONST_ID_LEN = 9
CONST_MIN_PREVIOUS_YEARS = 2
CONST_MAX_PREVIOUS_YEARS = 6
BASELINE_TUITION = 1000 # tuition cannot be lower than this amount. If current year tuition is calculated as lower than this amount, it will default to this value
ENROLMENT_GROWTH_PER_YEAR = 100

# check to make sure the ID is the correct number of digits (9 in this case)
def student_id():
    print("Please enter your student ID: ", end='')
    id = int(input())

    while len(str(id)) != CONST_ID_LEN:
        print("Student ID must be " + str(CONST_ID_LEN) + " digits long. Please try again.")
        print("Please enter your student ID: ", end='')
        id = input()

    return id

# checks to make sure that the entry of previous years is between the minimum and maximum previous year values (in this case between 2 and 6)
def num_of_previous_years():
    print("Please enter the number of years as inputs: ", end='')
    years = int(input())

    # if the number of years entered isn't within the bounds, user is prompted to enter again.
    while years < CONST_MIN_PREVIOUS_YEARS or years > CONST_MAX_PREVIOUS_YEARS:
        print("The number of years must be between " + str(CONST_MIN_PREVIOUS_YEARS) + " and " + str(CONST_MAX_PREVIOUS_YEARS) + ". Please try again.")
        print("Please enter the number of years as inputs: ", end='')
        years = int(input())

    # return the value if the input is valid
    return years

# stores the previous years tuition in a list and returns the list
def previous_years_tuition_input(years):
    previous_years_tuition = []
    for i in range(years):
        print("Please enter Year " + str(i+1) + " tuition: ", end='')
        tuition = input()
        previous_years_tuition.append(tuition)
    return previous_years_tuition

# this formats the revenue string such that it contains commas every 3 characters, as large numbers usually do
def get_revenue_str(revenue):
    revenue = str(int(revenue))
    length = len(revenue)
    digits_before_comma = length % 3

    # these 3 if/elif/else statements add the first few digits before the first comma
    if(digits_before_comma == 0):
        new_revenue_string = revenue[0] + revenue[1] + revenue[2] + ','
        digits_used = 3
    elif(digits_before_comma == 1):
        new_revenue_string = revenue[0] + ','
        digits_used = 1
    else:
        new_revenue_string = revenue[0] + revenue[1] + ','
        digits_used = 2

    # this adds the rest of the digits, adding a comma every 3 digits
    for i in range(length - digits_used):
        if i % 3 == 0 and i > 2:
            new_revenue_string = new_revenue_string + ','
            new_revenue_string = new_revenue_string + revenue[digits_used + i]
        else:
            new_revenue_string = new_revenue_string + revenue[digits_used + i]

    return new_revenue_string

# This function calculates the tuition increment by summing up the differences between tuition each year. It then
# divides the summation of differences by (number_of_previous_years - 1), which is the number of differences included
# in the summation, to get the increment. The tuition each year is calculated as the previous years tuition plus
# the increment.
def calculate_forecasted_revenue(number_of_previous_years, previous_years_tuitions, number_of_forecasted_years, number_of_students):
    sum_of_previous_years_tuition_increments = 0
    for i in range(number_of_previous_years - 1):
        sum_of_previous_years_tuition_increments += (int(previous_years_tuitions[i+1]) - int(previous_years_tuitions[i]))

    # This pertains to the tuition growth. Enrolment growth is stored as a constant.
    increment_per_year = float(sum_of_previous_years_tuition_increments) / (number_of_previous_years - 1)

    last_years_tuition = float(previous_years_tuitions[len(previous_years_tuitions) - 1])
    last_years_enrolment = number_of_students

    print("*** CALCULATING ***")

    for i in range(number_of_forecasted_years):
        this_years_tuition = last_years_tuition + increment_per_year
        this_years_enrolment = last_years_enrolment + ENROLMENT_GROWTH_PER_YEAR
        if(this_years_tuition < BASELINE_TUITION):
            this_years_tuition = BASELINE_TUITION
        this_years_revenue = get_revenue_str(this_years_enrolment * this_years_tuition)
        print("Year " + str((i + number_of_previous_years + 1)) + " forecasted tuition: $" + "%.2f" % this_years_tuition)
        print("Year " + str((i + number_of_previous_years + 1)) + " forecasted enrolment: " + str(this_years_enrolment))
        print("Year " + str((i + number_of_previous_years + 1)) + " forecasted revenue: $" + this_years_revenue)
        last_years_tuition = this_years_tuition
        last_years_enrolment = this_years_enrolment

# runs the forecast program. No need to re-enter name and student number on re-runs.
def run_forecast():
    number_of_previous_years = num_of_previous_years()
    previous_years_tuition = previous_years_tuition_input(number_of_previous_years)

    print("Please enter current student enrolment: ", end='')
    number_of_students_enrolled = int(input())

    print("Please enter number of years to forcast: ", end='')
    number_of_forecast_years = int(input())

    calculate_forecasted_revenue(number_of_previous_years, previous_years_tuition, number_of_forecast_years, number_of_students_enrolled)

# THE PROGRAM BEGINS HERE
print("Please enter your name: ", end='')
name = input()

# the student ID isn't used for anything, so it doesn't need to be stored, however this can easily be changed in the future
student_id()

print("*** Access Granted ***")
print("Welcome " + name + " to the Revenue Forecasting Tool!")

run_again = 'y'
while(run_again == 'y'):
    run_forecast()
    print("Would you like to do another forecast (y,n): ",end='')
    run_again = input()
    while run_again != 'y' and run_again != 'n':
        print("Please enter 'y' or 'n'")
        print("Would you like to do another forecast (y,n): ", end='')
        run_again = input()

print("Goodbye!")





