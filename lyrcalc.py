# Various calculators in a crappy tkinter window for lyrania.
# Maybe someone other than myself will find this useful.


# Probably not


from tkinter import *
from math import ceil, pow

root = Tk()
root.title("Lyrania Calculator")
root.configure(background='black')


def calc_level():
    level = int(level_entry.get())
    next_level = level * 25
    buffer = int(buffer_entry.get())
    count = 0
    while buffer > next_level:  # probably should do this some other way but nrn
        count += 1
        buffer -= next_level
        next_level += 25
    print("Total Buffer Levels: ", count)
    buffer_levels_label = Label(root, text="Buffer Levels: " + str(count))
    buffer_levels_label.grid(row=0, column=0, padx=5, pady=5)


def calc_damage():
    if len(minutes_entry.get()) == 0:  # is there a better way to do this? Error if empty otherwise
        minutes = 0
    else:
        minutes = int(minutes_entry.get())
    if len(seconds_entry.get()) == 0:
        seconds = (minutes * 60)
    else:
        seconds = (minutes * 60) + int(seconds_entry.get())
    health = int(health_entry.get())
    attacks = seconds / 6  # is this 5 or 6????
    damage_req = ceil(health / attacks)
    damage_req_label = Label(root, text="Damage Req.: " + f"{damage_req:,}")
    damage_req_label.grid(row=0, column=1, padx=5, pady=5)


def calc_jade():
    units = float(units_entry.get())
    current = ceil(float(skill_level_entry.get()) / units)
    print(current)
    goal = ceil(float(goal_entry.get()) / units)
    print(goal)
    discount = 1 - float(joaj_entry.get()) / 100
    jade_total = 0
    for i in range(current + 1, goal + 1):
        jade_total += ceil(i * 5 * discount)
    jade_total_label = Label(root, text="Total Jade: " + f"{jade_total:,}")
    jade_total_label.grid(row=0, column=2, padx=5, pady=5)


# formula for equipment cost increase is (0.005 * (level ^ 2)) - .0101 * level + .0052) * blacksmith_percent
def calc_equip():
    current = int(current_level_entry.get())
    goal = int(goal_level_entry.get())
    discount = 1 - float(blacksmith_entry.get()) / 100
    cost_total = 0
    for i in range(current + 1, goal + 1):
        cost_total += ((0.005 * pow(i, 2)) - .0101 * i + .0052) * discount
        print(cost_total)
    cost_total_label = Label(root, text="Total cost: " + f"{cost_total:,.4f}" + "p")
    cost_total_label.grid(row=0, column=3, padx=5, pady=5)


# calculates the amount of levels to be gained from overflow experience alone
level_label = Label(root, text="Player Level")
overflow_label = Label(root, text="Overflow XP")
level_entry = Entry(root)
buffer_entry = Entry(root)
level_button = Button(root, text='Confirm', command=calc_level)
level_label.grid(row=1, column=0, padx=5, pady=5)
level_entry.grid(row=2, column=0, padx=5, pady=5)
overflow_label.grid(row=3, column=0, padx=5, pady=5)
buffer_entry.grid(row=4, column=0, padx=5, pady=5)
level_button.grid(row=5, column=0, padx=5, pady=5)

# maybe calculates boss damage required per turn?
minutes_label = Label(root, text="Minutes")
seconds_label = Label(root, text="Seconds")
health_label = Label(root, text="Health")
minutes_entry = Entry(root)
seconds_entry = Entry(root)
health_entry = Entry(root)
damage_button = Button(root, text='Confirm', command=calc_damage)
minutes_label.grid(row=1, column=1, padx=5, pady=5)
minutes_entry.grid(row=2, column=1, padx=5, pady=5)
seconds_label.grid(row=3, column=1, padx=5, pady=5)
seconds_entry.grid(row=4, column=1, padx=5, pady=5)
health_label.grid(row=5, column=1, padx=5, pady=5)
health_entry.grid(row=6, column=1, padx=5, pady=5)
damage_button.grid(row=7, column=1, padx=5, pady=5)

# calculate jadeskill cost in a range
skill_level_label = Label(root, text="Current Jade")
goal_label = Label(root, text="Goal")
units_label = Label(root, text="Unit")
joaj_label = Label(root, text="JoaJ")
skill_level_entry = Entry(root)
goal_entry = Entry(root)
units_entry = Entry(root)
joaj_entry = Entry(root)
jade_button = Button(root, text="Confirm", command=calc_jade)
skill_level_label.grid(row=1, column=2, padx=5, pady=5)
skill_level_entry.grid(row=2, column=2, padx=5, pady=5)
goal_label.grid(row=3, column=2, padx=5, pady=5)
goal_entry.grid(row=4, column=2, padx=5, pady=5)
units_label.grid(row=5, column=2, padx=5, pady=5)
units_entry.grid(row=6, column=2, padx=5, pady=5)
joaj_label.grid(row=7, column=2, padx=5, pady=5)
joaj_entry.grid(row=8, column=2, padx=5, pady=5)
jade_button.grid(row=9, column=2, padx=5, pady=5)

# calculate equipment upgrade cost from any level range
current_level_label = Label(root, text="Current Equip")
goal_level_label = Label(root, text="Goal")
blacksmith_label = Label(root, text="Blacksmith")
current_level_entry = Entry(root)
goal_level_entry = Entry(root)
blacksmith_entry = Entry(root)
equipment_button = Button(root, text="Confirm", command=calc_equip)
current_level_label.grid(row=1, column=3, padx=5, pady=5)
current_level_entry.grid(row=2, column=3, padx=5, pady=5)
goal_level_label.grid(row=3, column=3, padx=5, pady=5)
goal_level_entry.grid(row=4, column=3, padx=5, pady=5)
blacksmith_label.grid(row=5, column=3, padx=5, pady=5)
blacksmith_entry.grid(row=6, column=3, padx=5, pady=5)
equipment_button.grid(row=7, column=3, padx=5, pady=5)

root.mainloop()
