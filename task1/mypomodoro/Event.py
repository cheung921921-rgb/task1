from datetime import datetime, timedelta

class Event:
    def __init__(self, title: str, start_time: datetime, duration_minutes: int = 60):
        self.title = title
        self.start_time = start_time
        self.duration_minutes = duration_minutes
        self.end_time = start_time + timedelta(minutes=duration_minutes)
    
    def __str__(self):
        return f"{self.title} ({self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')})"
    
    def display(self):
        return str(self)