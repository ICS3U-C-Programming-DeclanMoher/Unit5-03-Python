def grade(level):
    if level == "4++":
        mark = 97
        return mark
    if level == "4+":
        mark = 90
        return mark
    if level == "4":
        mark = 85
        return mark
    if level == "3+":
        mark = 78
        return mark
    if level == "3":
        mark = 74
        return mark
    if level == "3-":
        mark = 70
        return mark
    if level == "2+":
        mark = 67
        return mark
    if level == "2":
        mark = 65
        return mark
    if level == "2-":
        mark = 60
        return mark
    if level == "1+":
        mark = 59
        return mark
    if level == "1":
        mark = 55
        return mark
    if level == "-1":
        mark = 50
        return mark
    if level == "r":
        mark = 10
        return mark


def main():
    user_grade_str = input("Enter your grade:")

    grade_percentage = grade(user_grade_str)
    print(f"{grade_percentage}")


if __name__ == "__main__":
    main()
