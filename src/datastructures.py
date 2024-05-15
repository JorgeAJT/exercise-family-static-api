from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # list of members
        self._members = [
            {
                "id": 12,
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if "id" in member: id = member["id"]
        else: id=self._generateId()
        member_updated = {
                "id": id,
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
        self._members.append(member_updated)
        return member_updated

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                member_selected = member
        return member_selected

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
