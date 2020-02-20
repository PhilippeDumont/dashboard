class Item:
    item_id: str
    item_type: str
    value: str
    parent_id: str
    parent_type: str

    def __init__(self, item_id, item_type, value, parent_id, parent_type):
        self.item_id = item_id
        self.item_type = item_type
        self.value = value
        self.parent_id = parent_id
        self.parent_type = parent_type
