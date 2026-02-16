"""
Author: Annika Duggal
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" #string
preferred_weight_kg = 20.5 #float
highest_reps = 25 #int
membership_active = True #bool

# Step c: Create a dictionary named workout_stats
#dict containing strings and tuples
workout_stats = {
    "Alex" : (30, 45, 20),
    "Jamie" : (55, 35, 40),
    "Taylor" : (15, 40, 45)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for name, mins in list(workout_stats.items()):
    total = sum(mins)
    workout_stats[name + "_total"] = total

print("\nWorkout stats:")

for key, value in workout_stats.items():
    print(f"{key}: {value}")

# Step e: Create a 2D nested list called workout_list
#list datatype containing list elements of int values
workout_list = [list(mins) for name, mins in workout_stats.items() if "_total" not in name]

# Step f: Slice the workout_list
print("\nAll friends' yoga and running minutes: ")

for row in workout_list:
    print(row[:2])

print("\nLast 2 friends' weightlifting minutes:")

for row in workout_list[-2:]:
    print(row[2])

# Step g: Check if any friend's total >= 120

for key, value in workout_stats.items():
    if "_total" in key and value >= 120:
        name = key.replace("_total", "")
        print(f"Great job staying active, {name}")

# Step h: User input to look up a friend

searchedName = input("Enter friend's name: ")
if searchedName in workout_stats:
    activity = workout_stats[searchedName]
    total = workout_stats[searchedName + "_total"]

    print(f"\nWorkout stats for {searchedName}: ")
    print(f"Yoga minutes: {activity[0]}")
    print(f"Running minutes: {activity[1]}")
    print(f"Weightlifting minutes: {activity[2]}")
    print(f"Total workout minutes: {total}")

else:
    print(f"\nFriend {searchedName} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes

highestMins = 0
highestFriend = ""
lowestMins = 100000
lowestFriend = ""

for key, value in workout_stats.items():
    if "_total" in key:
        name = key.replace("_total", "")
        if value > highestMins:
            highestMins = value
            highestFriend = name
        if value < lowestMins:
            lowestMins = value
            lowestFriend = name

print (f"Highest Workout: {highestFriend} with {highestMins} minutes")
print (f"Lowest Workout: {lowestFriend} with {lowestMins} minutes")

