from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/food')
def food():
    return render_template('add_food.html')

def create_app():
    return app.run(debug=True)

if __name__=='__main__':
    create_app()