from crewai import Agent, Crew, Process, Task, LLM, TaskOutput
from crewai.project import CrewBase, agent, crew, task
from Crews.models import IdeaListOutput, TeamListOutput, StudentList, IdeaList
from Crews.guardrails import validate_team_formation, validate_idea_selection
import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
    model='gemini/gemini-2.0-flash',
    api_key=os.getenv("GEMINI_API_KEY")
)

@CrewBase
class ACMTeamMaker():

    agents_config = '../config/agents.yaml'
    tasks_config = '../config/tasks.yaml'

    @agent
    def TeamAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['TeamAgent'],
            verbose=False,
            llm=llm
        )
    @agent
    def IdeaAgent(self) -> Agent:
        return Agent(
            config=self.agents_config['IdeaAgent'],
            verbose=False,
            llm=llm
        )
    
    @task
    def TeamMaking(self) -> Task:
        return Task(
            config=self.tasks_config['TeamMaking'],
            output_json=TeamListOutput,
            input_model=StudentList,
            callback=self.team_callback,
            output_file='Output/Teams.json',
            create_directory=True,
            guardrail=validate_team_formation
        )
    @task
    def IdeaChoosing(self) -> Task:
        return Task(
            config=self.tasks_config['IdeaChoosing'],
            output_json=IdeaListOutput,
            input_model=IdeaList,
            callback=self.idea_callback,
            output_file='Output/Team_Idea.json',
            create_directory=True,
            guardrail=validate_idea_selection
        )
  
    def team_callback(self, output: TaskOutput):
        print(f"""
            Team Formation completed!
            """)
    
    def idea_callback(self, output: TaskOutput):
        print(f"""
            Idea Selection completed!
            """)

    @crew
    def TeamCrew(self) -> Crew:
        return Crew(
            agents=[
            self.TeamAgent(),
            ],
            tasks=[
            self.TeamMaking(),
            ],
            process=Process.sequential
        )
    @crew
    def IdeaCrew(self) -> Crew:
        return Crew(
            agents=[
            self.IdeaAgent()
            ],
            tasks=[
            self.IdeaChoosing()
            ],
            process=Process.sequential
        )