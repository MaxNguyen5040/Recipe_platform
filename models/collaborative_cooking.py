class CollaborativeSession:
    def __init__(self, session_id, recipe_id, participants):
        self.session_id = session_id
        self.recipe_id = recipe_id
        self.participants = participants

    def add_participant(self, user_id):
        self.participants.append(user_id)

    def remove_participant(self, user_id):
        self.participants.remove(user_id)

    def get_participants(self):
        return self.participants

sessions = {}

def create_session(session_id, recipe_id, participants):
    sessions[session_id] = CollaborativeSession(session_id, recipe_id, participants)

def join_session(session_id, user_id):
    if session_id in sessions:
        sessions[session_id].add_participant(user_id)

def leave_session(session_id, user_id):
    if session_id in sessions:
        sessions[session_id].remove_participant(user_id)

def get_session_participants(session_id):
    if session_id in sessions:
        return sessions[session_id].get_participants()
