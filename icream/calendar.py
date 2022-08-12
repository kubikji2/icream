# icalendar interface
import icalendar
# import deepcopy
import copy

# importing icream events
from . import event as ie

class ICREAMCalendar:

    def __init__(self, path = None, calendar=None):
        self.events = list()
        if path is not None:
            self.load_calendar(path)
        if calendar is not None:
            self.events = copy.deepcopy(calendar.events)

    # load calendar from file
    def load_calendar(self, path):
        with open(path, "r") as f:
            # read calendar from file
            ical = icalendar.Calendar.from_ical(f.read())
            f.close()
        
            for component in ical.walk():
                #print(component.name)
                if component.name == "VEVENT":
                    icrm_ev = ie.ICREAMEvent(component=component)
                    self.events.append(icrm_ev)
            
            self.sort_calendar_by_date()
    
    # prints callendar
    def print_calendar(self):
        for ev in self.events:
            print(ev)
    
    # sort calendar by date
    def sort_calendar_by_date(self, reverse=False):
        # loosly based on: https://www.programiz.com/python-programming/methods/list/sort
        self.events.sort(key=lambda x : x.start, reverse=reverse)
