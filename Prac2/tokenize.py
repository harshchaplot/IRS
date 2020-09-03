# TOKENIZATION

def tokenize(content, separator=" "):
	content_list = []
	s = ""
	for i in content:
		if i != separator:
			s += i
		else:
			content_list.append(s)
			s = ""
	content_list.append(s)
	return content_list