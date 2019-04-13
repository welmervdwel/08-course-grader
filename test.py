from course_grader import course_grader

test_cases = [
    {
        "input": [100, 75, 45],
        "output":  "fail"
    },
    {
        "input": [100, 70, 85],
        "output":  "pass"
    },
    {
        "input": [80, 60, 60],
        "output":  "fail"
    },
    {
        "input": [80, 80, 90, 30, 80],
        "output":  "fail"
    },
    {
        "input": [70, 70, 70, 70, 70],
        "output":  "pass"
    },
    {
        "input": [60, 80, 80, 70, 70],
        "output":  "pass"
    },
]

def test_leap_year_test_cases():
    for test_case in test_cases:
        assignment_response = course_grader(test_case['input'])
        assert assignment_response == test_case[
            'output'], f"""
For
\nInput:    {test_case['input']}
\nExpected: {test_case['output']}
\nGot:      {assignment_response}\n"""
