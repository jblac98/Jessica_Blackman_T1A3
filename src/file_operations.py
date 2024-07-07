import json
import os

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
  
# File path
file_path = 'data/habits.json'

# Printing the path to verify the file path
print("File path:", file_path)

# Attempt to open the file
try:
   with open(file_path, 'r') as f:
      # Process file here 
      pass
except FileNotFoundError:
   print("File not found")
except IOError as e:
   print("IOError:", e)


