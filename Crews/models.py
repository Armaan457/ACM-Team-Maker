from pydantic import BaseModel
from typing import List

class PersonData(BaseModel):
    Name: str
    Skills: str

class StudentList(BaseModel):
    students: List[PersonData]

class IdeaData(BaseModel):
    Team_number: int
    Ideas: str

class IdeaList(BaseModel):
    ideas: List[IdeaData]

class Team(BaseModel):
    Team_Number: int
    Member_Names: str

class TeamListOutput(BaseModel):
    Teams: List[Team]

class Idea(BaseModel):
    Team_Number: int
    Best_Idea: str

class IdeaListOutput(BaseModel):
    Team_Idea: List[Idea]