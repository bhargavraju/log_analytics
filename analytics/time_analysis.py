def get_time_analysis(url_dict):
    time_data = []
    for url in url_dict:
        for http_method in url_dict[url]:
            time_data.append((http_method, url, min(url_dict[url][http_method]), max(url_dict[url][http_method]),
                              sum(url_dict[url][http_method])/len(url_dict[url][http_method])))
    return time_data
