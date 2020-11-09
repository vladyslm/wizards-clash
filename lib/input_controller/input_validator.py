
def validate(input_list, correct_answer):
    users_answer = ""
    for num in input_list:
        users_answer = users_answer + num
    try:
        users_answer = int(users_answer)
        users_answer = True if users_answer == correct_answer else False
    except ValueError:
        users_answer = False
    except:
        quit()
    return users_answer


# print(validate(["2", "3"], 23))
