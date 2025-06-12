from pydantic import BaseModel
from crewai import Task, TaskOutput
from Agent_Stuff.Agents import TeamAgent

class Team(BaseModel):
    Team_Number: int
    Members: str

class PersonData(BaseModel):
    Name: str
    Skills: str

def team_callback(output: TaskOutput):
        print(f"""
            Team Formation completed!
            """)

TeamMaking = Task(
    description="""Create teams of 4 students given their names and skill sets for a hackathon ensuring diverse skills and backgrounds from both technical and non technical prospects.
    Here is the list of students with their skills: {input_data}""",
    expected_output="A JSON object with the key team number and values as a string containing all members.",
    agent = TeamAgent,
    output_json=Team,
    guardrail="Ensure that the response is a valid JSON object and the team is well balanced in terms of skills.",
    callback=team_callback,
    output_file='outputs/Teams.json',
    create_directory=True
)