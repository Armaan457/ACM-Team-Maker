import csv
import json
from crewai import Crew
from Agents_Tasks.Tasks import TeamMaking, StudentList
from Agents_Tasks.Agents import TeamAgent

csv_path = r'Data\Intra ACM Hackathon 2025 (Responses) - Form Responses 1.csv'

students_raw = []
with open(csv_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        students_raw.append({
            "Name": row.get("Full name", "").strip(),
            "Skills": row.get("Technical skills", "").strip()
        })

students = StudentList(students=students_raw)

student_list_str = json.dumps(
    [{"Name": s.Name, "Skills": s.Skills} for s in students.students],
    indent=2
)

crew = Crew(
    agents=[TeamAgent],
    tasks=[TeamMaking],
    verbose=True
)

crew_output = crew.kickoff(inputs={"input_data": student_list_str})

print("\n📝 Final Team Output:")
print(crew_output)
