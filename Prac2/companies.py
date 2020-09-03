# PREPROCESSING


# READING FILES

facebook = open("Companies//facebook.txt", "r")
content_facebook = facebook.read()

apple = open("Companies//apple.txt", "r")
content_apple = apple.read()

amazon = open("Companies//amazon.txt", "r")
content_amazon = amazon.read()

netflix = open("Companies//netflix.txt", "r")
content_netflix = netflix.read()

google = open("Companies//google.txt", "r")
content_google = google.read()


# TOKENIZATION

import tokenize as tk

facebook_tokenize = tk.tokenize(content_facebook)

apple_tokenize = tk.tokenize(content_apple)

amazon_tokenize = tk.tokenize(content_amazon)

netflix_tokenize = tk.tokenize(content_netflix)

google_tokenize = tk.tokenize(content_google)


# REMOVING STOPWORDS AND LOWERCASING

import remove_stopwords as stopwords

facebook_removed_stopwords = stopwords.remove(facebook_tokenize)

apple_removed_stopwords = stopwords.remove(apple_tokenize)

amazon_removed_stopwords = stopwords.remove(amazon_tokenize)

netflix_removed_stopwords = stopwords.remove(netflix_tokenize)

google_removed_stopwords = stopwords.remove(google_tokenize)


# STEMMING

import stemming as stemming

facebook_stemmed = stemming.stem(facebook_removed_stopwords)

apple_stemmed = stemming.stem(apple_removed_stopwords)

amazon_stemmed = stemming.stem(amazon_removed_stopwords)

netflix_stemmed = stemming.stem(netflix_removed_stopwords)

google_stemmed = stemming.stem(google_removed_stopwords)

