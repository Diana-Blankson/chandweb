
from flask import Flask, render_template


app = Flask(__name__)


#@app.route('/')
#def index():
#    return ('Hello world')


@app.route('/foo')
def foo():
    return render_template('foo.html')


#@app.route('/whereami')
#def whereami():
#    return 'Ghana'

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Services')
def Services():
    return render_template('Services.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
