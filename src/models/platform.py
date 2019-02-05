from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Platform(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "IS_IN_PLATFORM")
    repositories = RelatedFrom("Repository", "IS_IN_PLATFORM")
    versions = RelatedFrom("Version", "IS_IN_PLATFORM")

    def __init__(self, platform):
        self.name = platform['Name']
