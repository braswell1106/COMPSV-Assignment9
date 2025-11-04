class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend is not self and friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"Person '{name}' already exists!")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
        elif person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
        else:
            p1 = self.people[person1_name]
            p2 = self.people[person2_name]
            p1.add_friend(p2)
            p2.add_friend(p1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [f.name for f in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


network = SocialNetwork()


network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")


network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")   
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()




# Test your code here

#memo
#1: A graph is the best way to represent a structured network because it is a data structure that models relationships between entities, where connections can be complex and multidirectional. This means that graphs allow people to be linked to nodes and enable relationships to be connected. So, knowing that people can have multiple friendships, relationships, etc., this is the best setup to find how each one is connected/linked.
#2: A list or tree wouldn't work because of their type of structure. A list wouldn't work because it's linear and can only store people sequentially. The problem is that we can't see the connection they or others may have with one another. It won't work with the tree because it has a single root.