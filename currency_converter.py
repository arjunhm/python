import sys
import requests
from datetime import datetime
import matplotlib.pyplot as plt

#url = 'http://data.fixer.io/api/latest?access_key=77fcf242b180ad7794ea9001c90d21484&format=1/'
#currencies = ['USD', 'EUR', 'JPY', 'GBP', 'CAD', 'CHF']

url = 'http://api.fixer.io/latest'


def check_date(year, month):
    # Performs all the check conditions for a given date
    present = datetime.now()
    end_date = 31

    # To check if the date is valid
    try:
        user_date = datetime(year, month, 1)
    except ValueError:
        print("Enter Valid Date")
        sys.exit(1)

    # To check if the date has passed (can't retrieve future prices)
    if user_date < present:
        user_date = datetime(year, month, 1)
    else:
        sys.exit(1)

    # Set the end date of the month
    for x in range(31, 27, -1):
        try:
            test_date = datetime(year, month, x)
            end_date = x
            break
        except ValueError:
            pass

    return user_date, end_date


def get_historic_currency_rate(from_curr, to_curr, user_date, end_date):

    # Retrieves the daily exchange rates for a given month
    curr_arr = []
    
    for day in range(1, end_date + 1):    
        date = str(user_date.year) + '-' + str(user_date.month) + '-' + str(day)
        query = url + '?base={}&symbols={}&date={}'.format(from_curr, to_curr, date)

        try:
            response = requests.get(query)

            if response.status_code != 200:
                response = 'N/A'
                return response

            else:
                rates = response.json()
                converted_rate = rates["rates"][to_curr]
                curr_arr.append(converted_rate)

        except requests.ConnectionError as error:
            print(error)
            sys.exit(1)

    # Plots the graph of the acquired data
    plt.xlabel('Days')
    plt.ylabel('Rate')
    plt.plot(range(len(curr_arr)), curr_arr)
    plt.show()


def get_currency_rate(from_curr, to_curr):
    # Retrieves the exchange rate between to currencies
    query = url + '?base={}&symbols={}'.format(from_curr, to_curr)

    try:
        response = requests.get(query)

        if response.status_code != 200:
            response = 'N/A'
            return response

        else:
            rates = response.json()
            converted_rate = rates["rates"][to_curr]
            return converted_rate

    except requests.ConnectionError as error:
        print(error)
        sys.exit(1)


def main():

    from_curr = 'EUR' #input('Convert from: ')
    amount = 10.05 #float(input('Amount: '))
    to_curr = 'INR' #input('To: ')
    year = 2018 #int(input('Enter year: '))
    month = 4 #int(input('Enter month: '))
    user_date, end_date = check_date(year, month)
    #"""
    rate = get_currency_rate(from_curr, to_curr)
    print("{} {} = {} {}".format(amount, from_curr, to_curr, rate * amount))
    get_historic_currency_rate(from_curr, to_curr, user_date, end_date)
    #"""

if __name__ == '__main__':
    main()