from flask import Flask, flash, request, redirect, render_template, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
import os
import urllib.request
import sqlite3

import random
from search_preprocess import Indexer, Search
from werkzeug.utils import secure_filename
import re

import pickle
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

from gensim.parsing.preprocessing import STOPWORDS

from spellchecker import SpellChecker
import random
from docx import Document
from auto_tagging_script import AutoTags

from final_script_fulldb import get_summary, writeTofile, PreProcess
from main import main
from ready_for_search import *
from document_similarity import get_similar_documents


def get_text_from_docx_document(file):
    try:
        doc = Document(file)
        temp = ''
        for para in doc.paragraphs:
            temp += para.text
        return temp
    except Exception:
        print('Raising......')
        raise Exception


def clean_query(query):
    # lemmatization

    query = re.sub("'s", "", query)
    query = re.sub("s'", "", query)

    query = re.sub("n't", " not", query)

    # Perform Lemmatization on query.
    lemmed = [WordNetLemmatizer().lemmatize(word)
              for word in word_tokenize(query) if word not in STOPWORDS]
    lemmed = [WordNetLemmatizer().lemmatize(word, pos='v') for word in lemmed]

    spell = SpellChecker()
    if os.path.exists(os.path.join(os.getcwd(), "MyDictionary.json")):
        spell.word_frequency.load_dictionary("MyDictionary.json")

    misspelled = spell.unknown(lemmed)
    new_query = query
    if len(misspelled) == 0:
        return lemmed, query, new_query
    else:
        correct_words = list(set(lemmed) - misspelled)
        correction = []

        for word in misspelled:
            # Get the one `most likely` answer
            correction.append(spell.correction(word))

        for i in range(len(correction)):
            new_query = new_query.replace(list(misspelled)[i], correction[i])

        # cleaned query--
        lemmed = correct_words + correction

        print(f"Searching for {new_query} instead of {query}")
        return lemmed, query, new_query


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hard to guess string'

app.config['MAX_CONTENT_LENGTH	'] = 1024 * 1024 * 1024
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'docx', 'pptx']


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def load_corpus_and_data_files():
    global data, titles, auto_tag, summary, document_file

    data = pickle.load(open(r"DataBase/data_file.pkl", "rb"))
    titles = pickle.load(open(r"DataBase/title_file.pkl", "rb"))
    auto_tag = pickle.load(open(r"DataBase/svos_file.pkl", "rb"))
    summary = pickle.load(open(r"DataBase/summary_file.pkl", "rb"))
    document_file = pickle.load(open(r"DataBase/document_file.pkl", "rb"))


def load_search_data_files():
    global search_data_for_relevance, search_data_for_tag, search_data_for_title
    search_data_for_relevance = pickle.load(
        open(r"DataBase/search_file_relevance.pkl", "rb"))
    search_data_for_tag = pickle.load(
        open(r"DataBase/search_file_tag.pkl", "rb"))
    search_data_for_title = pickle.load(
        open(r"DataBase/search_file_title.pkl", "rb"))


@app.before_first_request
def load_all_data():
    load_corpus_and_data_files()

    global data_for_text
    data_for_tag = pickle.load(open(r"DataBase/tags_pickle.pkl", "rb"))
    data_for_text = pickle.load(open(r"DataBase/corpus_file.pkl", "rb"))
    data_for_title = pickle.load(open(r"DataBase/title_corpus.pkl", "rb"))

    if os.path.exists(os.path.join(os.getcwd(), "DataBase/search_file_relevance.pkl")) == False:
        objj = Indexer(data_for_text, search_type="relevance")
        objj.create_files()

    if os.path.exists(os.path.join(os.getcwd(), "DataBase/search_file_tag.pkl")) == False:
        objj = Indexer(data_for_tag, search_type="tag")
        objj.create_files()

    if os.path.exists(os.path.join(os.getcwd(), "DataBase/search_file_title.pkl")) == False:
        objj = Indexer(data_for_title, search_type="title")
        objj.create_files()

    load_search_data_files()

    print("all data loaded...")


the_exception_text = 0


@app.route('/')
def index():
    if(the_exception_text == -1):
        page_exception_text = -1
    elif(the_exception_text == 1):
        page_exception_text = 1
    else:
        page_exception_text = 0
    return render_template('index.html', var_path=var_path, page_exception_text=page_exception_text)


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        entered_text = request.form['search_bar']
        applied_filter_type = request.form['filter_type_name_holder']
        if applied_filter_type == "Search by Relevance":
            the_text = entered_text
            mystring = "Relevance"
            query = the_text

            # Cleaning of query
            tokenized_query, old_query, new_query = clean_query(query.lower())

            # Creating object for Search class with Data of "search_file_relevance.pkl"
            obj = Search(search_data_for_relevance)
            # Get the results
            indexes, results = obj.get_top_n(tokenized_query, data, n=10)

            results_titles = []
            results_summaries = []
            results_tags = []

            # Loop over all indexes of resultants documents, and create the list of resultant titles,
            # summaries and tags to pass them on HTML page.

            for i in indexes:
                results_titles.append(titles[i])
                results_summaries.append(summary[i])
                if auto_tag[i] != []:
                    results_tags.append(
                        list(set(random.choices(auto_tag[i], k=3))))
                else:
                    results_tags.append(['No Auto tags'])
            text = []

            # Loop over the results list and create the list of parts of texts to pass on HTML page
            for i in results:
                # Get the at most 2 sentences from text of document to show them on screen
                text_to_show = " ".join(sent_tokenize(i)[:2])
                if text_to_show != '':
                    text.append(text_to_show + '....')
                else:
                    # If we didn't get any text to show, that can be due to the very small document which doesn't
                    # contain any full stop. In that case, append whole text that document has.
                    text.append(i)

            title = results_titles
            summaries = results_summaries
            tags = results_tags

            title_len = len(title)

            extension_list = []
            for i in indexes:
                extension_list.append(document_file[i]["extension"])

            return render_template('searchbyText.html', text=text, tag=query, title=title, summaries=summaries, tags=tags,
                                   type=mystring, title_len=title_len, old_query=old_query, new_query=new_query,
                                   extension_list=extension_list, the_text=the_text)

        elif applied_filter_type == "Search by Tag":
            # return redirect(url_for('viewSearchbyTag', the_text=entered_text))
            the_text = entered_text
            mystring = "Tag"
            query = the_text

            # Cleaning of query---
            tokenized_query, old_query, new_query = clean_query(query.lower())

            # Creating object for Search class with Data of "search_file_tag.pkl"
            obj = Search(search_data_for_tag)

            # Get the results
            indexes, results = obj.get_top_n(tokenized_query, data, n=10)

            results_titles = []
            results_summaries = []
            results_tags = []

            # Loop over all indexes of resultants documents, and create the list of resultant titles,
            # summaries and tags to pass them on HTML page.

            for i in indexes:
                results_titles.append(titles[i])
                results_summaries.append(summary[i])
                if auto_tag[i] != []:
                    results_tags.append(
                        list(set(random.choices(auto_tag[i], k=3))))
                else:
                    results_tags.append(['No Auto tags'])

            # Loop over the results list and create the list of parts of texts to pass on HTML page
            text = []
            for i in results:
                # Get the at most 2 sentences from text of document to show them on screen
                text_to_show = " ".join(sent_tokenize(i)[:2])
                if text_to_show != '':
                    text.append(text_to_show + '....')
                else:
                    text.append(i)

            title = results_titles
            summaries = results_summaries
            tags = results_tags

            title_len = len(title)

            extension_list = []
            for i in indexes:
                extension_list.append(document_file[i]["extension"])

            return render_template('searchbyText.html', text=text, tag=query, title=title, summaries=summaries, tags=tags,
                                   type=mystring, title_len=title_len, old_query=old_query, new_query=new_query,
                                   extension_list=extension_list, the_text=the_text)

        elif applied_filter_type == "Search by Title":
            # return redirect(url_for('viewSearchbyTitle', the_text=entered_text))
            the_text = entered_text
            mystring = "Title"
            query = the_text

            # Cleaning of query---
            tokenized_query, old_query, new_query = clean_query(query.lower())

            # Creating object for Search class with Data of "search_file_title.pkl"
            obj = Search(search_data_for_title)
            # Get the results
            indexes, results = obj.get_top_n(tokenized_query, data, n=10)

            results_titles = []
            results_summaries = []
            results_tags = []

            # Loop over all indexes of resultants documents, and create the list of resultant titles,
            # summaries and tags to pass them on HTML page.

            for i in indexes:
                results_titles.append(titles[i])
                results_summaries.append(summary[i])
                if auto_tag[i] != []:
                    results_tags.append(
                        list(set(random.choices(auto_tag[i], k=3))))
                else:
                    results_tags.append(['No Auto tags'])
            text = []
            for i in results:
                # Get the at most 2 sentences from text of document to show them on screen
                text_to_show = " ".join(sent_tokenize(i)[:2])
                if text_to_show != '':
                    text.append(text_to_show + '....')
                else:
                    text.append(i)
            title = results_titles
            summaries = results_summaries
            tags = results_tags

            title_len = len(title)

            extension_list = []
            for i in indexes:
                extension_list.append(document_file[i]["extension"])
            return render_template('searchbyText.html', text=text, tag=query, title=title, summaries=summaries, tags=tags,
                                   type=mystring, title_len=title_len, old_query=old_query, new_query=new_query,
                                   extension_list=extension_list, the_text=the_text)

    return redirect('/')


@app.route('/', methods=['POST'])
def upload_file():
    global the_exception_text
    if request.method == 'POST':
        if 'files[]' not in request.files:
            return redirect(request.url)
        files = request.files.getlist(r'files[]')

        # the_requested_tag holds tha value of entered tag

        the_requested_tag = request.form['just_the_tag']
        print(the_requested_tag)
        print(files[0].filename)

        file_upload = files[0].filename

        manual_tags = the_requested_tag.lower().strip().split(',')

        # taking filename as a title
        title = " ".join(file_upload.split('.')[:-1])

        try:
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(
                        app.config['UPLOAD_FOLDER'], filename))
                    break

            # go to that file and read it
            file_upload = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            print(file_upload)
            main(file_upload, title, manual_tags)
            # after completion of processsing delete that file from folder.
            os.remove(file_upload)

            load_corpus_and_data_files()
            load_search_data_files()

            the_exception_text = 1
            return redirect('/')

        except Exception:
            the_exception_text = -1
            print("Exception raised ---")
            return redirect('/')


var_path = ""


@app.route('/path', methods=['POST'])
def choose():
    app.config['UPLOAD_FOLDER'] = ""
    global var_path
    var_path = request.form.get('folder_path')

    print(var_path)
    app.config['UPLOAD_FOLDER'] = var_path

    return redirect('/')


# tempdiv = ""
myclassname = ""

# NOT WORKING


@app.route('/filenameonclick', methods=['GET', 'POST'])
def filenameonclick():
    mymessage = "OOPS! Viewing function is not available currently! We will soon make it functional!!"
    return render_template('checkworking.html', mymessage=mymessage)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
