from random import choice
import requests
user_input = input("What would you like to search for? ")
url = "https://www.google.com"
r = requests.get(url, headers={"accept":"application"}, params={"term":user_input}).json()
num = r["total"]
res = r["res"]
if num > 1:
    print(f"I found {num} jokes about {user_input}. Here's one: ")
    print(choice(res)["joke"])
elif num == 1:
    print(f"I found 1 joke about {user_input}")
    print(res[0]["joke"])
else:
    print(f"Sorry, couldn't find joke.")