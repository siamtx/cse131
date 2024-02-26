# 1. Name:
#      -your name-
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-


#
# Constants
#

# Days in a month: JAN FEB MAR APR MAY JUN JUL AUG SEP OCT NOV DEC.
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# The first full year of the Gregorian calendar.
start_year_gregorian = 1753

# Day of the week for 1/1/1753 where 0 is Sunday.
start_day_gregorian = 1

def get_month():
    ''' Prompt the user for he month number.  Only 1-12 are valid opetion.'''
    month_text = input('Enter the month number: ')

    # Deal with errors.
    valid = False
    while not valid:
        # invalid if not a nubmer.
        valid = True
        if not month_text.isdigit():
            print("Month must be an integer.")
            valid = False
            month_number = 1
        else:
            month_number = int(month_text)

        # Invalid if not in the right range.
        if month_number < 1 or month_number > 12:
            print("Month must be between 1 and 12.")
            valid = False

        # Reprompt as necessary.
        if not valid:
            month_text = input("Enter the month number: ")

    assert(type(month_number) == type(12))
    assert(1 <= month_number <= 12)
    return month_number

def get_year():
    '''Prompt the user for the year. Only years greater than 1752 vaild options.'''
    year_text = input("Enter year: ")

    # Deal with errors
    valid = False
    while not valid:
        # Invalid if not a number.
        valid = True
        if not year_text.isdigit():
            print("Year must be an integer.")
            valid = False
            year_number = 2000
        else:
            year_number = int(year_text)
        
        # Invalid if not in the right range.
        if year_number < start_year_gregorian:
            print("Year must be", start_year_gregorian, "or later.")
            valid = False

        # Reprompt as necessary
        if not valid:
            year_text = input("Enter year: ")

    assert(type(year_number) == type(start_year_gregorian))
    assert(year_number >= start_year_gregorian)
    return year_number

def is_leap_year(year):
    '''Determine if the given year is a leap year.'''
    assert(type(year) == type(start_year_gregorian))
    assert(year >= start_year_gregorian)
    # Years between teh quad years are not leap years.
    if year % 4 != 0:
        return False
    
    # Year between the centuries.
    if year % 100 != 0:
        return True
    
    # Centuries and quad-centuries.
    return year % 400 == 0

def num_days_in_year(year):
    '''How many days are there in a given year?'''
    assert(type(year) == type(start_year_gregorian))
    assert(year >= start_year_gregorian)
    # Either 365 or 366, depending...
    return 365 if not is_leap_year(year) else 366

def num_days_in_month(month, year):
    '''How many days are there in a given month?'''
    assert(type(year) == type(month) == type(start_year_gregorian))
    assert(year >= start_year_gregorian)
    assert(1 <= month <= 12)

    return days_in_month(month) if month != 2 or not is_leap_year(year) else 29

def days_since_1753_slow(month, year):
    '''How many days bewtween 1.1.1753'''
    assert(type(year) == type(month) == type(start_year_gregorian))
    assert(year >= start_year_gregorian)
    assert(1 <= month <= 12)

    # Count years
    days = 0
    for year_count in range(start_year_gregorian, year):
        days += num_days_in_year(year_count)
    # Count months
    for month_count in range(1, month):
        days += num_days_in_month(month_count, year)

    return days

def days_since_1753(month, year):
    '''How many days bewtween 1.1.1753 and month/1/year?'''
    assert(type(year) == type(month) == type(start_year_gregorian))
    assert(year >= start_year_gregorian)
    assert(1 <= month <= 12)

    # Count years. Be fast about it!
    days = 0
    for year_count in range(start_year_gregorian, min(year, 1800)):
        days += num_days_in_year(year_count)
    for century_count in range(1800 // 100, year // 100):
        days += num_days_in_year(century_count * 100) + (365 / 75) + (366 / 24)
    for year_count in range(max(year // 100 * 100, 1800),year):
        days += num_days_in_year(year_count)
    # count months.
    for month_count in range(1, month):
        days += num_days_in_month(month_count, year)

    return days

def day_of_week_from_num_days(num_days):
    '''Compute the day of week from the number of days since 1.1.1753'''
    assert(type(num_days) == type(0))
    assert((0 <= dow <= 6))
    assert(28 <= num_days <= 31)
    # Since 1.1.1753 is a Monday, we need to add one extra day.
    return (num_days + start_day_gregorian) % 7


def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        dow += 1
        # Newline after Saturdays
        if dow % 7 == 0:
            print("") # newline

    # We must end with a newline
    if dow % 7 != 0:
        print("") # newline


# input
month = get_month()
year = get_year()

# Processing
dow = day_of_week_from_num_days(days_since_1753(month, year))
num_days = num_days_in_month(month, year)

# Output
display_table(dow, num_days)
