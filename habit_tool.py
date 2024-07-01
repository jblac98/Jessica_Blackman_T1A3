from datetime import datetime
"""
Use this function to return habit objects with respect to forming habits
inputs:
:habit_name str - The name of the habit
start_date - datetime - The date you started doing the new habit, e.g. datetime(2024, 6, 1) # 1st June 2024
duration_minutes: integer - How many minutes it takes to do that habit once
weekly_frequency: integer - How many times per week you do the habit
form_habit: boolean - Whether or not we are trying to form a new habit
"""
def get_habit(habit_name, start_date, duration_minutes, weekly_frequency, form_habit=True):
  # Personal details
  goal = 60

  # Total time elapsed in seconds
  time_elapsed = (datetime.now() - start_date).total_seconds()

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

  minutes_spent = weeks * duration_minutes * weekly_frequency

  if form_habit:
    return {"habit": habit_name, "time_since": hours, "days_remaining": days_to_go, "minutes_spent": minutes_spent}
  else:
    return {"habit": habit_name, "time_since": hours, "days_remaining": days_to_go, "minutes_saved": minutes_spent}


print(get_habit("gym", datetime(2024, 6, 1), duration_minutes=60, weekly_frequency=5))