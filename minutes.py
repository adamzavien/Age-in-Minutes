from datetime import date, datetime
import sys, inflect


def main():

    # ensure user input date format : YYYY-MM-DD
    dob = input("Date of Birth: ")

    valid_format(dob)

    # convert the date of birth string to a datetime object
    dob = datetime.strptime(dob, "%Y-%m-%d").date()

    current_date = date.today() # get current date

    # Calculate the difference in minutes
    difference_minutes = (current_date - dob).total_seconds() // 60

    # Convert the minutes to English words
    p = inflect.engine()
    minutes_in_words = p.number_to_words(int(difference_minutes)).capitalize().replace(" and", "").strip()

    print(f"Difference in minutes since Date of Birth : {minutes_in_words} minutes")


def valid_format(dob):

    try:
        format = '%Y-%m-%d'

        if datetime.strptime(dob, format):
            return True

    except ValueError:
        sys.exit("Invalid date")



if __name__ == "__main__":
    main()