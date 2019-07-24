from flask import Flask
import render_template
app = Flask(__name__)
@app.route('/')

def index():
    '''return 'Hello world, Bridget Sitsofe is my name.
am a young girl of twenty-one years old. '''
    
    return render_template('main.html')
    
@app.route('/whereami')
def whereami():
    return 'Ghana!'
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 