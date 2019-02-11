from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom
import re

class Version(GraphObject):
    __primarykey__ = "id"

    id = Property()
    number = Property()
    publish_timestamp = Property()
    created_timestamp = Property()
    updated_timestamp = Property()

    project = RelatedTo("Project")
    version = RelatedFrom("Version","DEPENDENT_ON")

    def __init__(self, version):
        self.id = version['ID']
        self.number = None
        version_parsed = re.findall("\\b\\d+\\b", version['Number'])
        if len(version_parsed) !=0:
            self.number = version_parsed[0]
            self.id = version['Project ID']+'_'+self.number

        self.publish_timestamp = version['Published Timestamp']
        self.created_timestamp = version['Created Timestamp']
        self.updated_timestamp = version['Updated Timestamp']
