new_input = input()
time_of_right_answers = dict()
time_of_wrong_answers = dict()
number_of_solved_problems = 0
total_time_measure = 0
while new_input != '-1':
    time_into_competition, problem_name, problem_status = [x for x in new_input.split(' ')]
    time_into_competition = int(time_into_competition)
    if problem_status == 'right':
        if problem_name in time_of_right_answers:
            time_of_right_answers[problem_name].append(time_into_competition)
        else:
            time_of_right_answers[problem_name] = []
            time_of_right_answers[problem_name].append(time_into_competition)
        if problem_name in time_of_wrong_answers:
            time_of_wrong_answers[problem_name].append(0)
        else:
            time_of_wrong_answers[problem_name] = []
            time_of_wrong_answers[problem_name].append(0)

        number_of_solved_problems += 1
        penalties = {k: sum(d[k] for d in time_of_wrong_answers if k in d) for k in set(k for d in time_of_wrong_answers for k in d)}
        sum_of_right_answers_time = {k: sum(d[k] for d in time_of_right_answers if k in d) for k in set(k for d in time_of_right_answers for k in d)}
        total_time_measure += (penalties + sum_of_right_answers_time)

    elif problem_status == 'wrong':
        if problem_name in time_of_wrong_answers:
            time_of_wrong_answers[problem_name].append(time_into_competition)
        else:
            time_of_wrong_answers[problem_name] = []
            time_of_wrong_answers[problem_name].append(time_into_competition)

print(number_of_solved_problems, end=' ')
print(total_time_measure)
