import requests

r = requests.get('http://pulse-rest-testing.herokuapp.com/roles/')

roles = r.json()
print(roles)

types = [role['type'] for role in roles]
uniq_types = list(set(types))

max_level_in_types = dict.fromkeys(uniq_types, 0)
print(max_level_in_types)
# max_level_in_types = {}
for role in roles:
    if role["level"] > max_level_in_types[role['type']]:
        max_level_in_types[role["type"]] = role['level']




# max_level_in_types = {}
# for item in uniq_types:
#     max_level_in_types[item] = 0


# max_level = 0
# for role in roles:
#     if role["level"] > max_level:
#         max_level = role['level']
#
# max_level_2 = max([role['level'] for role in roles])
#
# print(max_level)
# print(max_level_2)

