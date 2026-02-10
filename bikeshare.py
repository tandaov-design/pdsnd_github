import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        data - Pandas DataFrame containing city data filtered by month and day
    """


    return data


def time_stats(data):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    analysis_start_time = time.time()

    # display the most common months


    # display the most common day of weeks


    # display the most common start hours


    print("\nThis took %s seconds." % (time.time() - analysis_start_time))
    print('-'*40)


def station_stats(data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    analysis_start_time = time.time()

    # display most commonly used start stations


    # display most commonly used end stations


    # display most frequent combination of start station and end station trips


    print("\nThis took %s seconds." % (time.time() - analysis_start_time))
    print('-'*40)


def trip_duration_stats(data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    analysis_start_time = time.time()

    # display total travel times


    # display mean travel times


    print("\nThis took %s seconds." % (time.time() - analysis_start_time))
    print('-'*40)


def user_stats(data):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    analysis_start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - analysis_start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        data = load_data(city, month, day)

        analytis_time_stats(data)
        analytis_station_stats(data)
        analytis_trip_duration_stats(data)
        analytis_user_stats(data)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
