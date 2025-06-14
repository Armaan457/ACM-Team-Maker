from crewai import Task, TaskOutput
from Agents.agents import TeamAgent, IdeaAgent
from Agents.models import StudentList, IdeaList, TeamListOutput, IdeaListOutput

def team_callback(output: TaskOutput):
        print(f"""
            Team Formation completed!
            """)
def idea_callback(output: TaskOutput):
        print(f"""
            Idea Selection completed!
            """)

TeamMaking = Task(
    description="""Create teams of 4 students given their names and skill sets for a hackathon ensuring diverse skills and backgrounds from both technical and non technical prospects.
    Here is the list of students with their skills: {input_data}""",
    expected_output="A JSON object with the key as 'Teams' and values as a string containing all members.",
    agent = TeamAgent,
    output_json=TeamListOutput,
    input_model=StudentList,
    guardrail="Ensure that the response is a valid JSON object.",
    callback=team_callback,
    output_file='Outputs/Teams.json',
    create_directory=True
)

IdeaChoosing = Task(
    description="""Given a team and a set of ideas, choose the best idea for a hackathon environment. The idea should be clear, novel, scalable and user friendly.
    Here is the list of students with their skills: {team_data}""",
    expected_output="A JSON object with the key as 'Team_Ideas' and values as a list of jsons.",
    agent = IdeaAgent,
    output_json=IdeaListOutput,
    input_model=IdeaList,
    guardrail="Ensure that the response is a valid JSON object and no team is missing.",
    callback=idea_callback,
    output_file='Outputs/Team_Idea.json',
    create_directory=True
)