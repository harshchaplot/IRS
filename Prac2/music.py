# PREPROCESSING


# READING FILES

imagine_dragons = open("Music//imagine_dragons.txt", "r")
content_imagine_dragons = imagine_dragons.read()

maroon5 = open("Music//maroon_5.txt", "r")
content_maroon5 = maroon5.read()

one_republic = open("Music//one_republic.txt", "r")
content_one_republic = one_republic.read()

coldplay = open("Music//coldplay.txt", "r")
content_coldplay = coldplay.read()

the_beatles = open("Music//the_beatles.txt", "r")
content_the_beatles = the_beatles.read()


# TOKENIZATION

import tokenize as tk

imagine_dragons_tokenize = tk.tokenize(content_imagine_dragons)

maroon5_tokenize = tk.tokenize(content_maroon5)

one_republic_tokenize = tk.tokenize(content_one_republic)

coldplay_tokenize = tk.tokenize(content_coldplay)

the_beatles_tokenize = tk.tokenize(content_the_beatles)


# REMOVING STOPWORDS AND LOWERCASING

import remove_stopwords as stopwords

imagine_dragons_removed_stopwords = stopwords.remove(imagine_dragons_tokenize)

maroon5_removed_stopwords = stopwords.remove(maroon5_tokenize)

one_republic_removed_stopwords = stopwords.remove(one_republic_tokenize)

coldplay_removed_stopwords = stopwords.remove(coldplay_tokenize)

the_beatles_removed_stopwords = stopwords.remove(the_beatles_tokenize)


# STEMMING

import stemming as stemming

imagine_dragons_stemmed = stemming.stem(imagine_dragons_removed_stopwords)

maroon5_stemmed = stemming.stem(maroon5_removed_stopwords)

one_republic_stemmed = stemming.stem(one_republic_removed_stopwords)

coldplay_stemmed = stemming.stem(coldplay_removed_stopwords)

the_beatles_stemmed = stemming.stem(the_beatles_removed_stopwords)


# import stemming 

# ps = stemming.PorterStemmer()
# print(ps.stem('laughing'))