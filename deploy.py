from gcp_storage_helper import *
from gcp_pubsub_publish_helper import *

if __name__ == "__main__":
    project_name = "gcp-learning-project-274814"
    target_bucket_name = "skating_inbound_bucket"
    source_file_path = "/home/andy/git/2018-02-olympic-figure-skating-analysis/data/"
    topic_name = "projects/" + project_name + "/topics/andy_test"
    if not check_bucket_exists(target_bucket_name):
        create_bucket(target_bucket_name)

    bucket_list = list_buckets()

    for bucket in bucket_list:
        print(bucket.name)

    copy_file_to_bucket(target_bucket_name, source_file_path + "judges.csv", "judges.csv")

    bucket_contents = get_bucket_contents(target_bucket_name)

    print("bucket contents")
    for blob in bucket_contents:
        print(blob.name)

    copy_file_pattern_to_bucket(target_bucket_name,source_file_path,"*.csv")

    bucket_contents = get_bucket_contents(target_bucket_name)

    print("bucket contents")
    for blob in bucket_contents:
        print(blob.name)

    topics = list_pubsub_topics(project_name)
    for topic in topics:
        print(topic.name)
    if not check_pubsub_topic_exists(topic_name,project_name):
        create_pubsub_topics(topic_name,project_name)

