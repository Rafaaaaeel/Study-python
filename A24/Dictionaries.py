movie = {
    'title' : 'My life',
    'year' : 2001,
    'cast' : ['Sasha','Noah']
}
movie['title'] = 'My another life'

#       or use the update command

movie.update({'title':'My another and another life', 'year' : 2001, 'cast' : ['Sasha','Noah'] })
movie['budget']= 250000
#print(movie.get('budget','nor found'))
print(movie)

year = movie.pop('year')
print(year)

#del movie['year']

print(movie)

print(movie.keys())

print(movie.values())

#print(movie.items())


movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

for key, value in movie.items():
    print(key, value)


