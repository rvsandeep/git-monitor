from py2neo.ogm import GraphObject, Property, RelatedFrom, RelatedTo

class Platform(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "IS_IN_PLATFORM")
    repositories = RelatedFrom("Repository", "IS_IN_PLATFORM")
    versions = RelatedFrom("Version", "IS_IN_PLATFORM")

class Language(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "WRITTEN_IN")
    repositories = RelatedFrom("Repository", "WRITTEN_IN")
    versions = RelatedFrom("Version", "WRITTEN_IN")

class License(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "HAS_LICENSE")
    repositories = RelatedFrom("Repository", "HAS_LICENSE")

class Status(GraphObject):
    __primarykey__ = "name"

    name = Property()

    projects = RelatedFrom("Project", "STATUS")
    repositories = RelatedFrom("Repository", "STATUS")


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
