# moviemashup

106 Final Project Readme

1. Describe your project in 1-4 sentences. Include the rationale for doing it, the basic idea, and the output that it should generate.

My project draws data from multiple online sources about one or two movies. I chose to do this because I constantly find myself having to go to multiple different websites to get small bits of informaton about a movie. My program will tell you the price of the movie to buy and rent in standard definition and HD off iTunes, the the rating from IMDB and Metascore, the plot, the genre and runtime, and if the movie is available to watch on netflix. It can also compare the price of two movies to tell you which one would be cheaper to watch.

2. Explain exactly what needs to be done to run your program (what file to run, anything the user needs to input, anything else) and what we should see once it is done running (should it have created a new text file or CSV? What should it basically look like?).

To being running the program, type 'python FinalProject.py' into the terminal. (Make sure you are in the correct directory first). Then you will be prompted the rest of the way through the program. As a note, when entering a movie and a year do NOT include a space after or before the comma.(There is an example in the prompt, and in the cahed examples below) The program will simply print all output into the terminal window.

(Your program running should depend on cached data, but OK to write a program that would make more sense to run on live data and tell us to e.g. use a sample value in order to run it on cached data.)

Movie options if you want to run it on cached data:
Frozen,2013
Mulan,1998
Tangled,2010
Sabrina,1995
Forrest Gump,1994
Pulp Fiction,1994
Inception,2010

3. Any Python packages/modules that must be installed in order to run your project (e.g. requests ...):

unittest, requests, and json must be installed.

4. What data sources did you use? Provide links here and any other description necessary.

- The iTunes API --> https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/#searchexamples
- The OMDB API --> https://www.omdbapi.com
- The Netflix Roulette API --> http://netflixroulette.net/api/


5. Rationale for project: why did you do this project? Why did you find it interesting? Did it work out the way you expected?

I chose this project because I was interested in the subtle differences between a couple different APIs that gave information about movies. My intention was to build a program that combined that information, so that you could get information on price, plot, rating, and if it was on Netflix all in one place. For the most part it worked as expected except for the fact that the Netflix Roulette required spaces in the url to be encoded with a '%20' instead of a '+', but once I was able to figure out a workaround for that, the program (including making requests, caching, defining classes,testing,etc) all worked out as expected. 


Help/Contributions:
My first three methods in the Class Movie are adapted (and are almost exactly the same) from the code from lecture, as is the code for caching. The code I am refering to is: 
- lines 11-31 (caching/requests)
- the method getMovieWithiTunes
- the method getMovieWithOMDB
- the method getMovieWithNetflixRoulette

