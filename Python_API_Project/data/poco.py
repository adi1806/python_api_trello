class CreateBoard:
    def __init__(self, name):
        self.name = name


class CreateList:
    def __init__(self, name, idBoard):
        self.name = name
        self.idBoard = idBoard

class CreateCard:
    def __init__(self, name, desc, idList):
        self.name = name
        self.desc = desc
        self.idList = idList


class UpdateCard:
    def __init__(self, name):
        self.name = name



class CardResponse:
    def __init__(self, id, name, desc, id_list):
        self.id = id
        self.name = name
        self.desc = desc
        self.id_list = id_list
