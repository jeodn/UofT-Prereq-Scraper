from typing import *
from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

with open("courses.json") as f:
    COURSE_DATA = {c["code"]: c for c in json.load(f)["courses"]}

def expand_course(code):
    """Expand course code into its prerequisite tree recursively."""
    course = COURSE_DATA.get(code)
    if not course:
        return {"name": f"{code} (Unknown)"}

    prereq_list = course.get("prerequisites_list")
    if not prereq_list:
        return {"name": code}

    return parse_prereq_tree(prereq_list)

def parse_prereq_tree(tree: Union[list[str], None]):
    if isinstance(tree, str):
        return {"name": tree}

    if isinstance(tree, list):
        op = tree[0]
        children = [parse_prereq_tree(item) for item in tree[1:]]
        return {"name": op.upper(), "children": children}

    return {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data/<course_code>")
def get_prerequisites(course_code):
    if course_code not in COURSE_DATA:
        return jsonify({"error": "Course not found"}), 404

    return jsonify(expand_course(course_code))

if __name__ == "__main__":
    app.run(debug=True)
