from statsbombpy import sb
import mplsoccer
import warnings
import logging
from enum import Enum

def ignore_warnings():
    warnings.simplefilter("ignore")
log = logging.getLogger()

logging.basicConfig(level=logging.INFO)

class Competitions:
    def __init__(self) -> None:
        self.competitions = sb.competitions()
        
    def get_season(self, competition_name, season_name):
        condition = (self.competitions["competition_name"] == competition_name) & (self.competitions["season_name"] == season_name)
        season_row = self.competitions.loc[condition]
        try:
            season = Season(
            competition_id=season_row["competition_id"].values[0], 
            season_id=season_row["season_id"].values[0]
        )
            
        except Exception as e:
            raise ValueError("Failed to get season, Statsbomb API returned error", e) 
        return season

class Match:
    def __init__(self, match_id) -> None:
        self.match_id = match_id
        self.lineups = sb.lineups(match_id=match_id)
        self.teams = tuple(self.lineups.keys())
        self.events = sb.events(match_id=match_id)
    
    def get_event_by_id(self, event_id):
        return self.events.loc[event_id]
    
    def get_events(self, **kwargs):
        condition = True;
        for column_name, value in kwargs.items():
            condition = condition & (self.events[column_name] == value)
        
        return self.events.loc[condition]
        
        
class Season:
    def __init__(self, competition_id, season_id) -> None:
        self.matches = sb.matches(competition_id, season_id)

    def get_match_by_id(self, match_id):
        return self.matches.loc[match_id]
    
    def get_matches(self, **kwargs):
        if len(kwargs) == 0:
            return self.matches
        
        condition = True
        for column_name, value in kwargs.items():
            condition = condition & (self.matches[column_name] == value)
            
        return self.matches.loc[condition]

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
    
