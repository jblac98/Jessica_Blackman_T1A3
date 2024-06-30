from datetime import datetime

def break_habit(habit_name, start_date, duration_per_habit, frequency_per_habit):
  # Personal details
  goal = 60

  # Total time elapsed in seconds
  time_elapsed = (datetime.now() - start_date).total_seconds()

  # Convert timestamp into hour/days
  hours = round(time_elapsed / 60 / 60, 1)
  days = round(hours / 24, 2)

  # Goal (days to go)
  days_to_go = round(goal - days)

  # Change hours to days
  if hours > 72:
    hours = str(days) + " days"
  else:
    hours = str(hours) + " hours"

  return {"habit": habit_name, "time_since": hours, "days_remaining": days_to_go}

print(break_habit("gym", datetime(2024, 6, 1), duration_per_habit=60, frequency_per_habit=5))