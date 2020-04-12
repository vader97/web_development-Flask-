from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello Puppy</h1>'


@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'


# Dynamic Routing
@app.route('/puppy/<name>')
def puppy_name(name):
    return '<h1> This is a page for {}</h1>'.format(name)


@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    if name:
        if name[-1] == 'y':
            name = name[:-1] + "iful"
        else:
            name = name + 'y'
        return "<h1>Puppy Latin name is {}</h1>".format(name)
    else:
        return '<h1>Please Enter valid String</h1>'


@app.route('/developer/pic')
def pic():
    return render_template('basics.html')


if __name__ == '__main__':
    app.run(debug = True)
