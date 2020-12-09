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


def count_bags(bag_name):
    print("Processing %s with %s" % (bag_name, graph[bag_name]))
    num_bags = 1
    print("Added 1 more bag for %s" % bag_name)
    if graph[bag_name] == '':
        print("%s has no more bags inside" % bag_name)
    else:
        for bag, num in graph[bag_name].items():
            #print("%d %s bags" % (num, bag))
            new_bags = num * count_bags(bag)
            num_bags += new_bags
            print("Added %d more bags for %s" % (new_bags, bag))

    return num_bags


# Take 1 out for the shiny gold bag
total_count = count_bags("shiny gold") - 1
print("Number of bags is %d" % total_count)
