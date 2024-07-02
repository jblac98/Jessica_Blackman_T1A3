import json

def get_habit(file_path):
# Load habits from a JSON file. 
# parameters: file_path: Path to the JSON file
# return: list of habits or an empty list if an error occurs
  try:
      with open(file_path, 'r') as file:
        habits = json.load(file)
      return get_habit
  except FileNotFoundError:
     print(f"Error: The file {file_path} does not exist")
     return []
  
  except Exception as e:
     print(f"An unexpected error occured: {e}")
     return []

def remove_habit(file_path, habits):
# Remove habits from a JSON file
# parameters: file_path: Path to the JSON file 

   try:
      with open(file_path, 'rm') as file:
         json.update(habits, file, indent=4)
      print(f"Habit successfully removed from {file_path}")
    except PermissionError:
      print(f"Error: Permission denied to remove.")
      print("An unexpected error occured", e)
