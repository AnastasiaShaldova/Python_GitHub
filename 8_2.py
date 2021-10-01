import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as my_list:
    for line in my_list:
        RE_LOGS = re.findall(r'(^\S+)(?:\s\S){3}(\S+\s\S{5})(?:\S\s)(\S+)(?:\s)(\S+)(?:\s+\S+\s)(\d+\s)(\d)', line)
        print(RE_LOGS)

