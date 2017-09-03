import numbers


class Department:

    def __init__(self, *managers):
        self.instlist = list(managers)

    def getManList(self):
        manlist = []

        for item in range(len(self.instlist)):
            manlist.extend(self.instlist[item].__dict__.items())

        mannames = [ value for key,value in manlist if key == 'second_name' ]
        print 'Managers in department: ' + ', ' .join(mannames) + '\n'

    def giveSalary(self):
        salarylist = []
        for item in range(len(Employee.employees)):
            salarylist.append([ value for key, value in Employee.employees[item].__dict__.items()
                    if key == 'second_name' or key == 'first_name' or key == 'salary' ])

        for i in range(len(salarylist)):
            print "{0} {1}: got salary: {2}" .format(salarylist[i][1],salarylist[i][2],salarylist[i][0])



class Employee():
    employees = []

    def __init__(self, first_name, second_name, salary, experience, manager):
        self.first_name = first_name
        self.second_name = second_name
        if isinstance(salary, numbers.Number):
            self.salary = salary
        else:
            raise ValueError("\"salary\" value must be a number")
        if isinstance(experience, numbers.Number):
            self.experience = experience
        else:
            raise ValueError("\experience\" value must be a number")
        self.manager = manager
        self.employees.append(self)


    def getEmployee(self):
        print "{0} {1}, manager: {2}, experience: {3}" .format(self.first_name, self.second_name, self.manager.second_name, self.experience)

    def setSalary(self):
        if self.experience > 2:
            self.salary += 200
        elif self.experience > 5:
            self.salary = self.salary * 1.2 + 500

    def getSalary(self):
        print "{0} {1}: got salary {2}".format(self.first_name, self.second_name, self.salary)


class Developer(Employee):

    def __init__(self, first_name, second_name, salary, experience, manager):
        Employee.__init__(self, first_name, second_name, salary, experience, manager)


class Designer(Employee):
    def __init__(self, first_name, second_name, salary, experience, manager, effcoeff):
        Employee.__init__(self, first_name, second_name, salary, experience, manager)

        if isinstance(effcoeff, numbers.Number):
            self.effcoeff = effcoeff
        else:
            raise ValueError("\effcoef\" value must be a number")

    def setSalary(self):
        if 0 <= (self.effcoeff) <= 1:
            self.salary += self.salary * self.effcoeff
        else:
            raise ValueError("\"effcoef\" value must be between 0 and 1 inclusive")

    def getSalary(self):
        print "{0} {1}: got salary {2}".format(self.first_name, self.second_name, self.salary)


class Manager(Employee):

    def __init__(self, first_name, second_name, salary, experience, manager=None):
        Employee.__init__(self, first_name, second_name, salary, experience, manager)
        self.team = []

    def getEmployee(self):
        print "{0} {1}, manager: {2}, experience: {3}" .format(self.first_name, self.second_name, self.manager, self.experience)

    def addTeamMember(self, *empinst):
        inst = []
        inst.extend(empinst)
        for item in range(len(inst)):
            self.team.append(inst[item].__class__.__name__)
        print self.team


    def getTeamCount(self):
        descount = 0
        devcount = 0

        for item in range(len(self.team)):
            if self.team[item] == 'Designer':
                descount += 1
            else:
                devcount += 1

        print "Member types are: Designers({0}) and Developers({1})" .format(descount,devcount)
        print "Team count is {}".format(len(self.team)) + '\n'


    def setSalary(self):
        descount = 0
        devcount = 0

        for item in range(len(self.team)):
            if self.team[item] == 'Designer':
                descount += 1
            else:
                devcount += 1

        if self.team > 5 and devcount > len(self.team)/2:
            self.salary += 200
            self.salary *= 1.1
        elif self.team > 10 and devcount > len(self.team)/2:
            self.salary += 300
            self.salary *= 1.1
        elif self.team > 5:
            self.salary += 200
        elif self.team > 10:
            self.salary += 300
        elif devcount > len(self.team)/2:
            self.salary *= 1.1



    def getSalary(self):
        print "{0} {1}: got salary {2}".format(self.first_name, self.second_name, self.salary)


peter_manager = Manager('Peter', 'Petrov', 2000, 2)
vasya_manager = Manager('Vasya', 'Vasiliev', 2000, 10)
john_developer = Developer('John', 'Smith', 3200, 2, vasya_manager)
misha_developer = Developer('Mihail', 'Mihailov', 500, 20, peter_manager)
mark_designer = Designer('Mark', 'Markov', 500, 20, peter_manager, 0.5)

peter_manager.getEmployee()
peter_manager.addTeamMember(john_developer, misha_developer,john_developer, misha_developer, mark_designer,mark_designer, mark_designer)
peter_manager.getTeamCount()
peter_manager.setSalary()

vasya_manager.getEmployee()
vasya_manager.addTeamMember(john_developer, mark_designer)
vasya_manager.getTeamCount()
vasya_manager.setSalary()

john_developer.getEmployee()
john_developer.setSalary()

misha_developer.getEmployee()
misha_developer.setSalary()

mark_designer.getEmployee()
mark_designer.setSalary()

it = Department(peter_manager, vasya_manager)
it.getManList()
it.giveSalary()

