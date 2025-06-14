from Agents.agents import TeamAgent, IdeaAgent
from Agents.tasks import TeamMaking, IdeaChoosing
from crewai import Crew

Team_Crew = Crew(agents=[TeamAgent], 
                 tasks=[TeamMaking])

Idea_Crew = Crew(agents=[IdeaAgent], 
                 tasks=[IdeaChoosing])


