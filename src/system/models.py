from datetime import date


class Person:
    """
    @brief A main parent class from which every other child class
        inherits. Class has attributes: first name, last name, sex,
        date of birth (separately year, month, day), age.
    """

    def __init__(self, fname, lname, sex, dateOfBirth):
        """
        @brief Class constructor. It extracts year, month and day from
            date of birth and stores as separate attribute. It also
            calculates the age of person based on the date of their birth.
        
        @param fname: The frist name of person.
        @param lname: The last name of person.
        @param sex: The sex of person (M/F).
        @param dateOfBirth: The date of birth of person (YYYY/MM/DD).
        """

        self.fname = fname
        self.lname = lname
        self.sex = sex
        
        date = dateOfBirth.split("/")
        self.yearOfBirth = int(date[0])
        self.monthOfBirth = int(date[1])
        self.dayOfBirth = int(date[2])

        self.age = self.calculate_age()


    def __str__(self):
        """
        @brief String representation of object.

        @return Returns string representation of person object.
        """

        return f"<{self.fname} {self.lname}-" \
               f"{self.yearOfBirth}/{self.monthOfBirth}/{self.dayOfBirth}>"


    def __repr__(self):
        return self.__str__()


    def calculate_age(self):
        """
        @brief Calculates an age of person based on the class attributes.

        @return Returns age of person as integer.
        """

        today = date.today()
        if today.month > self.monthOfBirth:
            return today.year - self.yearOfBirth
        
        elif today.month == self.monthOfBirth:
            if today.day >= self.dayOfBirth:
                return today.year - self.yearOfBirth
        
        return today.year - self.yearOfBirth - 1
    

    def get_date_of_birth_as_string(self):
        return f"{self.yearOfBirth}/{self.monthOfBirth}/{self.dayOfBirth}"


class Employee(Person):
    """
    @brief The Employee class for all employees in company. It inherites
        from Person class and it's extended by salary and type of
        employment.
    """
    
    def __init__(self, fname, lname, sex, dateOfBirth, salary,
                 typeOfEmployment, jobPosition):
        """
        @brief Class constructor. Inherits from Person constructor
            and it's extended by salary, type of employment and job
            position.
        """
        
        super().__init__(fname, lname, sex, dateOfBirth)

        self.salary = salary
        self.typeOfEmployment = typeOfEmployment
        self.jobPosition = jobPosition
    

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.jobPosition})"
    

    def get_list_representation(self):

        return [self.fname, self.lname, self.sex,
                self.get_date_of_birth_as_string(), self.salary,
                self.typeOfEmployment, self.jobPosition]
    

# class Chief(Employee):
#     """
#     @brief The Chief class for all people in charge like CEO, CTO,
#         marketing director, finance director, product director, etc.
#     """

#     def __init__(self, fname, lname, sex, dateOfBirth, salary,
#                  typeOfEmployment, jobPosition, abbreviation):
#         """
#         @brief Class constructor. Inherits from Chief constructor
#             and it's extended by abbreviation of job position. 
#         """
    
#         super().__init__(fname, lname, sex, dateOfBirth, salary,
#                          typeOfEmployment, jobPosition)

#         self.employees = None
#         self.abbreviation = abbreviation


# class Visitor(Person):
#     pass



