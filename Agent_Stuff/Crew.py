from crewai import Crew
from Agent_Stuff.Agents import TeamMaker
from Agent_Stuff.Tasks import TeamMaking


crew = Crew(
    agents=[TeamMaker],
    tasks=[TeamMaking],
    verbose=True
)

crew_output = crew.kickoff()