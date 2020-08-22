from flask import Flask, render_template, request, redirect
import csv
import postgres
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

#GOING TO ROUTE TO ADDRESS THAT WAS ASKED FOR BY USING A VARIABLE 
@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)
'''
@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/components.html')
def component():
    return render_template('components.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/variable/<username>/<int:post_id>')
def variable(username = None, post_id = None):
    return render_template('index.html', name = username, post_id = post_id)
'''
def write_to_file(data):
    with open(r'C:\Users\luken\OneDrive\Documents\Complete_Python_Developer_2020 _Zero_to_Hero\web_server\database.txt','a') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open(r'C:\Users\luken\OneDrive\Documents\Complete_Python_Developer_2020 _Zero_to_Hero\web_server\database.csv',newline='',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

def write_to_database(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    postgres.insert(email,subject,message)

@app.route('/submit_form', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')#IN CASE SUBMITION WORKED, REDIRECT THE CLIENT TO THIS PAGE
        except:
            return 'Did not save in the database'
    else: 
        return 'something went wrong. Try again!'

if __name__ == '__main__':
    app.run(debug=True)