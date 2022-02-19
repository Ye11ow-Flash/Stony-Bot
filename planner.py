# planner.py
# 02.19.2022

import json

def writeJSON(filename, data):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4,sort_keys=True)
    return True

def readJSON(filename):
    with open(filename, 'r') as infile:
        data = json.load(infile)
    return data

def add_course(user, course, code, semester):
    plan_json = readJSON('planner.json')
    if user in plan_json:
        if semester in plan_json[user]:
            plan_json[user][semester].append(course + " " + code)
        else:
            plan_json[user][semester] = [course + " " + code]
    else:
        plan_json[user] = {semester: [course + " " + code]}
    writeJSON('planner.json', plan_json)

def remove_course(user, course, code):
    plan_json = readJSON('planner.json')
    if user not in plan_json:
        return "You have no registered courses"
    for key, value in plan_json[user].items():
        for i in value:
            if i == course + " " + code:
                plan_json[user][key].remove(i)
                writeJSON('planner.json', plan_json)
                return "Course successfully removed"
    return "Was unable to find course"

def move_course(user, course, code, oldsem, newsem):
    plan_json = readJSON('planner.json')
    if user not in plan_json:
        return "You have no registered courses"
    add_course(user, course, code, newsem)
    if oldsem in plan_json[user]:
        if course + " " + code in plan_json[user][oldsem]:
            plan_json[user][oldsem].remove(course + " " + code)
            writeJSON('planner.json', plan_json)
            return f"Successfully moved {course} {code}"
        else:
            return f"Could not find {course} {code} in {oldsem}. Added it to {newsem} anyway"
    return f"Could not find {oldsem} in your planner lol. Added course to {newsem} anyway"

def planner(user):
    leader = "```\n"
    plan_json = readJSON('planner.json')
    if user not in plan_json:
        return "You have no registered courses"
    for key,value in plan_json[user].items():
        if value != []:
            leader += f"{key}\n"
            for i in value:
                leader += "- " + i + "\n"
    return leader +  "```"