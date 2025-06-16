from crewai import Agent, LLM
import os
from dotenv import load_dotenv
load_dotenv()

llm = LLM(
        model='gemini/gemini-2.0-flash',
        api_key=os.getenv("GEMINI_KEY")
        )

TeamAgent = Agent(
    role="Team Making Agent",
    goal="Create well balanced teams of 4 students for a hackathon, ensuring diverse skills and backgrounds from both technical and non-technical prospects.",
    backstory="You are an expert in team formation with a focus on diversity and skill balance. Your task is to analyze the skills of students and form a team that maximizes the potential for success in a hackathon environment.",
    verbose=False,
    allow_delegation=False,
    llm=llm,
)

IdeaAgent = Agent(
    role="Idea Choosing Agent",
    goal="Choose the best idea for a hackathon environment from a set of ideas provided by a team.",
    backstory="You are an expert in evaluating and selecting ideas for hackathons for optimum performance. Your task is to analyze the ideas provided by a team and select the one that is the most clear, novel, scalable, and user-friendly.",
    verbose=False,
    allow_delegation=False,
    llm=llm,
)