import json

def load_habits(file_path):
# Load habits from a JSON file. 
# parameters: file_path: Path to the JSON file
# return: list of habits or an empty list if an error occurs
  try:
      with open(file_path, 'r') as file:
        habits = json.load(file)
      return habits
  except FileNotFoundError:
     print(f"Error: The file {file_path} does not exist")
     return []
  
  except Exception as e:
     print(f"An unexpected error occured: {e}")
     return []

