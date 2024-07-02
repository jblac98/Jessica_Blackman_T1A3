class HabitTracker:
  def __init__(self):
    self.habits = []

    def add_habit(self,name):
      habit = Habit(name)
      self.habits.append(habit)
      print(f"Added new habit: '{name}'")

    def remove_habit(self, name):
       habit = Habit(name)
       self.habits.append(habit)
       print(f"Habit removed: '{name}'")
    
    def view_habit(self, name):
       habit = Habit(name)
       self.habits.append(habit)
       print(f"View habit: '{name}'")

    def reflect_habit(self, name):
       habit = Habit(name)
       self.habits.append(habit)
       print(f"Reflect habit: '{name}'")

def main():
    tracker = HabitTracker()

    parser = argparse.ArgumentParser(description="Simple Habit Tracker")
    parser.add_argument('command', choices=['add', 'remove', 'view', 'track habits', 'reflect on habits'], help='Command to execute')
    parser.add_argument('habit_name', nargs='?', help='Name of the habit')

    args = parser.parse_args()

    if args.command == 'add':
        if not args.habit_name:
            print("Error: Please provide a habit name to add.")
        else:
            tracker.add_habit(args.habit_name)
    elif args.command == 'remove':
        # Implement 'remove' command logic
        pass
    elif args.command == 'view':
        # Implement 'view' command logic
        pass
    elif args.command == 'track habits':
        # Implement 'track habits' command logic
        pass
    elif args.command == 'reflect on habits':
        # Implement 'reflect on habits' command logic
        pass 

if args.command == 'add':
        if not args.habit_name:
            print("Error: Please provide a habit name to add.")
        else:
            tracker.add_habit(args.habit_name)

    elif args.command == 'remove':
        if not args.habit_name:
            print("Error: Please provide a habit name to remove.")
        else:
            tracker.mark_habit_done(args.habit_name)
            
    elif args.command == 'view':
        tracker.list_habits()

    elif args.command == 'track progress':
        if not args.habit_name:
            print("Error: Please provide a habit name to track the progress.")
        else:
            tracker.mark_habit_done(args.habit_name)
      
    elif args.command == 'reflect on progress':
        if not args.habit_name:
            print("Error: Please provide a habit name to reflect on progress.")
        else:
            tracker.mark_habit_done(args.habit_name)