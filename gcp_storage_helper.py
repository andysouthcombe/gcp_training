from google.cloud import storage
import glob
import os

storage_client = storage.Client()


def list_buckets():
    buckets = storage_client.list_buckets()
    return buckets


def check_bucket_exists(bucket_name):
    buckets_in_project = list_buckets()
    return any(bucket_in_project.name == bucket_name for bucket_in_project in buckets_in_project)


def create_bucket(bucket_name):
    storage_client.create_bucket(bucket_name)


def get_bucket_contents(bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    return bucket.list_blobs()


def copy_file_to_bucket(bucket_name, source_file_path, destination_blob_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_path)


def copy_file_pattern_to_bucket(bucket_name, source_file_path, source_file_pattern):
    files = glob.glob(source_file_path + source_file_pattern)
    for file in files:
        copy_file_to_bucket(bucket_name, file, os.path.basename(file))


if __name__ == "__main__":

    target_bucket_name = "skating_inbound_bucket"
    source_file_path = "/home/andy/git/2018-02-olympic-figure-skating-analysis/data/"

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