'''
Ben Rudinski
Topher's Lovers
SoftDev
K05: File Parsing
2024-09-17
time spent: 0.5 hr
'''

import random

with open("krewes.txt", "r") as file:  # open the krewes text file and read its contents
    content = file.read()

# split the content using '@@@' to separate each tuple
tuples = content.split("@@@")

devos_list = []
# process each tuple and split it by '$$$' to get period, devo, ducky
for tup in tuples:
    parts = tup.split("$$$")
    if len(parts) == 3:  # make sure are exactly 3 parts
        period, devo, ducky = parts
        devos_list.append({'period': period, 'devo': devo, 'ducky': ducky})

# randomly select a devo from the list and print their details
if devos_list:
    random_devo = random.choice(devos_list)
    print(f"Devo: {random_devo['devo']}, Period: {random_devo['period']}, Ducky: {random_devo['ducky']}")
else:
    print("No valid devos found.")
