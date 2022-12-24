import time
import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import datetime


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=''
    while city.lower() not in CITY_DATA.keys():
        print('choose from: chicago, washington or new york city')
        city= input().lower()

        if city=='chicago':
            return city
        elif city=='washington':
            return city
        elif city=='new york city':
            return city
        else:
            print('data only available for: chicago, washington and new york city')

def get_month():
    months={'january':1, 'february':2, 'march':3,'april':4,'may':5,'june':6,'all':7}
    month=''
    while month.lower() not in months.keys():
        print('\n month should be between january to june, \n if you want all the months just type all')
        month=input().lower()

        if month not in months.keys():
            print('your choice not in dataset')

    return month

def get_day():
    # get user input for day of week (all, monday, tuesday, ... sunday)

    day=''
    days={'all':0,'monday':1, 'tuesday':2, 'wednesday':3,'thursday':4,'friday':5,'saturday':6,'sunday':7}
    while day not in days.keys():
        print('\n choose a day and if you want all the days just type all')
        day= input().lower()

        if day.lower() in days.keys():
            return day
        else:
            print('you choice not in dataset')


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


    df= pd.read_csv(CITY_DATA[city])

    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('\n The most popular month:',popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nPopular day:',popular_day)


    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nPopular Start hour:',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_st_sta = df['Start Station'].mode()[0]
    print("\nThe most commonly used start station:" , common_st_sta)


    # display most commonly used end station
    common_end_sta = df['End Station'].mode()[0]
    print("\nThe most commonly used end station:" , common_end_sta)


    # display most frequent combination of start station and end station trip
    df['Start_End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    ensta= df['Start_End'].mode()[0]
    print("\nThe most frequent combination of start station and end station trip:" , ensta)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print('total travel time:', total_travel)


    # display mean travel time
    mean_travel= df['Trip Duration'].mean()
    print('mean travel time:', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type= df['User Type'].value_counts()
    print('each user type counts:',user_type)

    if city == 'chicago' or city == 'new york city':
        # Display counts of gender
        gender= df['Gender'].value_counts()
        print('each user gender counts:',gender)


        # Display earliest, most recent, and most common year of birth

        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        birth_common=df['Birth Year'].mode()[0]

        print('\n The earliest birth year:',earliest,
         '\n The most recent birth yeat:', recent, '\n most common year of birth:',birth_common)

    else:
        print('washington dose not have gender and birth columns')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data (df,answer):

    while answer == 'yes':
        print(df.head())
        break

        if answer == 'no':
            break



def main():
    while True:
        city = get_city()
        month = get_month()
        day = get_day()
        df = load_data(city, month, day)

        if df.empty:
            df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        print('\n do you want do display 5 raws of data? Enter yes or no.\n')
        answer = input().lower()
        display_data(df,answer)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
