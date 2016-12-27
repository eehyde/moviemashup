import unittest
import requests
import json


price_dictionary = {}

	########## The next three methods simply get a dictionary with information about the movie#######	
	#################################Definitions needed to make URL requests####################

def canonical_order(d):
		alphabetized_keys = sorted(d.keys())
		res = []
		for k in alphabetized_keys:
			res.append((k, d[k]))
		return res

def requestURL(baseurl, params = {}):
		req = requests.Request(method = 'GET', url = baseurl, params = canonical_order(params))
		prepped = req.prepare()
		return prepped.url

CACHE_FNAME = 'cache.json'

try:
		cache_file = open(CACHE_FNAME, 'r')
		cache_contents = cache_file.read()
		CACHE_DICTION = json.loads(cache_contents)
		cache_file.close()
except:
		CACHE_DICTION = {}	

######################################## Start Movie class #####################################

class Movie():
	def __init__(self, movie, year, entity):
		self.name = movie
		self.year = year
		self.entity = entity
	################################# To get a movie's data from iTunes########################

	def getMovieWithiTunes(self):
		BASE_URL = 'https://itunes.apple.com/search'
		full_url = requestURL(BASE_URL, params={'term':self.name,'entity': self.entity,'limit':1, 'releaseYearTerm':self.year})
		if full_url in CACHE_DICTION:
			#print 'using cache'
			# use stored response
			response_text = json.loads(CACHE_DICTION[full_url])
		else:
			#print 'fetching'
			# do the work of calling the API
			response = requests.get(full_url)
			# store the response
			CACHE_DICTION[full_url] = response.text
			response_text = json.loads(response.text)

			cache_file = open(CACHE_FNAME, 'w')
			cache_file.write(json.dumps(CACHE_DICTION))
			cache_file.close()
		return response_text

		################################# To get a movie's data from OMDB########################
	
	def getMovieWithOMDB(self):
		BASE_URL = 'http://www.omdbapi.com/?'
		full_url = requestURL(BASE_URL, params={'t':self.name,'y': self.year,'plot':'short','r':'json'})
		if full_url in CACHE_DICTION:
			#print 'using cache'
			# use stored response
			response_text = json.loads(CACHE_DICTION[full_url])
		else:
			#print 'fetching'
			# do the work of calling the API
			response = requests.get(full_url)
			# store the response
			CACHE_DICTION[full_url] = response.text
			response_text = json.loads(response.text)

			cache_file = open(CACHE_FNAME, 'w')
			cache_file.write(json.dumps(CACHE_DICTION))
			cache_file.close()
		return response_text

		####################### To see if the movie is on netflix (via netflix roulette)########################
	
	def getMovieWithNetflixRoulette(self):
		payload = {'title':self.name,'year':self.year}
		right_name = self.name
		if ' ' in right_name:
			right_name.replace(' ', '%20')
		BASE_URL = 'http://netflixroulette.net/api/api.php?title={}&year={}'.format(right_name, self.year)
		full_url = requests.get(BASE_URL)
		#print full_url.url
		if BASE_URL in CACHE_DICTION:
			#print 'using cache'
			# use stored response
			response_text = json.loads(CACHE_DICTION[BASE_URL])
		else:
			#print 'fetching'
			# do the work of calling the API
			response = requests.get(BASE_URL)
			# store the response
			CACHE_DICTION[BASE_URL] = response.text
			response_text = json.loads(response.text)

			cache_file = open(CACHE_FNAME, 'w')
			cache_file.write(json.dumps(CACHE_DICTION))
			cache_file.close()
		return response_text

		##############################               ###################################
		############################## Other Methods ###################################

	def getPriceFromiTunes(self):
	
		self.response_text = self.getMovieWithiTunes()	
		trackPrice = self.response_text['results'][0]['trackPrice']
		trackRentalPrice = self.response_text['results'][0]['trackRentalPrice']
		trackHDPrice = self.response_text['results'][0]['trackHdPrice']
		trackHDRentalPrice = self.response_text['results'][0]['trackHdRentalPrice']
		if self.name not in price_dictionary:
			price_dictionary[self.name] = (trackPrice, trackRentalPrice, trackHDPrice, trackHDRentalPrice)

		print '\nFor the movie {}, on iTunes it costs: {} to buy, {} to rent, {} to buy in HD, and {} to rent in HD'.format(self.name,trackPrice,trackRentalPrice,trackHDPrice,trackHDRentalPrice)
		return trackPrice

	def getRatingfromOMDB(self):

		self.response_text = self.getMovieWithOMDB()
		imdbRating = self.response_text['imdbRating']
		Metascore_rating = self.response_text['Metascore']
		print "\nThe movie {} has a rating of {} from imdb (scale: 1-10), and a score of {} from Metascore (scale: 1-100)".format(self.name, imdbRating,Metascore_rating)
		return imdbRating

	def ismovieonNetflix(self):

		self.response_text = self.getMovieWithNetflixRoulette()
		if 'errorcode' in self.response_text.keys():
			print '\nSorry, this movie is not on nextflix'
			return 'Sorry, this movie is not on nextflix'
		else:
			print '\nThis movie is available to watch on Netflix'
			return 'This movie is available to watch on Netflix'

	def getPlotfromiTunes(self):

		self.response_text = self.getMovieWithiTunes()		
		plot = self.response_text['results'][0]['longDescription']
		print '\nThe plot is:',plot,'\n'

	def aboutMoviefromiTunes(self):
		
		self.response_text = self.getMovieWithiTunes()
		genre = self.response_text['results'][0]['primaryGenreName']
		time_millis = self.response_text['results'][0]['trackTimeMillis']
		time_hours = (time_millis/3600000.00)
		print '\n{} is a {} movie and is {} hours long'.format(self.name,genre,time_hours)
		return genre



######################################## End Movie class #####################################



chosen_movie = raw_input('Please enter a movie followed by a year in this format: Frozen,2013)')
str(chosen_movie)
the_movie =[]
the_movie.append(chosen_movie.split(','))
for x in the_movie:
	a = x[0]
	b = x[1]
movie_input = Movie(a,b, 'movie')
movie_input.aboutMoviefromiTunes()	
movie_input.getPriceFromiTunes()
movie_input.getRatingfromOMDB()
movie_input.ismovieonNetflix()
movie_input.getPlotfromiTunes()
some_input = raw_input('Would you like to get information on another movie to compare them? (answer yes or no)')
str(some_input)
some_input.lower()
if some_input == 'yes':
	next_movie = raw_input('Please enter a movie followed by a year in this format: Frozen,2013)')
	str(next_movie)
	the_next_movie =[]
	the_next_movie.append(next_movie.split(','))
	for y in the_next_movie:
		c = y[0]
		d = y[1]
	the_next_movie = Movie(c,d, 'movie')	
	the_next_movie.aboutMoviefromiTunes()
	the_next_movie.getPriceFromiTunes()
	the_next_movie.getRatingfromOMDB()
	the_next_movie.ismovieonNetflix()
	the_next_movie.getPlotfromiTunes()
	what_to_compare = raw_input('Would you like to compare the price of these two movies? (type "price" to compare price, type "no" to quit)')
	str(what_to_compare)
	what_to_compare.lower()
	if what_to_compare == 'price':
		sorted_prices = sorted(price_dictionary, key = lambda q: price_dictionary[q])
		price_dictionary_values = price_dictionary.values()
		if price_dictionary_values[0] == price_dictionary_values[1]:
			print 'These movies cost the same'
		else:	
			print sorted_prices[0],'is the cheaper movie'

	else:
		print 'Thank you for using my program!'
if some_input == 'no':
	print 'Thank you for using my program!'



############################ Test Cases ##############################
print '\n\n ----------Test Cases---------- \n'
print '---Testing the class methods----'
Forrest_Gump = Movie("Forrest Gump", 1994, 'movie')
netflix = Forrest_Gump.ismovieonNetflix()
rating1 = Forrest_Gump.getRatingfromOMDB()
Frozen = Movie("Frozen", 2013, 'movie')
netflix2 = Frozen.ismovieonNetflix()
price1 = Frozen.getPriceFromiTunes()
genre1 = Frozen.aboutMoviefromiTunes()
print '-------------Results-------------'
class Problem1(unittest.TestCase):
	def test1(self):
		self.assertEqual(Forrest_Gump.name,'Forrest Gump','Testing to see that the class constructor works for the year')
	def test2(self):	
		self.assertEqual(netflix,'This movie is available to watch on Netflix', 'Testing that the ismovieonNetflix function can correctly say if a movie is on Netflix')
	def test3(self):
		self.assertEqual(netflix2,'Sorry, this movie is not on nextflix', 'Testing that the ismovieonNetflix function can correctly say if a movie is on Netflix')	
	def test4(self):
		self.assertEqual(price1, 14.99,'Testing to see if the getPriceFromiTunes function gets the right prce')
	def test5(self):
		self.assertEqual(rating1, '8.8', 'Testing that the getRatingfromOMDB function gets the right rating')
	def test6(self):
		self.assertEqual(genre1, 'Kids & Family','Testing that aboutMoviefromiTunes returns the correct genre')	
unittest.main(verbosity=2)




