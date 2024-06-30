from datetime import datetime
from habit_tool import break_habit
import pandas as pd
from tabulate import tabulate

habits = [
    break_habit("Gym", datetime(2024, 6, 1), duration_per_habit=60, frequency_per_habit=5),
    break_habit("Skin care", datetime(2024, 6, 15), duration_per_habit=15, frequency_per_habit=7),
    break_habit("Vaping", datetime(2024, 6, 5), duration_per_habit=8, frequency_per_habit=7),
    break_habit("Running", datetime(2024, 6, 20), duration_per_habit=30, frequency_per_habit=3)
]

df = pd.DataFrame(habits)

print(tabulate(df, headers="keys", tablefmt="psql"))