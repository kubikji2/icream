
class ICREAMEvent:
    
    def ICREAMEvent(self, start=None, end=None, name="", organizer="", description=""):
        self.start = start
        self.end = end
        self.name = name
        self.organizer = organizer
        self.description = description
        pass

    def get_duration(self):
        return 0 if (self.start is None) or (self.end is None) else self.end - self.start
    
    