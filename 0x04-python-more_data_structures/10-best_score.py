#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        if len(a_dictionary) > 0:
            best_keys = []
            max_score = max(a_dictionary.values())
            print (max_score)
            for key, value in a_dictionary.items():
                if value == max_score:
                    best_keys.append(key)
            return best_keys
    return None
