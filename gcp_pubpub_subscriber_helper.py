from google.cloud import pubsub_v1


def list_pubsub_subscriptions(project_name):
    subscriber = pubsub_v1.SubscriberClient()
    project_path = subscriber.project_path(project_name)
    subscriptions = subscriber.list_subscriptions(project_path)
    return subscriptions
    subscriber.close()


def check_if_pubsub_subscription_exists(subscription_name, project_name):
    subscriptions = list_pubsub_subscriptions(project_name)
    return any(s == subscription_name for s in subscriptions)


def create_pubsub_pull_subscription(subscription_name, project_name, topic_path):
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        project_name, subscription_name
    )
    subscription = subscriber.create_subscription(
        subscription_path, topic_path
    )

    print("Subscription created: {}".format(subscription))

    subscriber.close()
    # [END pubsub_create_pull_subscription]
