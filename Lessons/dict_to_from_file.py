import requests
import json

book_data2 = [
    {"name": "Vdovichenko 2", "type": "Shcoder II", "level": 567,
     "book": post_book_with_aut_2.json()['id']},
    {"name": "Vdovichenko 2", "type": "Shcoder II", "level": 115,
     "book": post_book_with_aut_2.json()['id']},
    {"name": "Vdovichenko 2", "type": "Dude", "level": 115,
     "book": post_book_with_aut_2.json()['id']},
    {"name": "Vdovichenko 2", "type": "Dude", "level": 80,
     "book": post_book_with_aut_2.json()['id']}
]

with open('../home_work_8/roles_list_filter.txt', 'w') as output:
    output.write(json.dumps(book_data2))

output.close()


# with open('../home_work_8/books_list.txt', 'r') as output:
#     book = json.loads(str(output.read()))
#     print(book)
#
# output.close()