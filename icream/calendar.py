import event
 
from copy import deepcopy

# icalendar interface
import icalendar

class ICREAMCalendar:

    def __init__(self, path = None, calendar=None):
        self.events = list()
        if path is not None:
            self.load_calendar(path)
        if calendar is not None:
            self.events = deepcopy(calendar.events)

    # load calendar from file
    def load_calendar(self, path):
        with open(path, "r") as f:
            # read calendar from file
            ical = icalendar.Calendar.from_ical(f.read())
            f.close()
        
            for component in ical.walk():
                #print(component.name)
                if component.name == "VEVENT":
                    icrm_ev = event.ICREAMEvent(component=component)
                    self.events.append(icrm_ev)
            
            self.sort_calendar_by_date()
    
    # prints callendar
    def print_calendar(self):
        for ev in self.events:
            print(ev)
    
    # sort calendar by date
    def sort_calendar_by_date(self, reverse=False):
        self.events.sort(key=lambda x : x.start, reverse=reverse)

if __name__=="__main__":
    _path = "../cals/kubikji2@fel.cvut.cz.ics"
    icrm_cal = ICREAMCalendar(path=_path)
    icrm_cal.sort_calendar_by_date()
    icrm_cal.print_calendar()
