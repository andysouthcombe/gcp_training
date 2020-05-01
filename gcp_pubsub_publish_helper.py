from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()


def list_pubsub_topics(project_name):
    project = publisher.project_path(project_name)
    return publisher.list_topics(project)


def check_pubsub_topic_exists(topic_path, project_name):
    topics = list_pubsub_topics(project_name)
    return any(t.name == topic_path for t in topics)


def create_pubsub_topics(topic_name, project_name):
    topic_path = publisher.topic_path(project_name, topic_name)
    topic = publisher.create_topic(topic_path)


def publish_pubsub_message(topic_name, data):
    data = data.encode("utf-8")
    future = publisher.publish(topic_name, data=data)
    print(future.result())
