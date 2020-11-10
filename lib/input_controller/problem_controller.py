from lib.input_controller.equation_generator import generate_equation


class ProblemController:
    def __init__(self):
        self.problem = {
            "problem": None,
            "answer": None
        }
        self.input_controllers = []

    def add_input_controllers(self, input_c1, input_c2):
        self.input_controllers.append(input_c1)
        self.input_controllers.append(input_c2)

    def notify_input_controllers(self):
        for input_controller in self.input_controllers:
            input_controller.clean_input()
            if not input_controller.is_player:
                input_controller.set_countdown()

    def set_problem(self):
        self.notify_input_controllers()
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
        self.notify_input_controllers()
