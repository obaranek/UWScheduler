import json

from flask import Flask, request
from flask_cors import CORS
import Optimize
from control.CourseData import get_data

app = Flask(__name__)
CORS(app)

def get_optimized_courses(list):
    best_options = Optimize.optimize(list[0], list[1], list[2], list[3], list[4])
    return best_options


@app.route('/')
def index():
    return "Success"


@app.route('/getCourses', methods=['POST'])
def getInfo():
    print("Accepting request")
    jsonobject = json.dumps(request.json);
    dict = json.loads(jsonobject)
    arr = dict['courses']
    data = get_optimized_courses(get_data(arr))
    return data


if __name__ == '__main__':
    app.run(debug=True)

