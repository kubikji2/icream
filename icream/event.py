# import icalendar 
import icalendar

# import my utils 
from . import utils as iu

# basic event object used by ICREAMCalendar
class ICREAMEvent:

    # constructor
    # '-> either use particular data, or use icalendar.Event to initialize
    def __init__(self, start=None, end=None, name="", organizer="", description="", component=None):
        self.start = start
        self.end = end
        self.name = name
        self.organizer = organizer
        self.description = description
        if component is not None:
            self.parse_component(component=component)
    
    # update ICREAMEvent using icalendar.Event
    def parse_component(self, component : icalendar.Event):
        if component.name == "VEVENT":
            self.name = iu.replace_mult_spaces(component.get('summary'))
            # decoding based on: https://icalendar.readthedocs.io/en/latest/usage.html#more-documentation
            self.start = iu.icream_date_converter(component.decoded('dtstart'))
            self.end = iu.icream_date_converter(component.decoded('dtend'))
            self.organizer = iu.iceam_parse_email(component.get('organizer'))
            self.description = component.get('description')
        else:
            print("[ICREAM-event] invalid component {}=!=\'VEVENT\'".format(component.name))

    # computes event durartion
    def get_duration(self):
        return 0 if (self.start is None) or (self.end is None) else self.end - self.start

    # string representatoni
    def __str__(self):
        dur_s = iu.icream_duration_formater(self.start, self.end)
        s = "{} ({}) by {}".format(self.name, dur_s, self.organizer)
        return s

    