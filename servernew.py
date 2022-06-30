from flask import Flask,render_template,url_for,request,redirect
import csv

app = Flask(__name__,template_folder='template')
#print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

#---------use this code instead of adding each and every page
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('dbnew.txt',mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('dbnew.csv',mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
       # write_to_file(data)                  ------------for writing to db
        write_to_csv(data)                     #------------writing to csv
        return redirect('thankyou.html')
    else:
        return 'something went wrong'

# @app.route("/about.html")
# def about():
#     return render_template('about.html')
#
# @app.route("/work.html")
# def work():
#     return render_template('work.html')
#
# @app.route("/works.html")
# def works():
#     return render_template('works.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')




if __name__=='__main__':
    app.run(debug=True)

