# ACM Team Maker (Hackathon Team & Idea Automation)

This project automates the complex and time consuming process of organizing a hackathon by using AI agents powered by CrewAI. It intelligently forms balanced teams from a list of participants, aggregates their project ideas, and then selects the most promising idea for each team to work on.

The entire workflow is orchestrated in a single script, producing a final, clean CSV report ready for hackathon organizers.


## ✨ Features

-   **AI-Powered Team Formation**: Analyzes participant skills to create balanced and synergistic teams.
-   **AI-Driven Idea Selection**: Evaluates the aggregated ideas for each team and chooses the best one to pursue.
-   **End-to-End Automation**: Runs the entire process—from raw registration data to a final report—with a single command.
-   **Modular & Extendable**: Built with a clear structure, making it easy to customize agents, tasks, or the workflow itself.
-   **Intelligent Guardrails**: Built-in validation system ensures output quality and catches common errors like duplicate team assignments or invalid team sizes.

---

## ⚙️ How It Works: The Workflow

The `main.py` script executes a four-step pipeline:

1.  **Team Formation Crew**:
    -   Reads participant names and skills from the input CSV.
    -   The `TeamCrew` with a `TeamAgent` executes a `TeamMaking` task.
    -   **Output**: A `Output/Teams.json` file detailing the members of each team.

2.  **Idea Aggregation**:
    -   The script maps the newly created teams back to the original participant data.
    -   It collects all the project ideas submitted by the members of each team.

3.  **Idea Selection Crew**:
    -   The aggregated ideas for each team are passed to a `IdeaCrew`.
    -   An `IdeaAgent` executes an `IdeaChoosing` task to analyze the ideas and select the best one for each team.
    -   **Output**: A `Output/Team_Idea.json` file containing the chosen idea for each team.

4.  **Final Report Generation**:
    -   The script merges the team member data from `Teams.json` and the selected ideas from `Team_Idea.json`.
    -   **Final Output**: A clean `Output/final_teams_with_ideas.csv` file, providing a complete overview of all teams, their members, and their assigned projects. 
    -   The aforementioned intermediate json files are automatically deleted after the successful completion of the script

---

## 📌 Note

For the sake of privacy the Data and Output folder have not been tracked to GitHub