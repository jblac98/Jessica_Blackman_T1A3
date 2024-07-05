import argparse
from datetime import datetime, date
import pandas as pd
from tabulate import tabulate

class Habit:

  def __str__(self):
    return self.name  

  def __init__(self, name, start_date, frequency_weekly, duration_minutes, form_habit=True):
    self.name = name
    self.start_date = start_date
    self.frequency_weekly = frequency_weekly
    self.duration_minutes = duration_minutes
    self.form_habit = form_habit
  
  def edit_habit(self, name, start_date, frequency_weekly, duration_minutes, form_habit=True):
    self.name = name
    self.start_date = start_date
    self.frequency_weekly = frequency_weekly
    self.duration_minutes = duration_minutes
    self.form_habit = form_habit


  """
  Use this function to return habit objects with respect to forming habits
  inputs:
  :habit_name str - The name of the habit
  start_date - datetime - The date you started doing the new habit, e.g. datetime(2024, 6, 1) # 1st June 2024
  duration_minutes: integer - How many minutes it takes to do that habit once
  weekly_frequency: integer - How many times per week you do the habit
  form_habit: boolean - Whether or not we are trying to form a new habit

  returns: Dictionary with key metadata
  """
  def get_habit_dict(self):
    # Personal details
    goal = 21

    # Total time elapsed in seconds
    time_elapsed = (datetime.now() - self.start_date).total_seconds()

    # Convert timestamp into hour/days
    hours = round(time_elapsed / 60 / 60, 1)
    days = round(hours / 24, 2)
    weeks = round(days / 7, 2)

    # Goal (days to go)
    days_to_go = round(goal - days)

    # Change hours to days
    if hours > 72:
      hours = str(days) + " days"
    else:
      hours = str(hours) + " hours"

    minutes_spent = weeks * self.duration_minutes * self.frequency_weekly

    if self.form_habit:
      return {"habit": self.name, "frequency": self.frequency_weekly, "duration": self.duration_minutes, "time_since": hours, "days_remaining": days_to_go, "minutes_spent": minutes_spent}
    else:
      return {"habit": self.name, "frequency": self.frequency_weekly, "duration": self.duration_minutes, "time_since": hours, "days_remaining": days_to_go, "minutes_saved": minutes_spent}

class HabitTracker:
  def __init__(self):
    self.habits = []

  def add_habit(self, name, duration, frequency):
    habit = Habit(name, datetime.now(), duration, frequency)
    self.habits.append(habit)
    print(f"Added new habit: '{name}', duration: '{duration}', frequency: '{frequency}'")

  # def remove_habit(self, name):
  #    habit = Habit(name)
  #    self.habits.append(habit)
  #    print(f"Habit removed: '{name}'")
    
  def view_habits(self):
    df_form_habits = pd.DataFrame([habit.get_habit_dict() for habit in self.habits])
    print(tabulate(df_form_habits, headers="keys", tablefmt="psql"))
    # print(self.habits)
    for habit in self.habits:
       print(habit)

    # def reflect_habit(self, name):
    #    habit = Habit(name)
    #    self.habits.append(habit)
    #    print(f"Reflect habit: '{name}'")

def main():
    tracker = HabitTracker()

    parser = argparse.ArgumentParser(description="Simple Habit Tracker")
    parser.add_argument('command', choices=['add', 'remove', 'view', 'edit', 'reflect on habits'], help='Command to execute')
    parser.add_argument('habit_name', nargs='?', help='Name of the habit')
    parser.add_argument('--duration', type=int, help='Duration of the habit in minutes')
    parser.add_argument('--frequency', type=int, help='Frequency of the habit per week')

    args = parser.parse_args()

    if args.command == 'add':
        if not args.habit_name:
            print("Error: Please provide a habit name to add.")
        else:
            tracker.add_habit(args.habit_name, args.duration, args.frequency)
            tracker.view_habits()
    elif args.command == 'remove':
        # Implement 'remove' command logic
        pass
    elif args.command == 'view':
        # Implement 'view' command logic
        pass
    elif args.command == 'reflect on habits':
        # Implement 'reflect on habits' command logic
        pass 

main()




# if args.command == 'add':
#         if not args.habit_name:
#             print("Error: Please provide a habit name to add.")
#         else:
#             tracker.add_habit(args.habit_name)

#     elif args.command == 'remove':
#         if not args.habit_name:
#             print("Error: Please provide a habit name to remove.")
#         else:
#             tracker.mark_habit_done(args.habit_name)
            
#     elif args.command == 'view':
#         tracker.list_habits()

#     elif args.command == 'track progress':
#         if not args.habit_name:
#             print("Error: Please provide a habit name to track the progress.")
#         else:
#             tracker.mark_habit_done(args.habit_name)
      
#     elif args.command == 'reflect on progress':
#         if not args.habit_name:
#             print("Error: Please provide a habit name to reflect on progress.")
#         else:
#             tracker.mark_habit_done(args.habit_name)