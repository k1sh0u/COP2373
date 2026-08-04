'''
Write a program (function) to create a database called population_(your initials). For ex: population_SM would be my database. Create a table named population with the following fields; 1. city, 2. year, 3. population. Choose 10 cities in Florida and insert data into the population table for the year 2023.

Create a function to the simulate population growth and decline for the next 20 years at various rates for each year. Insert this data into the population table.

Using matplotlib, create a function to show the population growth for a city. Let the user know the 10 cities as options and ask them to choose one and display the population growth for the city visually.

This assignment will have at least three functions.

Submit your .py file in this assignment and in your repository.
'''
import random
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

def setup()
        conn = sqlite3.connect('population_EL.db')

        cursor = conn.cursor()

        cursor.execute('DROP TABLE IF EXISTS population')

        cursor.execute('''
        CREATE TABLE population (
            city TEXT,
            year INTEGER,
            population INTEGER)
        ''')

        city_data = [
                ('Tampa', 2026, 419635),
                ('Miami', 2026, 499943),
                ('Orlando', 2026, 340004),
                ('Jacksonville', 2026, 1032061),
                ('Sarasota', 2026, 59000),
                ('Bradenton', 2026, 57000),
                ('St. Petersburg', 2026, 266670),
                ('Fort Lauderdale', 2026, 190168),
                ('Pensacola', 2026, 54608),
                ('Tallahassee', 2026, 206428)
            ]

        cursor.executemany('INSERT INTO population VALUES (?,?,?)', city_data)

        conn.commit()
        conn.close()

def sim_pop_growth():
        rate = (float(random.randint(-10,10))/100)
        years = 20
        new_data = []

        conn = sqlite3.connect('population_EL.db')
        cursor = conn.cursor()
        cursor.execute(
                "SELECT city, population FROM population WHERE year = 2026"
        )



        current_city_data = cursor.fetchall()

        for city, pop in current_city_data:
                current_population = float(pop)

                for year in range(0, years):
                        current_pop = current_pop * (1 + rate)
                        new_data.append(city, (year + 1), int(current_pop))

        cursor.executemany("INSERT INTO population VALUES (?,?,?)", new_data)

        conn.commit()
        conn.close()

