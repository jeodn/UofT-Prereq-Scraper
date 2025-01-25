import json
from scrape2 import get_prerequisite_text, get_course_title, html_content

JSON_FILE = "courses.json"


def add_course(course_code, course_title, prerequisites):
    # Load the existing JSON data
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Create the new course dictionary
    new_course = {
        "code": course_code,
        "title": course_title,
        "prerequisites": prerequisites
    }

    # Append the new course to the courses list
    data["courses"].append(new_course)

    # Save the updated data back to the JSON file
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    print(f"Course {course_code} added successfully!")

if __name__ == "__main__":
        
    course_code = input('Course code: ')
    course_title = get_course_title(course_code)
    course_prereqs = get_prerequisite_text(course_code)

    add_course(course_code, course_title, course_prereqs)


