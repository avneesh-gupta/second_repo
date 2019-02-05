# git@github.com:avneesh-gupta/second_repo.git
import json


def greet(obj):
    print("hello ",obj)


def print_all(obj):

    obj = json.loads(obj)
    for k in obj:
        print(k, obj[k])
