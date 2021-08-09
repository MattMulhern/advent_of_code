#!/usr/bin/env python
import re


def part_one(passports):
    """ my correct answer was 206 """
    print("*** PART 1 ***")
    valid_passports = []
    for passport in passports:
        if pass_is_valid(passport):
            valid_passports.append(passport)
    print(f"Ignoring a missing'cid' field, there are {len(valid_passports)} valid passports out of {len(passports)}")
    return valid_passports


def part_two(passports):
    """ my correct answer was 123 """
    print("*** PART 2 ***")
    valid_passports = []
    for passport in passports:
        if validate_passport(passport):
            valid_passports.append(passport)
    print(f"Ignoring a missing'cid' field and validating fields, there are {len(valid_passports)} valid passports out of {len(passports)}")  # noqa: E501


def chunk_to_passport(chunk):
    passport = {}
    for line in chunk:
        for pair in line.split():
            key, val = pair.split(":")
            if key in passport.keys():
                raise KeyError(f"Chunk has multiple copies of {key}: {chunk}")
            passport[key] = val
    return passport


def chunk_lines(lines):
    chunks = []
    chunks.append([])
    chunk_id = 0
    for line in lines:
        chunks[chunk_id].append(line)
        if len(line) == 0:
            chunk_id += 1
            chunks.append([])
    return chunks


def get_missing_keys(passport, ignore_cid=True):
    mandatory_keys = ["ecl", "eyr", "hcl", "pid", "iyr", "byr", "hgt"]
    if not ignore_cid:
        mandatory_keys.append("cid")
    missing_keys = []
    for key in mandatory_keys:
        if key not in passport.keys():
            missing_keys.append(key)
    return missing_keys


def pass_is_valid(passport, ignore_cid=True):
    num_valid_fields = 8
    if len(passport.keys()) == num_valid_fields:
        return True
    elif (ignore_cid and (len(passport.keys()) == (num_valid_fields - 1)) and ("cid" not in passport.keys())):
        # print('igniring optional cid missing')
        return True
    # print(f"invalid [{get_missing_keys(passport)}] -> {passport.keys()}")
    return False


def validate_passport(passport, ignore_cid=True):
    for key, val in passport.items():
        if key == "byr":
            if not (1920 <= int(val) <= 2002):
                # print(f"byr: {val:<10}  :  {passport}")
                return False

        elif key == "iyr":
            if not (2010 <= int(val) <= 2020):
                # print(f"iyr: {val:<10}  :  {passport}")
                return False

        elif key == "eyr":
            if not (2020 <= int(val) <= 2030):
                # print(f"eyr: {val:<10}  :  {passport}")
                return False

        elif key == "hgt":
            if val.lower().endswith("cm"):
                if not (150 <= int(val.strip("cm")) <= 193):
                    # print(f"hgt: {val:<10}  :  {passport}")
                    return False
            elif val.lower().endswith("in"):
                if not (59 <= int(val.strip("in")) <= 76):
                    # print(f"hgt: {val:<10}  :  {passport}")
                    return False
            else:
                # print(f"hgt: {val:<10}  :  {passport}")
                return False

        elif key == "hcl":
            if not re.match("^#[0-9a-f]{6}$", val.lower()):
                # print(f"hcl: {val:<10}  :  {passport}")
                return False

        elif key == "ecl":
            if val.lower() not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                # print(f"ecl: {val:<10}  :  {passport}")
                return False

        elif key == "pid":
            if not re.match("^[0-9]{9}$", val):
                # print(f"pid: {val:<10}  :  {passport}")
                return False
        elif key == "cid":
            pass  # don't validate cid
        else:
            print(f"got missing key {key}  :  {passport}")
            return False
    return True


if __name__ == "__main__":
    # with open("../4.example.input.txt", "r") as fp:
    # with open("../4.invalids.txt", "r") as fp:
    # with open("../4.valids.txt", "r") as fp:
    with open("../4.input.txt", "r") as fp:
        lines = fp.readlines()
        passlines = [x.strip() for x in lines]  # strip newlines
        chunks = chunk_lines(passlines)
        passports = [chunk_to_passport(x) for x in chunks]
        print(f"checking {len(passports)} passports for valid field values")
        passports_with_valid_keys = part_one(passports)
        part_two(passports_with_valid_keys)
