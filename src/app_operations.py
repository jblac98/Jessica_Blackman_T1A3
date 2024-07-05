import json
import datetime
from data_manager import *

def add_habits(args):
  # Validate inputs
  if not all([args.first_name, args.last_name, args.start_date, args.duration, args.duration, args.frequency]):
    print("Error: Missing required inputs.")
    return
  
  try:
      start_date = datetime.datetime.strptime(args.start_date, '%d/%m/%Y').date()
  except ValueError:
     print("Error: Incorrect date format. Use dd/mm/yyyy.")
     return
  
  habit = {
     'first_name': args.first_name,
     'last_name': args.last_name,
     'start_date': args.start_date,
     'duration': args.duration,
     'frequency': args.frequency
  }

  # Save habit to JSON file
  save_habit(habit)
  print("Habit added successfully.")

  def remove_habit(args):
     # Implement remove habit logic
     pass
  
  def edit_habit(args):
     # Implement edit habit logic
     pass
  
  def view_habit(args):
     # Implement view habit logic
     pass
  
  def reflect_on_habit(args):
     # Implement reflect on habit logic
     pass
  
  def add_habit():
     print("\n=== Add a habit ===")
     first_name = input("Enter first name: ").strip()
     last_name = input("Enter last name: ").strip()
     start_date = input("Enter start date (dd/mm/yyyy): ").strip()
     duration = input("Enter duration in minutes: ").strip()
     frequency = input("Enter weekly frequency: ").strip()

     try:
        start_date = datetime.datetime.strptime(start_date, '%d/%m/%Y').date()
        duration = int(duration)
        frequency = int(frequency)
    except ValueError:
  print("Error: Incorrect input format.")
  return

habit = {
   'first_name': first_name, 
   'last_name': last_name, 
   'start_date': start_date.strftime('%d/%m/%Y'),
   'duration': duration,
   'frequency': frequency
}

save_habit(habit)
print("Habit added successfully.")

def remove_habit():
   print("\n=== Remove a Habit ====")
   habits = load_habits()
   if not habits:
      print("No habits to remove.")
      return
   
   print("Select a habit to remove:")
   for index, habits in enumerate(habits):
      print(f"{index + 1}. {habit['first_name']} {habit['last_name']}")

    try:
      choice = int(input("Enter the number of the habit to remove: ").strip())
      if 1 <= choice <= len(habits):
         removed_habit = habits.pop(choice - 1)
         save_to_json(habits)
         print(f"Removed habit: {removed_habit['first_name']} {removed_habit['last_name']} - Start Date: {habit['start_date']}, Duration: {habit['duration']} minutes, Frequency: {habit['frequency']} times/week")

def view_all_habits():
   print("\n=== View All Habits ===")
   habits = load_habits()
   if not habits:
      print("No habits found.")
    else:
      for index, habit in enumerate(habits):
         print(f"{index + 1}. {habit['first_name']} {habit['last_name']} - Start Date: {habit['start_date']}, Duration: {habit['duration']} minutes, Frequency: {habit['frequency']} times/week")

def edit_habit():
   print("\n=== Edit a Habit ===")
   habits = load_habits()
   if not habits:
      print("No habits to edit.")
      return
   
   print("Select a habit to edit:")
   for index, habit in enumerate(habits):
      print(f"{index + 1}. {habit['first_name']} {habit['last_name']}")
    
    try:
      choice = int(input("Enter the number of the habit to edit: ").strip())
      if 1 <= choice <= len(habits):
         selected_habit = habits[choice - 1]
         print(f"Editing habit: {selected_habit['first_name']} {selected_habit['last_name']}")

         # Prompt user for new values.
         new_duration = input(f"Enter new duration for {selected_habit['first_name']} {selected_habit['last_name']} (current: {selected_habit['duration']} minutes):").strip()
         new_frequency = input(f"Enter new frequency for {selected_habit['first_name']} {selected_habit['last_name']} (current: {selected_habit['frequency']} times/week):").strip()

         # Update the selected habit.
         selected_habit['duration'] = int(new_duration) if new_duration else selected_habit['duration']
         selected_habit['frequency'] = int(new_frequency) if new_frequency else selected_habit['frequency']

         # Save updated habits list
         save_to_json(habits)
         print("Habit updated successfully.")
      else:
         print("Invalid choice.")
    except ValueError:
      print("Invalid input. Please enter  number.")



