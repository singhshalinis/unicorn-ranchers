from flask import Flask, render_template, request
import handlers

class Unicorn:
    def __init__(self, name, color, location):
        self.name = name
        self.color = color
        self.location = location

app = Flask(__name__)
app.config['DEBUG'] = True

# from base import session
# from models import Unicorn

unicorn_list = []

@app.route('/', methods=['GET'])
def home():
    return render_template('index-01.html')


@app.route('/unicorn', methods=['GET'])
def getUnicorns():
    unicorns = getAllUnicorns()
    return render_template('index.html', unicorns=unicorns)


def getAllUnicorns():
    unicorn_list.append(Unicorn(name="U1", color="Brown", location='Barn'));
    unicorn_list.append(Unicorn(name="U2", color="Pink", location='Barn'));
    # print unicorn_list
    return unicorn_list


@app.route('/changestate/<unicorn_name>/<location>',methods=['POST', 'GET'])
def change_state(unicorn_name, location):
    if request.method == 'POST':
        # print unicorn_list
        for unicorn in unicorn_list:
            if unicorn.name == unicorn_name:
                unicorn.location = location
        # response.status_code = 204
        return "success", 204
    else:
        return render_template('index-01.html')
