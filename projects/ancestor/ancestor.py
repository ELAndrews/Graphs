class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def earliest_ancestor(ancestors, starting_node):
    has_ancestors = False

    for ancestor in ancestors:
        if ancestor[1] == starting_node:
            has_ancestors = True
    
    if has_ancestors is False:
        return -1
    
    q = Queue()
    q.enqueue([starting_node])
    ancestors_found = []

    while q.size() > 0:
        path = q.dequeue()

        curr_ancestor = path[-1]
        has_new_ancestors = False

        for ancestor in ancestors:
            if ancestor[1] == curr_ancestor:
                has_new_ancestors = True
                next_ancestor = list(path)
                next_ancestor.append(ancestor[0])
                q.enqueue(next_ancestor)

        if has_new_ancestors == False:
            ancestors_found.append(path)
            continue

    longest = 0
    paths = []

    for path in ancestors_found:
        if len(path) > longest:
            paths = []
            longest = len(path)
            paths.append(path[-1])
            continue
        elif len(path) == longest:
            paths.append(path[-1])

        
    lowest_ancestor = min(paths)
    print(lowest_ancestor)
    return lowest_ancestor