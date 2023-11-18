import re


def check_domain_name(input_string):
    pattern = re.compile(r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+(?:[a-zA-Z]{2,})$', re.VERBOSE)
    return bool(re.match(pattern, input_string))


input_string = "stankin.rus.moscow.www"
print(check_domain_name(input_string))
input_string = "stankin..www"
print(check_domain_name(input_string))