from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

## 코딩 할 준비 ##

View_star = db.movies.find_one({'title': '월-E'})

print(View_star['star'])


movies = list(db.movies.find({'star':View_star}))
View_star = movies['star']

for View_star in movies:

print(View_star['title'])




