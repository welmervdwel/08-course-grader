def course_grader(test_scores):
    # define avg_score
    sum = 0
    for num in test_scores:
        sum = sum + num
    avg_score  = sum / len(test_scores)

# if avg score >= 70 AND LOWEST in list >= 50, return "pass"
    if avg_score >= 70 and min(test_scores) >= 50:
        return "pass"
    else:
        return "fail"
    
def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"
    print(course_grader([60,80,80,70,70]))  # "pass"

if __name__ == "__main__":
    main()

