"""
    Chapter10 正则表达式与json
    Part 2 json

    json.loads():
    json --> python 反序列化
    json object --> dict
    json array  --> list
    true / false --> True / False
    string --> str
    number --> int / float
    null  --> None

"""
import json

jsonStr = '{"name":"Jacky","sex":"male","age":15}'
student = json.loads(jsonStr)
print(student)

jsonArrStr = '''
            [
                {"name":"Jacky","sex":"male","age":15,"flag":false},
                {"name":"Pony","sex":"female","age":25,"flag":null}
            ]
            '''
people = json.loads(jsonArrStr)
print(people)

"""
    json.dumps()
    python --> json 序列化
"""
students = [
            {'name': 'Jacky', 'sex': 'male', 'age': 15, 'flag': False},
            {'name': 'Pony', 'sex': 'female', 'age': 25, 'flag': None}
            ]
jsonStrs = json.dumps(students)
print(jsonStrs)
