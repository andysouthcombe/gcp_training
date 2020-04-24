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


