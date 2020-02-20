from datetime import date


class Activity:
    activity_id: str
    context_id: str
    context_type: str
    object_id: str
    object_type: str
    subject_id: str
    subject_type: str
    date: date
    activity_type: str

    def __init__(self, activity_id, context_id, context_type, object_id, object_type, subject_id, subject_type,
                 date_act, activity_type):
        self.activity_id = activity_id
        self.context_id = context_id
        self.context_type = context_type
        self.object_id = object_id
        self.object_type = object_type
        self.subject_id = subject_id
        self.subject_type = subject_type
        self.date = date_act
        self.activity_type = activity_type
