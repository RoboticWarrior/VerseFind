from flask import Flask, request, render_template, redirect
import os
import random
from datetime import date

app = Flask(__name__)

def get_file(file_path, write = None):
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
    return render_template('homepage.html')

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