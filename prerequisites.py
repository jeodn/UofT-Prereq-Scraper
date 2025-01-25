"""
Query a course and get all of its prerequisites.
"""
import json

with open('courses.json', 'r') as file:
    data = json.load(file)

courses = data['courses']

class Course:
    id: str
    name: str
    prerequisites: list

    def __init__(self, id, name, prerequisites):
        self.id = id
        self.name = name
        self.prerequisites = prerequisites 

    def __str__(self):
        return f"{self.id}: {self.name} \n\t{self.prerequisites}\n"

#for course in courses:
    #print(course, type(course))

if __name__ == "__main__":
    new_course = Course('MAT136H5', 'Integral Calculus', [ 'MAT132H5', 'MAT135H5','MAT137H5','MAT157H5','MAT135H1', 'MATA29H3', 'MATA30H3', 'MATA31H3'])
    print(new_course)

# scrape website
# https://utm.calendar.utoronto.ca/section/Mathematical-Sciences