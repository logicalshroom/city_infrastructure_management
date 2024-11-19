# Add a new feature to the existing event class to add participants
# Add an additional feature to print number of participants

class Event:
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.participants = participants

    def display_details(self):
        print(f"Event name: {self.name}\nDate: {self.date}\nParticipants: {self.participants}")

    def update_participants(self, new_participants):
        self.participants = new_participants

events = {} #keys = names

def add_event(name, date, participants):
    if name in events:
        print(f"Error, event already exists.")
        return
    events[name] = Event(name, date, participants)
    print(f"New Event Successfully Added: {name} on {date} with {participants} attendees.")
    

def update_event(name, new_participants):
    if name in events:
        events[name].update_participants(new_participants)
        print(f"Event Participant count for Event: {name} has been updated to {new_participants}")
    else:
        print(f"Event not found.")

def display_event():
    for event in events.values():
        event.display_details()

#quick cli

print(f"Welcome to the Event Management System.")

while True:
        command = input("Please input your command:\n (add, update, display, exit)\n >>>").lower()
        if command == "exit":
            break

        try:
            if command == "add":
                name = input(f"Please enter the Event Name: ")
                date = input(f"Please enter the Event Date: ")
                participants = input(f"Please enter the number of participants: ")
                add_event(name, date, participants)
            elif command == "update":
                name = input(f"Please enter the Event Name: ")
                new_participants = input(f"Please enter the new Participant Count: ")
                update_event(name, new_participants)
            elif command == "display":
                display_event()
        except Exception as e:
            print(f"Error Occurred: {e}")

