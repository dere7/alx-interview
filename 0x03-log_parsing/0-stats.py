#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


def print_stat(status_codes, tot_file_size):
    """print stat for specified inputs"""
    print('File size: {}'.format(total_file_size))
    for k, v in sorted(status_code_counts.items(), key=lambda i: i[0]):
        if v != 0:
            print('{}: {}'.format(k, v))


if __name__ == '__main__':
    status_codes = [400, 200, 301, 401, 403, 404, 405, 500]
    status_code_counts = {str(status): 0 for status in status_codes}
    total_file_size = 0
    line_count = 0
    while True:
        try:
            line = input()
            line_count += 1
            status_code, file_size = line.split(' ')[-2:]
            if int(status_code) not in status_codes:
                continue
            status_code_counts[status_code] += 1
            total_file_size += int(file_size)
            if line_count == 10:
                print_stat(status_code_counts, total_file_size)
                # reset after printing
                status_code_counts = {
                    str(status): 0 for status in status_codes}
                total_file_size = 0
                line_count = 0
        except KeyboardInterrupt:
            print_stat(status_code_counts, total_file_size)
            exit(1)
