#!/usr/bin/env python
import re


def parse_input(lines):
    initial_re = re.compile(r"^([\w]*\s[\w]*)\sbags\scontain\s([\d]*)\s([\w]*\s[\w]*)\s[bags]{3,4}")
    additional_clause_re = re.compile(r"\s*(\d*)\s(\w*\s*\w*)\s[bags]{3,4}")
    rules = {}
    for line in lines:
        if 'contain no other' in line:
            rule_name = " ".join(line.split()[0:2])
            if rule_name in rules.keys():
                raise KeyError(f"Duplicate bag definition for {rule_name}")
            rules[rule_name] = {}
            continue
        splitline = line.split(",")

        # set up initial clause of rule
        initial_check = initial_re.match(splitline[0])
        if not initial_check:
            raise ValueError("Initial rule pattern matching failed!")
        groups = initial_check.groups()
        rule_name = groups[0]
        clause_val = int(groups[1])
        clause_name = groups[2]
        if rule_name in rules.keys():
            raise KeyError(f"Duplicate bag definition for {rule_name}")
        rules[rule_name] = {clause_name: clause_val}

        # add subsequent clauses from the same line to the rule
        for clause in splitline[1:]:
            check = additional_clause_re.match(clause)
            if not check:
                raise ValueError("Clause pattern matching failed!")
            groups = check.groups()
            clause_val = int(groups[0])
            clause_name = groups[1]
            if clause_name in rules[rule_name].keys():
                raise KeyError(f"Duplicate clause '{clause_name}' in rule {line}")
            rules[rule_name][clause_name] = clause_val
    return rules


def follow_bag(rules, bagname):
    if len(rules[bagname]) == 0:
        return False
    if 'shiny gold' in rules[bagname].keys():
        return True
    for sub_bag in rules[bagname].keys():
        found = follow_bag(rules, sub_bag)
        if found:
            return True


def part_one_recursion(rules):
    print("*** PART 1 (recursion) ***")
    total = 0
    for bagname in rules.keys():
        cah_hold_shiney = follow_bag(rules, bagname)
        if cah_hold_shiney:
            total += 1
    print(f"A total of {total} bags eventually may contain a shiny gold bag.")
    return total


def find_containing_bags(childname, rules):
    containing_bags = []
    for bagname, bag_rules in rules.items():
        if childname in bag_rules.keys():
            containing_bags.append(bagname)
    return containing_bags


def part_one(rules):
    print("*** PART 1 ***")
    shiney_bag_containers = []
    for bag_name in rules.keys():
        if 'shiny gold' in rules[bag_name].keys():
            shiney_bag_containers.append(bag_name)
    shiney_bag_containers = set(shiney_bag_containers)
    total = len(shiney_bag_containers)
    while True:
        new_bags = []
        for bag in shiney_bag_containers:
            new_bags.extend(find_containing_bags(bag, rules))

        new_bags = set(new_bags)  # dump duplicates
        shiney_bag_containers.update(new_bags)

        if len(shiney_bag_containers) == total:
            break  # no new bags were found!
        else:
            total = len(shiney_bag_containers)

    print(f"A total of {total} bags eventually may contain a shiny gold bag.")
    return total


def verify_rules(lines, rules):
    """ compare generated rules to line contents """
    for rule_name, rule in rules.items():
        for line in lines:
            if line.lower().startswith(rule_name.lower()):
                for clause_name, clause_val in rule.items():
                    if f"{clause_val} {clause_name}" not in line:
                        raise ValueError("SOMETHING'S WRONG!")


def part_two(rules):
    print("*** PART 2 ***")
    total = (total_bag(rules, "shiny gold", 1) - 1)  # extra -1 is because we don't count the shiny gold bag itself.
    print(f"A single shiny gold bag leads to {total} overall.")
    return total


def total_bag(rules, bagname, total):
    if len(rules[bagname]) == 0:  # contains no more bags
        return total
    subtotal = 0
    for sub_bag, sub_bag_multiple in rules[bagname].items():
        subtotal += total_bag(rules, sub_bag, sub_bag_multiple)
    return (subtotal * total) + total


if __name__ == "__main__":
    print("*** EXAMPLE ***")
    with open("../7.example.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        bag_rules = parse_input(lines)
        verify_rules(lines, bag_rules)
        assert part_one(bag_rules) == 4
        assert part_one_recursion(bag_rules) == 4
    with open("../7.example2.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        bag_rules = parse_input(lines)
        verify_rules(lines, bag_rules)
        assert part_two(bag_rules) == 126
    print("\n*** MY INPUT ***")
    with open("../7.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        bag_rules = parse_input(lines)
        verify_rules(lines, bag_rules)
        assert part_one(bag_rules) == 332
        assert part_one_recursion(bag_rules) == 332
        assert part_two(bag_rules) == 10875
