# Your name: Antony Wu
# Your student id: 0439 9524
# Your email: antonywu@umich.edu
# List who you have worked with on this project: Phillip Ripsam-Walsh

import sqlite3
import json
import os
import requests
import re
import matplotlib
import matplotlib.pyplot as plt


def main():
    conn = sqlite3.connect('covid.db')
    c = conn.cursor()

    c.execute("SELECT Covid_Data.date, Covid_Data.newCases, Stock_Data.changePrice FROM Covid_Data JOIN Stock_Data ON Covid_Data.date = Stock_Data.date")

    results = c.fetchall()
    conn.close()

    avgChangePerMonth = {}
    sum_change = 0
    day_counter = 0
    curr_month = 1
    for day in results:
        month = day[0] // 100
        if curr_month != month:
            avgChangePerMonth[curr_month] = sum_change / day_counter
            sum_change = 0
            curr_month = month
            day_counter = 0
        sum_change += day[2]
        day_counter = day_counter + 1
        if day == results[-1]:
            avgChangePerMonth[curr_month] = sum_change / day_counter
            sum_change = 0
            curr_month = month
            day_counter = 0

    avgCasesPerMonth = {}
    sum_change = 0
    day_counter = 0
    curr_month = 1
    for day in results:
        month = day[0] // 100
        if curr_month != month:
            avgCasesPerMonth[curr_month] = sum_change / day_counter
            sum_change = 0
            curr_month = month
            day_counter = 0
        sum_change += day[1]
        day_counter = day_counter + 1
        if day == results[-1]:
            avgCasesPerMonth[curr_month] = sum_change / day_counter
            sum_change = 0
            curr_month = month
            day_counter = 0

    print("Average New Covid Cases and Expedia Price Changes in 2020: ")
    print()
    for i in range(1, len(avgCasesPerMonth)+1):
        if i == 1:
            print("January: ")
        elif i == 2:
            print("February: ")
        elif i == 3:
            print("March: ")
        elif i == 4:
            print("April: ")
        elif i == 5:
            print("May: ")
        elif i == 6:
            print("June: ")
        elif i == 7:
            print("July: ")
        elif i == 8:
            print("August: ")
        elif i == 9:
            print("September: ")
        elif i == 10:
            print("October: ")
        elif i == 11:
            print("November: ")
        elif i == 12:
            print("December: ")

        print("Average Cases Per Day: " + str(avgCasesPerMonth[i]))
        print("Average Expedia Price Change Per Day: " + str(avgChangePerMonth[i]))
        print()


    x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
         "Aug", "Sep", "Oct", "Nov", "Dec"]
    y = [avgChangePerMonth[1],avgChangePerMonth[2],avgChangePerMonth[3],avgChangePerMonth[4],avgChangePerMonth[5],avgChangePerMonth[6],avgChangePerMonth[7],avgChangePerMonth[8],avgChangePerMonth[9],avgChangePerMonth[10],avgChangePerMonth[11],avgChangePerMonth[12]]

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Month')
    ax.set_ylabel('Average Daily Change of Expedia Stock')
    ax.set_title('Average Daily Change of Expedia Stock Per Month In 2020')
    ax.grid()


    x1 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
         "Aug", "Sep", "Oct", "Nov", "Dec"]
    y2 = [avgCasesPerMonth[1],avgCasesPerMonth[2],avgCasesPerMonth[3],avgChangePerMonth[4],avgCasesPerMonth[5],avgCasesPerMonth[6],avgCasesPerMonth[7],avgCasesPerMonth[8],avgCasesPerMonth[9],avgCasesPerMonth[10],avgCasesPerMonth[11],avgCasesPerMonth[12]]

    fig1, ax1 = plt.subplots()
    ax1.plot(x1, y2)
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Average Daily New Covid Cases')
    ax1.set_title('Average Daily New Covid Cases Per Month In 2020')
    ax1.grid()
    plt.show()


if __name__ == "__main__":
    main()
