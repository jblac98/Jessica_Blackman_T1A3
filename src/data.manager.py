import json
import os

DATA_FILE = "habits.json"

# Appends new habit to the list of habits and then saves the updated list back to the JSON file.
def save_habits(habit):
  habits = load_habits()
  habits.append(habit)
  save_to_json(habits)

# Load habits from 'habits.json' or initialises an empty list if it doesn't.
  def load_habits():
    if os.path.exists(DATA_FILE):
      with open(DATA_FILE, 'r') as file:
        habits = json.load(file)

    else:
        habits = []
    return habits
  
  # Saves data (list of habits) to 'habits.json'
  def save_to_json(data):
    with open(DATA_FILE, 'w') as file:
      json.dump(data, file, indent=4)