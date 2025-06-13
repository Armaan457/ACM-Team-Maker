from crewai import Agent, LLM
import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
        model='gemini/gemini-1.5-flash',
        api_key=os.getenv("GEMINI_KEY")
        )

TeamAgent = Agent(
    role="Team Making Agent",
    goal="Create well balanced teams of 4 students for a hackathon, ensuring diverse skills and backgrounds from both technical and non-technical prospects.",
    backstory="You are an expert in team formation with a focus on diversity and skill balance. Your task is to analyze the skills of students and form a team that maximizes the potential for success in a hackathon environment.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
)