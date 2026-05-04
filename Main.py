from flask import Flask, request, render_template, redirect
from Page_render import Page
import os
import random
from datetime import date

app = Flask(__name__)

home_page = Page({
    'header': {'data': 'VerseFind', 'size': 80},
    'body': {'data': 'Our only mission is to let you know that Jesus Christ loves you and is Lord', 'size': 60}
    })

def get_file(file_path: str, write: str = None):
    if write == None:
        if os.path.exists(file_path):
            file_open = open(file_path, 'r')
            file_read = file_open.readlines()
            file_open.close()
            retvar = file_read

        else:
            retvar = 'None'

        return retvar
    
    else:
        file_open = open(file_path, 'w')
        file_open.write(write)
        file_open.close()

@app.route('/')
def homepage():
    return render_template('homepage.html', header=home_page.render('header', 'data'))

@app.route('/salpage')
def salpage():
    return render_template('salpage.html')

@app.route('/versepage')
def versepage():
    current_date = str(date.today())

    if get_file('vod.txt')[0].strip() != current_date:
        get_book = get_file('Bible_books/kjv.txt')
        get_file('vod.txt', f'{current_date}\n{get_book[random.randint(0, len(get_book) - 1)].strip()}')

    verse = get_file('vod.txt')[1]

    return render_template('versepage.html', verse=verse)

@app.route('/search_page,html')
def searchpage():
    return render_template('searchpage.html')

@app.route('/load_page', methods=['POST'])
def load_page():
    page = request.get_data(as_text=True)

    if page == 'home':
        return redirect('/')
    
    elif page == 'salpage':
        return redirect('/salpage')
    
    elif page == 'vodpage':
        return redirect('/versepage')
    
    elif page == 'search_page':
        return redirect('/searchpage')
    
    return 'None'

if __name__ == '__main__':
    app.run(debug=True)