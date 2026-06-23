# Course Recommendation System

# Dictionary containing interests and corresponding courses
course_catalog = {
    "datascience": [
        "Data Science 101",
        "Introduction to Machine Learning",
        "Data Visualization with Python"
    ],
    "webdevelopment": [
        "HTML and CSS Basics",
        "JavaScript for Beginners",
        "Building Websites with Flask"
    ],
    "cybersecurity": [
        "Introduction to Cybersecurity",
        "Network Security Fundamentals",
        "Ethical Hacking"
    ],
    "artificial intelligence": [
        "AI for Everyone",
        "Deep Learning Basics",
        "AI Ethics and Society"
    ],
    "business": [
        "Business Management 101",
        "Marketing Strategies",
        "Financial Accounting"
    ]
}

# Function to get user interests
def get_user_interests():
    interests = []

    print("Please enter your interests one by one.")
    print("Type 'done' when you are finished.")

    while True:
        interest = input("> ").strip().lower()

        if interest == "done":
            break

        interests.append(interest)

    return interests

# Function to recommend courses
def recommend_courses(interests):
    recommended_courses = []

    for interest in interests:
        if interest in course_catalog:
            recommended_courses.extend(course_catalog[interest])

    return recommended_courses

# Function to display recommendations
def display_recommendations(recommended_courses):
    if recommended_courses:
        print("\nBased on your interests, we recommend the following courses:\n")

        for course in recommended_courses:
            print(f"- {course}")
    else:
        print("Sorry, we couldn't find any courses matching your interests.")

# Main Program
user_interests = get_user_interests()
recommended_courses = recommend_courses(user_interests)
display_recommendations(recommended_courses)
