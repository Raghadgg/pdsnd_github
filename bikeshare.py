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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to see? please choose one: chicago or new york city or washington." + ' ')
        if city not in ('chicago', 'new york city', 'washington'):
            print('Sorry, city not found, please try again.')
            continue
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Choose one month from this list "january, february, march, april, may, june" to filter by or "all".' + ' ')
        if month not in ('january', 'februray', 'march', 'april', 'may', 'june', 'all'):
            print('Sorry, month not found, please try again')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Choose "all" or one day of the week from monday to saturday.'+ ' ')
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print('Sorry, day not found, please try again.')
            continue
        else:
            break


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
        df - Pandas DataFrame containing city data filtered by month and day
    """


    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

# filter by month and day

    if month != 'all':
        months = ['january', 'februray', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station']).count()
    print('Most frequent combination:', frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total travel time:', total)


    # TO DO: display mean travel time
    travelmean = df['Trip Duration'].mean()
    print('Mean travel time:', travelmean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:', user_types)

    try:
        gender = df['Gender'].value_counts()
        print('Gender:',gender)
    except KeyError:
        print('No gender data available')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('Earliest birth year:', earliest_year)
    except KeyError:
        print('No data available for birth year')

    try:
        recent_year = df['Birth Year'].max()
        print('Most recent birth year:', recent_year)
    except KeyError:
        print('No data available for birth year')

    try:
        common_year = df['Birth Year'].mode()[0]
        print('Most common year of birth:', common_year)
    except KeyError:
        print('No data available for birth year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view_data = input('Would you like to view 5 rows of individual trip data? yes or no' + ' ')
    start_loc = 0

    while True:
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input('Do you want to continue? yes or no' + ' ').lower()
        if view_display != 'yes':
            break






def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
