import json
from account import Account
from restaurant import Restaurant
from service import MainService

account = Account(input("사용자 아이디를 입력하세요.\n>> "))

with open("restaurants.json", "r", encoding="utf-8") as file:
    restaurants = [Restaurant(**data) for data in json.load(file)]

MainService(account, restaurants)
