from bs4 import BeautifulSoup

with open(r"C:\\Users\\ismat\\Documents\\home.html", "r", encoding="utf-8") as html_file:
    content = html_file.read()
    #print(content)

    soup = BeautifulSoup(content, "lxml")
    header_tags = soup.find_all('h1')
    for header in header_tags:
        print(header.text,'\n')
    courses_cards = soup.find_all('div',class_='course-card')
    for course in courses_cards:
        course_name = course.find('h3').text
        course_info = course.find('p').text
        course_price = course.find('a').text
        print(f"{course_name} : {course_info} \n {course_price}")
