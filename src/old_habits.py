from datetime import datetime
from src.habit_tool import get_habit
import pandas as pd
from tabulate import tabulate

form_habits = [
    get_habit("Gym", datetime(2024, 6, 1), duration_minutes=60, weekly_frequency=5),
    get_habit("Skin care", datetime(2024, 6, 15), duration_minutes=15, weekly_frequency=7),
    get_habit("Running", datetime(2024, 6, 20), duration_minutes=30, weekly_frequency=3)
]
break_habits = [
    get_habit("Vaping", datetime(2024, 5, 31), duration_minutes=8, weekly_frequency=7, form_habit=False),
    get_habit("Sugar", datetime(2024, 6, 12), duration_minutes=15, weekly_frequency=7, form_habit=False),
    get_habit("Sleeping in", datetime(2024, 6, 15), duration_minutes=20, weekly_frequency=6, form_habit=False)
]

df_form_habits = pd.DataFrame(form_habits)
df_break_habits = pd.DataFrame(break_habits)

print(tabulate(df_form_habits, headers="keys", tablefmt="psql"))
print(tabulate(df_break_habits, headers="keys", tablefmt="psql"))