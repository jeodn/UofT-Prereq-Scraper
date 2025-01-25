from bs4 import BeautifulSoup

# Load the HTML file
html_file = "webpages/utm_mathsci/utm_mathsci.html"
with open(html_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

def get_prerequisite_text(department_name, course_code, course_title):
    # Courses only section

    subject = "Mathematical Sciences Courses"
    courses_sec = soup.find(string=department_name)

    # Search for the course section
    course_div = courses_sec.find_next(string=f"Introduction to Discrete Mathematics")
    if not course_div:
        return f"Course {course_code} not found."
    
    print(course_div)

    # Navigate to the prerequisites section
    prereq_div = course_div.find_next("div", class_="views-field views-field-field-desc")
    if not prereq_div:
        return f"No prerequisites found for {course_code}."

    print(prereq_div)

    # Navigate to the prerequisites section
    prereq_section = prereq_div.find_next("span")
    if not prereq_section:
        return f"No prerequisites found for {course_code}."

    # Extract and clean the prerequisites text
    prereq_text = prereq_section.get_text()
    return prereq_text

if __name__ == '__main__':
    # Example usage
    subject = "Mathematical Sciences Courses"
    course_code = "MAT202H5"
    prerequisites = get_prerequisite_text(subject, course_code)
    print(f"{course_code}: {prerequisites}")