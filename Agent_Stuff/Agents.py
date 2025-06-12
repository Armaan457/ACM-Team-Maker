from crewai import Agent

TeamMaker = Agent(
    role="Team Making Agent",
    goal="Create well balanced teams of 4 students for a hackathon, ensuring diverse skills and backgrounds from both technical and non-technical prospects.",
    backstory="You are an expert in team formation with a focus on diversity and skill balance. Your task is to analyze the skills of students and form a team that maximizes the potential for success in a hackathon environment.",
    verbose=False,
    allow_delegation=False,
    llm="gpt-4o",
)