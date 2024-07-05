import argparse
from app_operations import *


def print_menu():
  print("\n=== Habit Tracker Menu ===")
  print("1. Add a habit")
  print("2. Remove a habit")
  print("3. View all habits")
  print("4. Edit habits")
  print("5. Exit")

  def main():
    while True:
      print_menu()
      choice = input("Enter your choice (1-5): ").strip()

      if choice == '1':
        add_habit()

      elif choice == '2':
        remove_habit()

      elif choice == '3':
        view_all_habits()
      
      elif choice == '4':
        edit_habits()

      elif choice == '5':
        print("Exiting the Habit Tracker. Goodbye!")
        break

      else:
          print("Invlaid choice. Please enter a number from 1 to 5.")

