def display_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


display_details(
    name="Deva",
    age=21,
    course="Python",
    city="Chennai"
)