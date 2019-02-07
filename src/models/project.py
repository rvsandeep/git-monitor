from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo
import re

class Project(GraphObject):
    __primarykey__ = "project_id"

    project_id = Property()
    name = Property()
    created_timestamp = Property()
    updated_timestamp = Property()
    description = Property()
    homepage = Property()
    source_rank = Property()
    latest_release_publish_timestamp = Property()
    latest_release_number = Property()
    last_synced_timestamp = Property()

    versions = RelatedFrom("Version", "BELONGS_TO")
    repositories = RelatedTo("Repository")
    platform = RelatedTo("Platform")
    language = RelatedTo("Language")
    status = RelatedTo("Status")
    licence = RelatedTo("Licence")

    def __init__(self, project):
        self.project_id = project['ID']
        self.name = project['Name']
        self.created_timestamp = project['Created Timestamp']
        self.updated_timestamp = project['Updated Timestamp']
        self.description = project['Description']
        self.homepage = project['Homepage URL']
        self.source_rank = project['SourceRank']
        self.latest_release_publish_timestamp = project['Latest Release Publish Timestamp']
        version_parsed = re.findall("\\b\\d+\\b", project['Latest Release Number'])
        if len(version_parsed) !=0:
            self.latest_release_number = version_parsed[0]
        else :
            self.latest_release_number = None
        self.last_synced_timestamp = project['Last synced Timestamp']
