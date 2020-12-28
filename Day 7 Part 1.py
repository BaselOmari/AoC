with open("DATA/Day7Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

color_rules = []

count = 0
for rule in data:
    rule_string = rule.split()
    contained_bags = []

    if rule[-22:] != "contain no other bags.":
        for i, text in enumerate(rule_string[4:]):
            x = i+4
            if text == "bag." or text == "bags." or text == "bag," or text == "bags,":
                contained_bags.append([int(rule_string[x-3]),rule_string[x-2] + " " + rule_string[x-1]])
        
    color_rules.append([rule_string[0] + " " + rule_string[1], contained_bags])

    count += 1