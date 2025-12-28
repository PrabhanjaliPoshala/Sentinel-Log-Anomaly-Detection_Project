import re

LOG_PATTERN = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<time>.*?)\] "(?P<method>\w+) (?P<url>.*?)" (?P<status>\d+)'
)

def parse_log(line):
    match = LOG_PATTERN.search(line)
    if not match:
        return None
    return match.groupdict()
