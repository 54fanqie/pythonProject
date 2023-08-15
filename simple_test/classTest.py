class Stundent :
    def __init__(self, name , studeng_id):
        self.name = name
        self.student_id = studeng_id
        self.grades = {"语文" : 0,"数学":12,"英语":20}
    def set_grades(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade
    def print_grandes(self):
        print(f"学生{self.name} (学号 ： {self.student_id}) 的成绩为：")
        for cource in self.grades:
            print(f"{cource} : {self.grades[cource]} 分")
xiao = Stundent("小奶狗",110)
xiao.set_grades("语文",100)
xiao.set_grades("数学",10)
xiao.set_grades("外语",120)

xiao.print_grandes()
