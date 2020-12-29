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

'''
How its stored:
    Each entry has:
    "BAG NAME STRING", [[BAG COUNT,"BAG NAME STRING"]]
'''

def bag_counter(bag_rule):
    for bag in bag_rule[1]:
        if bag[1] == "shiny gold":
            return True
        else:
            index = 0
            for i in range(len(color_rules)):
                if color_rules[i][0] == bag[1]:
                    index = i
                    break
            
            if bag_counter(color_rules[index]):
                return True
    
    return False
    

count = 0
for bag in color_rules:
    if bag_counter(bag):
        count += 1

print(count)
