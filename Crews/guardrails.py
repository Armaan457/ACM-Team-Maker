from crewai import TaskOutput
from typing import Tuple, Any
import json

def validate_team_formation(result: TaskOutput) -> Tuple[bool, Any]:
    try:
        if hasattr(result, 'json_dict') and result.json_dict:
            teams_data = result.json_dict
        else:
            teams_data = json.loads(str(result))
        
        if 'Teams' not in teams_data:
            return (False, "Output missing 'Teams' key")
        teams = teams_data['Teams']
        if not isinstance(teams, list):
            return (False, "Teams should be a list")
        if len(teams) == 0:
            return (False, "No teams were created")
        
        all_members = set()
        for i, team in enumerate(teams):
            if 'Team_Number' not in team or 'Member_Names' not in team:
                return (False, f"Team {i+1} missing required fields")
            member_names = team['Member_Names'].split(',')
            member_names = [name.strip() for name in member_names if name.strip()]
            if len(member_names) < 4:
                return (False, f"Team {team['Team_Number']} has fewer than 4 members ({len(member_names)} members)")
            if len(member_names) > 5:
                return (False, f"Team {team['Team_Number']} has more than 5 members ({len(member_names)} members)")
            
            for member in member_names:
                if member in all_members:
                    return (False, f"Student '{member}' is assigned to multiple teams")
                all_members.add(member)
        
        return (True, result)
        
    except json.JSONDecodeError:
        return (False, "Invalid JSON format in team formation output")
    except Exception as e:
        return (False, f"Unexpected error during team validation: {str(e)}")


def validate_idea_selection(result: TaskOutput) -> Tuple[bool, Any]:
    try:
        if hasattr(result, 'json_dict') and result.json_dict:
            ideas_data = result.json_dict
        else:
            ideas_data = json.loads(str(result))
        
        if 'Team_Idea' not in ideas_data:
            return (False, "Output missing 'Team_Idea' key")
        team_ideas = ideas_data['Team_Idea']
        if not isinstance(team_ideas, list):
            return (False, "Team_Idea should be a list")
        if len(team_ideas) == 0:
            return (False, "No team ideas were created")
        
        team_numbers = set()
        for i, team_idea in enumerate(team_ideas):
            if 'Team_Number' not in team_idea or 'Best_Idea' not in team_idea:
                return (False, f"Team idea {i+1} missing required fields")
            team_number = team_idea['Team_Number']
            best_idea = team_idea['Best_Idea'].strip()
            if team_number in team_numbers:
                return (False, f"Duplicate team number {team_number} in idea selection")
            team_numbers.add(team_number)
            if not best_idea or best_idea.upper() == 'N/A':
                return (False, f"Team {team_number} has no valid idea assigned")
        
        return (True, result)
        
    except json.JSONDecodeError:
        return (False, "Invalid JSON format in idea selection output")
    except Exception as e:
        return (False, f"Unexpected error during idea validation: {str(e)}")