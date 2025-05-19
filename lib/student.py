from lib.user import User

class Student(User):
    def __init__(self, first_name="First", last_name="Last"):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, info):
        self.knowledge.append(info)

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")


class ChattyStudent(Student):
    def hello(self):
        print("Hey there! I'm so excited to learn stuff. Did you watch that show last night? So sad about who died...")

    def raise_hand(self):
        for _ in range(10):
            print("Pick me!")
