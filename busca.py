import DFA

def is_in_search_tree(doc: str, root: DFA.State) -> dict:
    current = root
    apparisons = {}
    chkpoint = 0
    for i in range(len(doc)):
        vt = doc[i]
        if vt in current.transitions:
            if current.current_string == "":
                chkpoint = i
            current = current.transitions[vt][0]
            if current.is_final_state():
                apparisons.setdefault(current.current_string,0)
                apparisons[current.current_string] += 1
                current = root
                i = chkpoint
        elif current.current_string != "":
            i = chkpoint
            current = root
    return apparisons


def main():
    words = ["gripa", "contagio", "distancia", "calentura", "covid", "cansancio", "cubrebocas", "dolor"]
    search_tree = DFA.generate_tree(words)
    apparisons = is_in_search_tree("congripa y sana distancia o cocalenturacovid gripa", search_tree)
    for key, val in apparisons.items():
        print(f"{key} : {val}")

main()