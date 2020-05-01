from gcp_pubsub_publish_helper import *
import json

project_name = "gcp-learning-project-274814"
target_bucket_name = "skating_inbound_bucket"
source_file_path = "/home/andy/git/2018-02-olympic-figure-skating-analysis/data/"
source_file_name = 'judge-scores.csv'
topic_name = "andy_test"
topic_path = "projects/" + project_name + "/topics/" + topic_name


def get_top_n_lines_of_file(filename, num_of_lines):
    with open(filename) as f:
        lines = [next(f) for x in range(num_of_lines)]
        return lines


if __name__ == "__main__":
    lines_to_send = get_top_n_lines_of_file(source_file_path + source_file_name, 5)
    key_list = lines_to_send[0].split(",")
    json_list = []
    for line in lines_to_send[1:]:
        values = line.split(",")
        this_line_dict = {}
        for index, value in enumerate(values):
            this_line_dict.update({key_list[index]: value})
        json_list.append(json.dumps(this_line_dict))

    for message in json_list:
        publish_pubsub_message(topic_path,message)

