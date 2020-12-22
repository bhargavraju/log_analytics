from heapq import nlargest


def get_most_frequent_calls(url_dict, k):
    calls = []
    for url in url_dict:
        for http_method in url_dict[url]:
            calls.append((http_method, url, len(url_dict[url][http_method])))
    most_frequent = nlargest(k, calls, key=lambda x: x[2])
    return most_frequent
