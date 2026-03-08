# schedule.py
from datetime import datetime, timedelta
from Event import Event  


class ScheduleManager:  #建立event list 和加&show event
    def __init__(self):
        self.events = []

    def add_event_by_details(self, title: str, start_time: datetime, duration_minutes: int):
        event = Event(title, start_time, duration_minutes)
        self.events.append(event)
        print(f"Added: {event}")

    def show_all_events(self):
        if not self.events:
            print("No events scheduled yet.")
            return
        
        print("\n--- All Scheduled Events ---")
        for i, event in enumerate(sorted(self.events, key=lambda e: e.start_time), 1):
            print(f"{i}. {event}")
        print("-----------------------------")