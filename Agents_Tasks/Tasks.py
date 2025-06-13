from pydantic import BaseModel
from typing import List
from crewai import Task, TaskOutput
from Agents_Tasks.Agents import TeamAgent

class Team(BaseModel):
    Team_Number: int
    Member_Names: str

class PersonData(BaseModel):
    Name: str
    Skills: str

class StudentList(BaseModel):
    students: List[PersonData]

def team_callback(output: TaskOutput):
        print(f"""
            Team Formation completed!
            """)

TeamMaking = Task(
    description="""Create teams of 4 students given their names and skill sets for a hackathon ensuring diverse skills and backgrounds from both technical and non technical prospects.
    Here is the list of students with their skills: {input_data}""",
    expected_output="A JSON object with the key team number and values as a string containing all members.",
    agent = TeamAgent,
    input_model=StudentList,
    output_json=Team,
    guardrail="Ensure that the response is a valid JSON object.",
    callback=team_callback,
    output_file='Outputs/Teams.json',
    create_directory=True
)