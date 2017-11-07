import re

def read_in_phone_numbers(filename):
    """Takes in the name of a file with normalized phone numbers and returns them as a list"""
    phone_numbers_file = open(filename)
    phone_numbers_list = phone_numbers_file.read().splitlines()
    phone_numbers_file.close()
    return phone_numbers_list

def read_in_route_costs(filename):
    """Takes in the name of a file with a phone route and its cost separated by a comma
    and returns a list of lists each containing a route and its cost"""
    routes_and_costs_list = []
    routes_file = open(filename)
    split_lines = routes_file.read().splitlines()
    for line in split_lines:
        routes_and_costs_list.append([x.strip() for x in line.split(',')])
    return routes_and_costs_list

def find_cost(phone_number, route_costs):
    """Takes in a phone number in string format and a list containing route costs
    and finds the cost of calling the phone number from that list"""
    for route_list in route_costs:
        route = route_list[0]
        route_index = 0
        #longest_match_index = -1
        

# def contains(text, pattern, start=None):
#     """Return a boolean indicating whether pattern occurs in text."""
#     assert isinstance(text, str), 'text is not a string: {}'.format(text)
#     assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
#     # TODO: Implement contains here (iteratively and/or recursively)
#     # iterative:
#     if pattern == '':
#         return True
#     text_index = 0
#     while text_index != len(text):
#         for i in range(len(pattern)):
#             if text_index + i < len(text):
#                 if text[text_index + i] != pattern[i]:
#                     break
#                 if i == len(pattern) - 1:
#                     return True
#         text_index += 1
#     return False



if __name__ == '__main__':
    #print(read_in_phone_numbers('phone-numbers-10.txt'))
    # print(read_in_route_costs('route-costs-10.txt'))
    routes = read_in_route_costs('route-costs-106000.txt')
    phone_number = '+15124156620'
    find_cost(phone_number, routes)
