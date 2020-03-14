NORMAL_STATE = 'NORMAL'

WAITING_IMG_ADD = 'WAITING_IMG_ADD'
WAITING_IMG_DETECT = 'WAITING_IMG_DETECT'

CONTRIBUTOR_WAIT_NAME = 'CONTRIBUTOR_WAIT_NAME'
CONTRIBUTOR_WAIT_PHONE = 'CONTRIBUTOR_WAIT_PHONE'

class State:
    def __init__(self, name, status=NORMAL_STATE):
        self.name = name
        self.status = status

    def change_status(self, status):
        self.status = status

    def reset(self):
        self.status = NORMAL_STATE
