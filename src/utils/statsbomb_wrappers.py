from statsbombpy import sb
import mplsoccer
import warnings
import logging

warnings.simplefilter("ignore")
log = logging.getLogger()

logging.basicConfig(level=logging.INFO)

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

