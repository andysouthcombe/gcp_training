from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()


def list_pubsub_topics(project_name):
    project = publisher.project_path(project_name)
    return publisher.list_topics(project)


def check_pubsub_topic_exists(topic_name,project_name):
    topics = list_pubsub_topics(project_name)
    return any(t.name == topic_name for t in topics)


def create_pubsub_topics(topic_name,project_name):
    topic_path = publisher.topic_path(project_name, topic_name)
    topic = publisher.create_topic(topic_path)


def publish_pubsub_message(topic_name,project_name,data):

        # The `topic_path` method creates a fully qualified identifier
        # in the form `projects/{project_id}/topics/{topic_name}`
        topic_path = publisher.topic_path(project_name, topic_name)
        data = data.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        print(future.result())

