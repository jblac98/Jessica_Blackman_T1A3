import argparse
from datetime import datetime
import json
import pandas as pd
from tabulate import tabulate

class Habit:
    def __init__(self, name, start_date, frequency_weekly, duration_minutes, form_habit=True):
        """
        To create a habit.

        - name of habit
        - the start date for the habit
        - how oftern per week the habit is being done
        - how long in minutes the habit is being performed
        """
        self.name = name
        self.start_date = start_date
        self.frequency_weekly = frequency_weekly
        self.duration_minutes = duration_minutes
        self.form_habit = form_habit

    def __str__(self):
        """
        Return the name of the habit when the object is printed as a string.
        """
        return self.name
    
    def serialize(self):
        """
        To serialize the habit suitable for a JSON file.
        """
        return {
            'name': self.name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),  # Serialize datetime to string
            'frequency_weekly': self.frequency_weekly,
            'duration_minutes': self.duration_minutes,
            'form_habit': self.form_habit
        }

    def get_habit_dict(self):
        """
        To create a dictionary with calculated fields.
        """
        time_elapsed = (datetime.now() - self.start_date).total_seconds()
        hours = round(time_elapsed / 60 / 60, 1)
        days = round(hours / 24, 2)
        weeks = round(days / 7, 2)

        days_to_go = round(21 - days)

        if hours > 72:
            hours = str(days) + " days"
        else:
            hours = str(hours) + " hours"

        minutes_spent = weeks * self.duration_minutes * self.frequency_weekly

        if self.form_habit:
            return {"habit": self.name, "frequency": self.frequency_weekly, "duration": self.duration_minutes,
                    "time_since": hours, "days_remaining": days_to_go, "minutes_spent": minutes_spent}
        else:
            return {"habit": self.name, "frequency": self.frequency_weekly, "duration": self.duration_minutes,
                    "time_since": hours, "days_remaining": days_to_go, "minutes_saved": minutes_spent}

class HabitTracker:
    
    def __init__(self):
        """
        A list to store habits.
        """
        self.habits = []

    def add_habit(self, name, duration, frequency):
        """
        Add a new habit to the tracker. 

        Adds a habit with the fields below. 
        """
        habit = Habit(name, datetime.now(), duration, frequency)
        self.habits.append(habit)
        print(f"Added new habit: '{name}', duration: '{duration}', frequency: '{frequency}'")
        self.save_habits()

    def save_habits(self):
        """
        Save the current list of habits to a JSON file. 

        """
        with open('data/habits.json', 'w') as file:
            serialized_habits = [habit.serialize() for habit in self.habits]
            json.dump(serialized_habits, file, indent=4)


    def load_habits(self):
        """
        Load habits from a JSON file into self.habits.  
        """
        try:
            with open('data/habits.json', 'r') as file:
                habits_data = json.load(file)
                self.habits = []
                for habit_data in habits_data:
                    habit_data['start_date'] = datetime.strptime(habit_data['start_date'], '%Y-%m-%d')
                    habit = Habit(**habit_data)
                    self.habits.append(habit)
        except FileNotFoundError:
            self.habits = []

    def view_habits(self):
        """
        Display all habits in self.habits in a tabular format.
        """
        if not self.habits:
            print("No habits found.")
        else:
            df_form_habits = pd.DataFrame([habit.get_habit_dict() for habit in self.habits])
            print(tabulate(df_form_habits, headers="keys", tablefmt="psql"))

    def remove_habit(self, name):
        """
        Remove a habit from self.habits by it's name. 
        """
        self.habits = [habit for habit in self.habits if habit.name != name]
        self.save_habits()

    def edit_habit(self, name, new_name=None, new_duration=None, new_frequency=None):
        """
        To edit an existing habit.
        """
        habit = next((habit for habit in self.habits if habit.name == name), None)
        if habit:
            if new_name:
                habit.name = new_name
            if new_duration:
                habit.duration_minutes = new_duration
            if new_frequency:
                habit.frequency_weekly = new_frequency
            self.save_habits()
            print(f"Habit '{name}' edited successfully.")
        else:
            print(f"Habit '{name}' not found.")

def main():
    """
    Main function to run the terminal app - Habit Tracker.
    """
    tracker = HabitTracker()
    tracker.load_habits()

    parser = argparse.ArgumentParser(description="Simple Habit Tracker")
    parser.add_argument('command', choices=['add', 'remove', 'view', 'edit'], help='Command to execute')
    parser.add_argument('habit_name', nargs='?', help='Name of the habit')
    parser.add_argument('--duration', type=int, help='Duration of the habit in minutes')
    parser.add_argument('--frequency', type=int, help='Frequency of the habit per week')
    parser.add_argument('--new_name', help='New name for the habit')
    parser.add_argument('--new_duration', type=int, help='New duration for the habit in minutes')
    parser.add_argument('--new_frequency', type=int, help='New frequency for the habit per week')

    args = parser.parse_args()

    if args.command == 'add':
        if not args.habit_name or not args.duration or not args.frequency:
            print("Error: Please provide habit name, duration, and frequency to add a habit.")
        else:
            tracker.add_habit(args.habit_name, args.duration, args.frequency)
            tracker.view_habits()

    elif args.command == 'remove':
        if not args.habit_name:
            print("Error: Please provide habit name to remove.")
        else:
            tracker.remove_habit(args.habit_name)
            tracker.view_habits()

    elif args.command == 'view':
        tracker.view_habits()

    elif args.command == 'edit':
        if not args.habit_name:
            print("Error: Please provide habit name to edit.")
        else:
            tracker.edit_habit(args.habit_name, args.new_name, args.new_duration, args.new_frequency)
            tracker.view_habits()

if __name__ == "__main__":
    main()
