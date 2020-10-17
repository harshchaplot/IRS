from tkinter import *
import tkinter.messagebox as tkMessageBox
import os
import numpy as np
import tokeniser as tkn


def searchQuery(query, text_files, stats_dict, Number_of_docs, doc_list, idf_dict, list_of_words):

    processed_query = tkn.tokenise_normalise(query)  # normalising the query

    final_query = processed_query

    final_query = tkn.stem(final_query)  # stemming the query

    final_query = [x for x in final_query if x in stats_dict]
    if final_query:
        # print final_query

        query_dict = tkn.create_tf_dict_query(final_query)  # finding tf scores for each query word

        query_dict = tkn.find_tfidf_query(query_dict, idf_dict,
                                          Number_of_docs)  # find tf-idf scores for each query word

        vector_array = np.zeros((len(query_dict.keys()), Number_of_docs))

        i = 0
        j = 0

        query_vector = np.zeros((1, len(query_dict.keys())))

        for w in query_dict:
            # create tf-idf vector for each document for each word in query
            query_vector[0][i] = query_dict[w]
            for d in doc_list:
                if d not in stats_dict[w]:
                    j += 1
                else:
                    vector_array[i][j] = stats_dict[w][d]
                    j += 1
            i += 1
            j = 0

        vector_array[np.isnan(vector_array)] = 0

        q_magnitude = np.linalg.norm(query_vector, axis=1)  # changing the query vector to unit vector
        query_vector = np.divide(query_vector, q_magnitude)

        dot_product = np.dot(query_vector, vector_array)  # finding the dot product of each document vector with query vector.
        dot_product = dot_product.tolist()

        final_rank = list(zip(dot_product[0], doc_list))  # sorting the cosine scores to rank the documents.
        final_rank.sort(reverse=True)
        searchf = Tk()
        searchf.wm_title(query + "-Harsh's Search Engine")
        blank = '           '
        blanklabel = Label(searchf, text=blank * 20, font=("ComicSansMS", 10))
        label1 = Label(searchf, text='Query entered: '+query + '\n\n', font=("ComicSansMS", 20))
        label1.pack()
        blanklabel.pack()

        for i in final_rank[:5]:
            labl = Label(searchf, text=i[1], font=("ComicSansMS", 15), justify=LEFT)
            labl.bind("<Button-1>")
            labl.pack()

    else:
        tkMessageBox.showinfo("Are yr!!", "Kuch nhi mila, Sorry!!",
                              icon='warning')  # if query is empty, print error message.


corpus_dir = "corpus"  # getting text files

text_files = [os.path.join(corpus_dir, f) for f in os.listdir(corpus_dir)]
stats_dict = {}

Number_of_docs = len(text_files)  # getting number of docs

doc_list = []

for f in text_files:  # reading each doc
    doc = open(f, 'r')
    lines = [l.strip() for l in doc.readlines()]

    index = 0

    full_transcript = []

    while True:
        if index >= len(lines):
            break
        line = lines[index]
        full_transcript.append(line)
        index += 1
    # tokenising and stemming text
    processed_text = tkn.tokenise_normalise(full_transcript)
    processed_text = tkn.stem(processed_text)
    stats_dict = tkn.create_tf_dict_doc(processed_text, f, stats_dict)  # creating tf dictionary
    doc_list.append(f)

stats_dict, idf_dict = tkn.find_tfidf_doc(stats_dict, Number_of_docs)

list_of_words = sorted(stats_dict.keys())
doc_list.sort()

top = Tk()
top.wm_title("Harsh's Search Engine")
f = Frame(top, width=600, height=350)
f.pack(fill=X, expand=True)

e1 = Entry(top, bd=6, width=40)
e1.insert(END, 'Search here')
e1.place(relx=0.5, rely=0.35, anchor=CENTER)
b1 = Button(top, text="Search",
            command=lambda: searchQuery(e1.get(), text_files, stats_dict, Number_of_docs, doc_list, idf_dict,
                                        list_of_words))
b1.place(relx=0.5, rely=0.5, anchor=CENTER)
top.mainloop()
