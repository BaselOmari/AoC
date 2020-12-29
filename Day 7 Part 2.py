with open("DATA/Day7Data.txt", 'r') as f:
    data = f.readlines()

data = [line.strip() for line in data]

color_rules = []
for rule in data:
    rule_string = rule.split()
    contained_bags = []

    if rule[-22:] != "contain no other bags.":
        for i, text in enumerate(rule_string[4:]):
            x = i+4
            if text == "bag." or text == "bags." or text == "bag," or text == "bags,":
                contained_bags.append([int(rule_string[x-3]),rule_string[x-2] + " " + rule_string[x-1]])
        
    color_rules.append([rule_string[0] + " " + rule_string[1], contained_bags])

# First find the gold details

sg_index = 0
for i, bag in enumerate(color_rules):
    if bag[0] == "shiny gold":
        sg_index = i
        break


def bag_counter(index_bg):
    bag_rule = color_rules[index_bg]
    count = 0
    for sub_rule in bag_rule[1]:
        for sub_count in range(sub_rule[0]):
            index = 0
            for i, bag in enumerate(color_rules):
                if bag[0] == sub_rule[1]:
                    index = i
                    break
            count += 1 + bag_counter(index) 
    return count

print(bag_counter(sg_index))
