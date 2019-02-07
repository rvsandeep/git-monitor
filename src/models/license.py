from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class License(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "HAS_LICENSE")
    repositories = RelatedFrom("Repository", "HAS_LICENSE")

    def __init__(self, license):
        self.name = license['Licenses']
