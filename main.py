import sys
from analytics.frequent_calls import get_most_frequent_calls
from analytics.time_analysis import get_time_analysis
from log.log_processor import process_log_file


def print_most_frequent_calls(most_frequent_calls_list):
    print("############### Most Frequent Calls ##############")
    print("Method\tURL\tFrequency")
    for call in most_frequent_calls_list:
        print(call[0], call[1], call[2])
    print("##################################################")


def print_time_analysis(time_analytics):
    print("############### Time Analytics ##############")
    print("Method\tURL\tMin Time\tMax Time\tAverage Time")
    for time_stat in time_analytics:
        print(time_stat[0], time_stat[1], time_stat[2], time_stat[3], "{:.2f}".format(time_stat[4]))
    print("##################################################")


if __name__ == '__main__':
    try:
        urls = process_log_file("Sample input - Log Parser (1).csv")
    except FileNotFoundError:
        print("Log file not found at given path")
        sys.exit()
    most_frequent_calls = get_most_frequent_calls(urls, 5)
    print_most_frequent_calls(most_frequent_calls)
    time_analysis = get_time_analysis(urls)
    print_time_analysis(time_analysis)
