import csv
from collections import defaultdict
from .url_modifier import id_replacer


def process_log_file(file_path):
    urls = defaultdict(dict)
    with open(file_path) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            raw_url = row[1]
            http_method = row[2]
            response_time = int(row[3])
            processed_url = id_replacer(raw_url)
            if processed_url in urls:
                if http_method in urls[processed_url]:
                    urls[processed_url][http_method].append(response_time)
                else:
                    urls[processed_url][http_method] = [response_time]
            else:
                urls[processed_url] = {http_method: [response_time]}
    return urls
