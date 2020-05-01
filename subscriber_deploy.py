from gcp_storage_helper import *
from gcp_pubpub_subscriber_helper import *

if __name__ == "__main__":
    project_name = "gcp-learning-project-274814"
    topic_name = "andy_test"
    topic_path = "projects/" + project_name + "/topics/" + topic_name
    subscription_name = "andy_test_sub"
    list_pubsub_subscriptions(project_name)
    print(check_if_pubsub_subscription_exists(subscription_name, project_name))

    if not check_if_pubsub_subscription_exists(subscription_name, project_name):
        create_pubsub_pull_subscription(subscription_name, project_name, topic_path)
