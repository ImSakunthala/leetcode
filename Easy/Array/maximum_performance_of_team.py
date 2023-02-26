total_team_members = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
required_team_members = 3

member = []

for num in range(0, total_team_members+1):
    if num == required_team_members:
        print(member)
    else:
        num = required_team_members - 1
        print(member)


