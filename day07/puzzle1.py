graph = {}

# O(N)
with open('rules.txt', 'r') as rules_file:
    for rule in rules_file:
        container, contents = rule.split(' bags contain ')
        #print("Container is %s" % container)
        if contents.strip() == "no other bags.":
            #print("No other bags detected!")
            graph[container] = ''
        else:
            bags = {}
            for content in contents.split(', '):
                #print("Content is %s" % content.strip())
                num_bags = int(content.split(' ')[0])
                bag_type = content[content.index(' '):content.index(' bag')].strip()
                #print("There are %d bags of type '%s'" % (num_bags, bag_type))
                bags[bag_type] = num_bags
            graph[container] = bags


def find_shiny_gold(contents):
    print("Trying to find shiny gold in %s" % contents)
    if contents == '':
        return False
    elif "shiny gold" in contents.keys():
        print("Found shiny gold")
        return True
    else:
        for content in contents.keys():
            if content in processed.keys():
                print("%s already processed, reusing it" % content)
                if processed[content]:
                    return True
            elif find_shiny_gold(graph[content]):
                processed[content] = True
                return True
            else:
                processed[content] = False
        return False

# Avoid recalculating already calculated graphs
processed = {}
count = 0
# O(N)
for container, contents in graph.items():
    print("Processing %s container with %s contents" % (container, contents))
    if container in processed.keys():
        if processed[container]:
            count += 1
    elif find_shiny_gold(contents):
        count += 1
        processed[container] = True
    else:
        processed[container] = False

#print(graph)


print("Count is %d" % count)
