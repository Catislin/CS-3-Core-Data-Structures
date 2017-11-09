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
    longest_match = 0
    longest_match_index = -1
    for index, route_cost_pair in enumerate(route_costs): # go through each (route, cost) pair
        route = route_cost_pair[0]
        route_length = len(route)
        if route == phone_number[:route_length] and route_length > longest_match:
            longest_match = route_length
            longest_match_index = index

    if longest_match == 0 or longest_match_index == -1:
        print("route not found!")

    return route_costs[longest_match_index][1]





if __name__ == '__main__':
    #print(read_in_phone_numbers('phone-numbers-10.txt'))
    # print(read_in_route_costs('route-costs-10.txt'))
    routes = read_in_route_costs('route-costs-106000.txt')
    phone_number = '+6498418344'
    print(find_cost(phone_number, routes))
    phone_number = '+8613870265'
    print(find_cost(phone_number, routes))
