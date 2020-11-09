from lib.input_controller.equation_generator import generate_equation


class ProblemController:
    def __init__(self):
        self.problem = {
            "problem": None,
            "answer": None
        }

    def set_problem(self):
        problem, answer = generate_equation()
        self.problem["problem"] = problem
        self.problem["answer"] = answer

    def get_problem(self):
        return self.problem["problem"]

    def get_answer(self):
        print(self.problem["answer"])
        return self.problem["answer"]

    def clean_problem(self):
        self.problem["problem"] = None
        self.problem["answer"] = None
