class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


people = [
    Person("A", 15, "Montreal"),
    Person("B", 24, "Sherbrooke"),
    Person("C", 62, "Montreal"),
    Person("D", 8, "Montreal"),
    Person("E", 90, "Quebec"),
    Person("F", 34, "Granby"),
    Person("G", 21, "Montreal")
]


def print_stats(people):
    # ***** Part 1 ******
    # Given the class and setup above, implement the print_stats method.
    # The output for calling print_stats(people) should be :
    #   D is young [8]
    #   A is young [15]
    #   G is young [21]
    #   B is not young [24]
    #   F is not young [34]
    #   C is not young [62]
    #   E is not young [90]
    # **********************
    pass


print_stats(people)


def get_city_stats(people):
    # ***** Part 2 ******
    # Given the class and setup below, implement the get_city_stats method.
    # The output for get_city_stats(people) should be :
    #   Granby -> 1
    #   Montreal -> 4
    #   Quebec -> 1
    #   Sherbrooke -> 1
    # **********************
    pass


get_city_stats(people)
