with open("DATA/Day7Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

color_rules = []

for rule in data:
    rule_string = rule.split()
    contained_bags = []

    for i, text in enumerate(rule_string[4:]):
        if text == "bag." or text == "bags." or text == "bag," or text == "bags,":
            contained_bags.append([int(rule_string[i-3]),rule_string[i-2] + " " + rule_string[i-1]])
        
    color_rules.append([rule_string[0] + " " + rule_string[1], contained_bags])

print(color_rules)