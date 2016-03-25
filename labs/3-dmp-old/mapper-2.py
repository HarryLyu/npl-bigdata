import sys

user_categories = {}
lines = open('user-categories.txt', 'r').read().split("\n")
for line in lines:
    data = line.strip().split("\t")
    if len(data) > 2:
        uid, category = data
        if uid not in user_categories.keys():
            user_categories[uid] = {}
        user_categories[uid][category] = 1

def is_valid_data (data):
    return data != '' and data != '-'

categories_order = ['2', '12', '13', '14']

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 3:
        uid, date, url = data
        if is_valid_data(uid):
            string = uid
            if uid in user_categories.keys():
                for category in categories_order:
                    if category in user_categories[uid]:
                        string = string + "\t" + user_categories[uid][category]
                    else:
                        string = string + "\t" + "0"
            else:
                string = string + ("\t0" * 4)
            print string