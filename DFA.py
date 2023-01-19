class State:
    def __init__(self, current_string: str):
        self.current_string = current_string
        self.transitions = {}

    def is_final_state(self):
        return len(self.transitions) == 0


def extend_node(w: str):
    start = State(w[0])
    previous = start
    for c in w[1:]:
        next = State("")
        next.current_string = previous.current_string + c
        if previous.transitions.get(c):
            previous.transitions[c].append(next)
        else:
            previous.transitions[c] = [next]
        previous = next
    return start


def generate_tree(list_of_words):
    root = State("")
    for word in list_of_words:
        word_node = extend_node(word)
        ptr = root
        for i, v in enumerate(word):
            if ptr.transitions.get(v):
                ptr = ptr.transitions[v][0]
            else:
                ptr.transitions[v] = [word_node]
                break
            word_node = word_node.transitions[word[i + 1]][0]
    return root
