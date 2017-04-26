from collections import deque

graph = dict()

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == "m"


def breadth_first_search(name):

    search_sequence = deque()
    search_sequence += graph[name]

    searched = []

    while search_sequence:

        person = search_sequence.popleft()

        if person not in searched:

            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_sequence += graph[person]
                searched += person

    return False


breadth_first_search("you")
