from statsbombpy import sb
import mplsoccer
import warnings
import logging
from enum import Enum

def ignore_warnings():
    warnings.simplefilter("ignore")

ignore_warnings()
log = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def search_in_dataframe(dataframe, **kwargs):
    if len(kwargs) == 0:
        return dataframe
    
    condition = True
    for column_name, value in kwargs.items():
        condition = condition & (dataframe[column_name] == value)
        
    return dataframe.loc[condition]

class Competitions:
    def __init__(self) -> None:
        self.competitions = sb.competitions()
        
    def get_season(self, competition_name, season_name):
        condition = (self.competitions["competition_name"] == competition_name) & (self.competitions["season_name"] == season_name)
        season_row = self.competitions.loc[condition]

        assert len(season_row) == 1, f"Failed to get season, Statsbomb API should return 1 season, not {len(season_row)}"
        
        try:
            season = Season(
            competition_id=season_row["competition_id"].iloc[0], 
            season_id=season_row["season_id"].iloc[0]
        )
            season.load_competition_events(season_row["country_name"].iloc[0], season_row["competition_name"].iloc[0], season_row["season_name"].iloc[0], season_row["competition_gender"].iloc[0])
            
        except Exception as e:
            raise ValueError("Failed to get season, Statsbomb API returned error", e) 
        return season
    
    

class Season:
    def __init__(self, competition_id, season_id) -> None:
        self.matches = sb.matches(competition_id, season_id)
        self.events = None

    def load_competition_events(self, country, competition_name, season_name, gender):
        self.events = sb.competition_events(
            country=country,
            division=competition_name,
            season=season_name,
            gender=gender
        )   
         
    def get_match_by_id(self, match_id):
        return self.matches.loc[match_id]
    
    def get_matches(self, **kwargs):
        return search_in_dataframe(self.matches, **kwargs)
    
    def get_events(self, **kwargs):
        return search_in_dataframe(self.events, **kwargs)


class Match:
    def __init__(self, match_id) -> None:
        self.match_id = match_id
        self.lineups = sb.lineups(match_id=match_id)
        self.teams = tuple(self.lineups.keys())
        self.events = sb.events(match_id=match_id)
    
    def get_event_by_id(self, event_id):
        return self.events.loc[event_id]
    
    def get_events(self, **kwargs):
        return search_in_dataframe(self.events, **kwargs)
     

class PitchDim(Enum):
    WIDTH = 80
    HEIGHT = 120
    
    DEF_BASELINE = 0
    ATT_BASELINE = DEF_BASELINE + HEIGHT
    LEFT_SIDELINE = 0
    RIGHT_SIDELINE = LEFT_SIDELINE + WIDTH
    
    DEF_LCORNER = (DEF_BASELINE, LEFT_SIDELINE)
    DEF_RCORNER = (DEF_BASELINE, RIGHT_SIDELINE)
    ATT_LCORNER = (ATT_BASELINE, LEFT_SIDELINE)
    ATT_RCORNER = (ATT_BASELINE, RIGHT_SIDELINE)
    
    LEFT_MIDPOINT = (DEF_BASELINE + HEIGHT / 2, LEFT_SIDELINE)
    RIGHT_MIDPOINT = (DEF_BASELINE + HEIGHT / 2, RIGHT_SIDELINE)
    CENTRE = (DEF_BASELINE + HEIGHT / 2, LEFT_SIDELINE + WIDTH / 2)
    
    DEF_GOAL_LPOST = (DEF_BASELINE, WIDTH / 2 - 4)
    DEF_GOAL_RPOST = (DEF_BASELINE, WIDTH / 2 + 4)
    ATT_GOAL_LPOST = (ATT_BASELINE, WIDTH / 2 - 4)
    ATT_GOAL_RPOST = (ATT_BASELINE, WIDTH / 2 + 4)
    
