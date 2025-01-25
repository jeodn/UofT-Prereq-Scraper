from bs4 import BeautifulSoup

# Load the HTML file
html_file = "utm_mathsci_academiccalendar.html"
with open(html_file, "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

def get_prerequisites(course_code):
    # Search for the course section
    course_div = soup.find(string=course_code)
    if not course_div:
        return f"Course {course_code} not found."

    # Navigate to the prerequisites section
    prereq_section = course_div.find_next("div", class_="prerequisites")
    if not prereq_section:
        return f"No prerequisites found for {course_code}."

    # Extract and clean the prerequisites text
    prereq_text = prereq_section.get_text(strip=True)
    return prereq_text

if __name__ == '__main__':
    # Example usage
    course_code = "MAT223H5"
    prerequisites = get_prerequisites(course_code)
    print(f"Prerequisites for {course_code}: {prerequisites}")