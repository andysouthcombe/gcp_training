from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
project_name = "gcp-learning-project-274814"


def list_pubsub_topics():
    project = publisher.project_path(project_name)
    return publisher.list_topics(project)
