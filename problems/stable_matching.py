'''
@Description: Stable-Matching / Gale-Shapley Algorithm https://en.wikipedia.org/wiki/Stable_marriage_problem
'''

import collections

preferred_rankings_men = {
	'ryan':  ('lizzy', 'sarah', 'zoey', 'daniella'),
	'josh':  ('sarah', 'lizzy', 'daniella', 'zoey'),
	'blake': ('sarah', 'daniella', 'zoey', 'lizzy'),
	'connor':('lizzy', 'sarah', 'zoey', 'daniella')
}

preferred_rankings_women = {
	'lizzy':   ('ryan', 'blake', 'josh', 'connor'),
	'sarah':   ('ryan', 'blake', 'connor', 'josh'),
	'zoey':    ('connor', 'josh', 'ryan', 'blake'),
	'daniella':('ryan', 'josh', 'connor', 'blake') 
}

tentative_engagements = []

free_men = []

def init_free_men():
    for man in preferred_rankings_men.items():
        free_men.append(man[0])

def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            print()
            begin_matching(man)

def begin_matching(man):
    print(f"Dealing with {man}")
    for woman in preferred_rankings_men[man]:
        taken_match = [couple for couple in tentative_engagements if woman in couple]

        if len(taken_match) == 0:
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print(f"{man} is now tentatively engaged to {woman}")
            break

        elif len(taken_match) > 0:
            current_match = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_match = preferred_rankings_women[woman].index(man)
            # print(current_match, potential_match)

            if current_match < potential_match:
                print(f"No luck with {woman}")
            
            else:
                print(f"{man} is now tentatively engaged to {woman}, and {taken_match[0][0]} is free man.")
                free_men.remove(man)
                free_men.append(taken_match[0][0])
                taken_match[0][0] = man
                break


if __name__ == "__main__":
    init_free_men()
    stable_matching()
    print(tentative_engagements)