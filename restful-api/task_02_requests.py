import requests
import csv

def fetch_and_print_posts():
    u = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(u)
    print("Status Code:", r.status_code)
    if r.status_code == 200:
        j = r.json()
        for p in j:
            print(p['title'])

def fetch_and_save_posts():
    u = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(u)
    if r.status_code == 200:
        j = r.json()
        l = []
        for i in j:
            d = {'id': i['id'], 'title': i['title'], 'body': i['body']}
            l.append(d)
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=['id','title','body'])
            w.writeheader()
            w.writerows(l)
