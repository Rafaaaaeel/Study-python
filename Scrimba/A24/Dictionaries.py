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
#print(movie)

#year = movie.pop('year')
#print(year)

#del movie['year']

#print(movie)

print('-------------------')
print(movie.keys())
print('-------------------')
print(movie.values())
print('-------------------')
print(movie.items())
print('-------------------')

movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}

for key, value in movie.items():
    print(key, value)


new_dict = {'rafael':19,'wagner':57,'sasha':2}

sum_ages = sum(new_dict.values())

formated = ', '.join(new_dict.keys())

print(len(new_dict))