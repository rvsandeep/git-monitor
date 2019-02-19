from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Status(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "STATUS")
    repositories = RelatedFrom("Repository", "STATUS")

    def __init__(self, status):
        self.name = status['Status']
