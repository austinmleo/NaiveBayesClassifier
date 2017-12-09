README

NAIVE BAYES CLASSIFIER
MACHINE LEARNING, FALL 2017

JED MENARD	10652773
AUSTIN LEO	10549295

LANGUAGE: 		Python 2
OPERATING SYSTEM:	Alamode Linux
INSTRUCTIONS:
	The following files must be in the same directory as 20_newsgroups:
	
		main.py
		test.py
		train.py
	
	From the terminal, the program can be run by the following command:
		
		python2 main.py
		
STRUCTURE:
	This program begins by getting the directory name and each file within that directory inside ./20_newsgroups/
	The directory name is used as the classifier and a key to a dictionary where the value is the name of each
	file in the directory.
	For each file in the classifier, each line is read and is split on whitespace and certain non-word characters
	and is then returned to a dictionary of words and their frequency of appearance. Words below a certain length
	threshold are omitted from the word count total to reduce the number of non-word entries and improve 
	computational efficiency.
	For training, we use the first 800 articles of each classifier and get the word counts and probabilities and
	the next 200 articles for testing. Using the posterior probability equation, the frequency of words in the
	test articles, and the total frequency of words in the class the program will output the classification
	accuracy.
	
