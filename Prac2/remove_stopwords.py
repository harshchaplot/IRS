# REMOVING STOPWORDS AND LOWERCASING

import tokenize as tk

def remove(content):
	stop_words = open("stop_words.txt", "r")
	stopwords = set(tk.tokenize(stop_words.read(), "\n"))
	result = []
	for i in content:
		i = i.lower()
		if i not in stopwords:
			result.append(i)
	return result


