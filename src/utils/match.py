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
        
    def get_event(self, event_id):
        event = self.events.loc[event["id"] == event_id]
        event_data = event.loc[~event.isnull()]
        
        try:
            frames = sb.frames(match_id=self.match_id)
            event_frames = frames.loc[frames["id"] == event["id"]]
        except Exception as e:
            log.info("No 360 frames available for this event.")
        
        return {
            "event": event,
            "frames": event_frames
        }
        
if __name__ == "__main__":
    match_id = 3847567
    final = Match(match_id=match_id)
    
    print(final.teams)