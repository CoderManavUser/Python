import random
when=["Once upon a time","Yesterday","A long time ago","On 21st December","There was once a"]
who=["Mary","Jane Eyre","Red Riding Hood","Peter Pan","Cinderella","Moby Dick","Harry Potter"]
where=["London","New York","Neverland","Venice","Madrid","Washington D.C"]
went=["School","Cinema","House","University","Airport","Club"]
what=["solved a mystery","killed someone","had a dinner","found a dead body","had a class","met friends"]
print(random.choice(when)+","+ random.choice(who)+" who lived in "+ random.choice(where)+" went to " +random.choice(went)+random.choice(what))