# Jessica_Blackman_T1A3

## Prerequisites
- Python3 + Venv

## Installation Steps
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## To deactivate venv
- `deactivate`

## Instructions on using the Habit Track terminal applicaiton
1. If you haven't already, install:
- pip install pandas
- pip install tabulate

2. Use the main.py script to start the Habit Tracker
- python3 src/main.py <command> [option]

3. Add a new habit to the Habit Tracker
- python3 src/main.py add running --duration 25 --frequency 4

4. Remove an exisiting habit from the Habit Tracker
- python3 src/main.py remove <habit_name>
Example: python3 src/main.py remove running

5. View all habits in the Habit Tracker
- python3 src/main.py view (this will show all the existing habits you have entered)

6. 
