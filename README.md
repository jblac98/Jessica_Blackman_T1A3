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
- pip install argparse

2. Use the main.py script to start the Habit Tracker
- python3 src/main.py <command> [option]

3. Add a new habit to the Habit Tracker
- python3 src/main.py add running --duration 25 --frequency 4

4. Remove an exisiting habit from the Habit Tracker
- python3 src/main.py remove <habit_name>
Example: python3 src/main.py remove running

5. View all habits in the Habit Tracker
- python3 src/main.py view (this will show all the existing habits you have entered)

6. Edit an existing habit in the Habit Tracker
- python3 src/main.py <habit_name> --new_name <new_name> --new_duration <new_duration> --new_frequency <new_frequency>
Example: python3 src/main.py running --new_duration 35

Additional notes:
JSON file: All habits are stored in a file called 'data/habits.json'.
Error handling: Anytime a common error is made such as missing the required argument.

The habit tracker allows you to efficiently manage your habits through the command line. It successfully manages your habits and provides feedback on the actions you have made towards your habit. 

## Trello
- The project management tool to assist with managing the progress and timeline of the terminal applicaiton.


