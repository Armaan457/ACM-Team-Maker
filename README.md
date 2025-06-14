# ACM Team Maker (Hackathon Team & Idea Automation)

This project automates the complex and time consuming process of organizing a hackathon by using AI agents powered by CrewAI. It intelligently forms balanced teams from a list of participants, aggregates their project ideas, and then selects the most promising idea for each team to work on.

The entire workflow is orchestrated in a single script, producing a final, clean CSV report ready for hackathon organizers.


## ✨ Features

-   **AI-Powered Team Formation**: Analyzes participant skills to create balanced and synergistic teams.
-   **Automated Idea Aggregation**: Collects all project ideas submitted by members of each newly formed team.
-   **AI-Driven Idea Selection**: Evaluates the aggregated ideas for each team and chooses the best one to pursue.
-   **End-to-End Automation**: Runs the entire process—from raw registration data to a final report—with a single command.
-   **Modular & Extendable**: Built with a clear structure, making it easy to customize agents, tasks, or the workflow itself.

---

## ⚙️ How It Works: The Workflow

The `main.py` script executes a four-step pipeline:

1.  **Team Formation Crew**:
    -   Reads participant names and skills from the input CSV.
    -   The `Team_Crew` with a `TeamAgent` executes a `TeamMaking` task.
    -   **Output**: A `Output/Teams.json` file detailing the members of each team.

2.  **Idea Aggregation**:
    -   The script maps the newly created teams back to the original participant data.
    -   It collects all the project ideas submitted by the members of each team.

3.  **Idea Selection Crew**:
    -   The aggregated ideas for each team are passed to a `Idea_Crew`.
    -   An `IdeaAgent` executes an `IdeaChoosing` task to analyze the ideas and select the best one for each team.
    -   **Output**: A `Output/Team_Idea.json` file containing the chosen idea for each team.

4.  **Final Report Generation**:
    -   The script merges the team member data from `Teams.json` and the selected ideas from `Team_Idea.json`.
    -   **Final Output**: A clean `Output/final_teams_with_ideas.csv` file, providing a complete overview of all teams, their members, and their assigned projects. 
    -   The aforementioned intermediate json files are automatically deleted after the successful completion of the script

---

## 📌 Note

For the sake of privacy the Data and Output folder have not been tracked to GitHub

---

## 📁 Project Structure

```
.
├── Agents/
│   ├── agents.py       # Defines CrewAI agents (TeamAgent, IdeaAgent)
│   ├── tasks.py        # Defines CrewAI tasks (TeamMaking, IdeaChoosing)
│   ├── crews.py        # Defines CrewAI crews (Team_Crew, Idea_Crew)
│   └── models.py       # Pydantic models for input and output validation
├── Data/
│   └── *.csv           # Input CSV file with participant data
├── Output/
│   ├── Teams.json      # Intermediate output from the team formation crew (Deleted post completion)
│   ├── Team_Idea.json  # Intermediate output from the idea selection crew (Deleted post completion)
│   └── final_teams_with_ideas.csv  # The final, merged report
├── .env                # For storing API keys
├── .gitgnore           # For specifying files and directories which should be ignored in version control
├── main.py             # Main script to orchestrate the entire workflow  
├── pyproject.toml      # Project metadata and dependencies
└── README.md           # You are here!
```