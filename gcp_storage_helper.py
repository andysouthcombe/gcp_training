from google.cloud import storage


def list_buckets():

    storage_client = storage.Client()
    buckets = storage_client.list_buckets()

    return buckets


def check_bucket_exists(bucket_name):
    buckets_in_project = list_buckets()

    return any(bucket_in_project.name == bucket_name for bucket_in_project in buckets_in_project)


def create_bucket(bucket_name):

    storage_client = storage.Client()
    storage_client.create_bucket(bucket_name)


if __name__ == "__main__":

    if not check_bucket_exists("skating_inbound_bucket"):
        create_bucket("skating_inbound_bucket")

    bucket_list = list_buckets()

    for bucket in bucket_list:
        print(bucket.name)
