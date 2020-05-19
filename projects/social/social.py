import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        
        # # The number of users must be greater than the average number of friendships.
        # if numUsers <= avgFriendships:
        #     print("Number of users must be greater than the average number of friendships")
        #     return 

        for user in range(numUsers):
            self.addUser(user)

        friends = list()
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.lastID+1):
                friends.append((user_id, friend_id))

        for i in range(0, len(friends)):
            random_i = random.randint(i, len(friends) - 1)
            friends[random_i], friends[i] = friends[i], friends[random_i]

        num_friendships = int((numUsers * avgFriendships) / 2)
        friend_list = friends[:num_friendships]

        for pair in friend_list:
            userID = pair[0]
            friendID = pair[1]
            self.addFriendship(userID, friendID)

    def getAllSocialPaths(self, userID):
        visited = {}  
        visited[userID] = [userID]

        q = []
        q.append([userID])

        while len(q) > 0:
            path = q.pop(0)
            curr_friend = path[-1]

            for friend in self.friendships[curr_friend]:
                if friend not in visited:
                    visited[friend] = path
                    new_path = list(path)
                    new_path.append(friend)
                    q.append(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
