from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Language(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "WRITTEN_IN")
    repositories = RelatedFrom("Repository", "WRITTEN_IN")
    versions = RelatedFrom("Version", "WRITTEN_IN")

    def __init__(self, language):
        self.name = language['Name']
