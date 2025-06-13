import csv
import json
from collections import defaultdict


csv_file_path = r'Data\Intra ACM Hackathon 2025 (Responses) - Form Responses 1.csv'          
team_json_path = r'outputs\Teams.json'       
output_csv_path = r'Data\team_ideas.csv'  

with open(team_json_path, 'r', encoding='utf-8') as f:
    teams = json.load(f)

name_to_team = {}
for team_num, members in teams.items():
    member_names = [name.strip() for name in members.split(',')]
    for name in member_names:
        name_to_team[name] = team_num

team_ideas = defaultdict(list)

with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["Full name"].strip()
        if name in name_to_team:
            idea = row["Ideas that you would like to build on"].strip()
            if idea:
                team = name_to_team[name]
                team_ideas[team].append(idea)

output_rows = [
    {"Team Number": team, "Combined Ideas": " , ".join(ideas)}
    for team, ideas in team_ideas.items()
]

output_rows.sort(key=lambda x: int(x["Team Number"].split('_')[-1]))

with open(output_csv_path, 'w', newline='', encoding='utf-8') as outfile:
    fieldnames = ["Team Number", "Combined Ideas"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(output_rows)

print(f"✅ Combined ideas saved to: {output_csv_path}")
