import json

a = 'MAT102H5 • Introduction to Mathematical Proofs'
print(a)

JSON_FILE = "courses.json"


def add_course(course_id, course_name, prerequisites):
    # Load the existing JSON data
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Create the new course dictionary
    new_course = {
        "id": course_id,
        "name": course_name,
        "prerequisites": prerequisites
    }

    # Append the new course to the courses list
    data["courses"].append(new_course)

    # Save the updated data back to the JSON file
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
    print(f"Course {course_id} added successfully!")

if __name__ == "__main__":
        
    course = input('Course code and name: ')
    prereqs = input('Course prerequisites: ')

    c_id, c_name = course.split(' • ') 
