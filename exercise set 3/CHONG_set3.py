#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #get user handle of first/lastname
    for key, value in social_graph.items():
        if value["first_name"] == from_member[0:from_member.find(" ")] and value["last_name"] == from_member[from_member.find(" ")+1:len(from_member)]:
            from_member = key
            break
    for key, value in social_graph.items():
        if value["first_name"] == to_member[0:to_member.find(" ")] and value["last_name"] == to_member[to_member.find(" ")+1:len(to_member)]:
            to_member = key
            break
      
    relationship = "no relationship"
    if to_member in social_graph.get(from_member).get('following'):
        relationship = "follower"
    if relationship == "follower":
        if from_member in social_graph.get(to_member).get('following'):
            relationship = "friends"
            return relationship
        else: return relationship
    else: 
        if from_member in social_graph.get(to_member).get('following'):
            relationship = "followed by"
            return relationship
        else: return relationship


def tic_tac_toe(board):
    '''Tic Tac Toe.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    mega = []
    n = len(board)

    for row in board:  #group horizontals
        mega.append(row)  
    for col in range(n): #verticals
        mini1 = []
        for row in range(n):
            mini1.append(board[row][col])
        mega.append(mini1)
    mini2 = []  #main diagonal \
    for times in range(n):
        mini2.append(board[times][times])
    mega.append(mini2)
    #anti-diagonal /
    mini3 = []
    for times in range(n):
        col = n - 1 - times
        mini3.append(board[times][col])
    mega.append(mini3)
    
    #look for the group that has all same symbols
    for mini in mega:
        if mini[0] != '' and all(mini[0] == mini[i] for i in range(1, n)):
            return mini[0]
    return 'NO WINNER'

def eta(first_stop, second_stop, route_map):
    '''ETA.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if first_stop == second_stop: #not moving
        return 0
    key_list = list(route_map.keys()) #determine the index of which the Stop is in the dictionary
    for i in key_list:
        if i[0] == first_stop:
            first_stop_index = key_list.index(i)
    for j in list(route_map.keys()):
        if j[1] == second_stop:
            second_stop_index = key_list.index(j)
    
    total_travel_time = 0
    if first_stop_index <= second_stop_index:
        for k in range(first_stop_index,second_stop_index+1):
            travel_time = route_map[key_list[k]]["travel_time_mins"]
            total_travel_time += travel_time
    else: #wrapping around the dictionary
        for l in range(first_stop_index,len(route_map)):
            travel_time = route_map[key_list[l]]["travel_time_mins"]
            total_travel_time += travel_time
        for l in range(0,second_stop_index+1):
            travel_time = route_map[key_list[l]]["travel_time_mins"]
            total_travel_time += travel_time
    return total_travel_time

