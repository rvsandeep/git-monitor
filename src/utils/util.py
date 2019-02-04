import models

def populate_project(project):
    project_node = models.Project()
    project_node.project_id = project['ID']
    project_node.name = project['Name']
    project_node.created_timestamp = project['Created Timestamp']
    project_node.updated_timestamp = project['Updated Timestamp']
    project_node.description = project['Description']
    project_node.homepage = project['Homepage URL']
    project_node.source_rank = project['SourceRank']
    project_node.latest_release_publish_timestamp = project['Latest Release Publish Timestamp']
    project_node.latest_release_number = project['Latest Release Number']
    project_node.last_synced_timestamp = project['Last synced Timestamp']
    return project_node
