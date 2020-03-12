NORMAL_STATE = 'NORMAL'
WAITING_IMG = 'WAITING_IMG'


class State:
    def __init__(self, name, status=NORMAL_STATE):
        self.name = name
        self.status = status

    def change_status(self, status):
        self.status = status

    def reset(self):
        self.status = NORMAL_STATE
