from datetime import datetime
from matplotlib import pyplot as plt
import json

# project class
class Project:
    # initialize the project's attributes
    def __init__(self, title, location, status, rating, score, date, tool) -> None:
        self.title = title
        self.location = location if location else "NULL"
        self.status = status if status else "NULL"
        self.rating = rating if rating else "NULL"
        self.score = score if score else "NULL"
        self.date = date if date else "NULL"
        self.tool = tool if tool else "NULL"
        self.organizations = []
        self.company = None
        self.categories = []

    # add objects that created from class Organization, Company and Category
    def addOrganization(self, organization):
        self.organizations.append(organization)
    def setCompany(self, company):
        self.company = company
    def addCategory(self, category):
        self.categories.append(category)

    # return project's attributes
    def getTitle(self):
        return self.title
    def getLocation(self):
        return self.location
    def getStatus(self):
        return self.status
    def getRating(self):
        return self.rating
    def getScore(self):
        return self.score
    def getDate(self):
        return self.date
    def getTool(self):
        return self.tool
    # return project's attributes with concatenation form
    def getAllAttributes(self):
        attributes = [self.title, self.location, self.status, str(self.rating), str(self.score), self.date, self.tool]
        attributes_str = " - ".join(attributes) if attributes else "NULL"
        # print(str(attributes))
        return attributes_str
    # return project's attributes with output-file form that match with input-file
    def getAllAttributes_OutputFile(self):
        attributes = [
            f"title: {self.title}",
            f"location: {self.location}",
            f"status: {self.status}",
            f"rating: {self.rating}",
            f"score: {self.score}",
            f"date: {self.date}",
            f"tool: {self.tool}"
        ]
        attributes_str = ", ".join(attributes) if attributes else "NULL"
        return attributes_str
    # get objects that belong to project
    def getOrganizations(self):
        return self.organizations
    def getCompany(self):
        return self.company
    def getCategories(self):
        return self.categories
    # check whether organization, capany and category belong to project by their attributes
    def checkOrganization(self, name, role):
        for organization in self.organizations:
            if organization.getName() == name and organization.getRole() == role:
                return True
        return False
    def checkCompany(self, name):
        if self.company:
            if self.company.getName() == name:
                return True
        return False
    def checkCategory(self, name, achievement):
        for category in self.categories:
            if category.getName() == name and category.getAchievement() == achievement:
                return True
        return False

class Attribute_Element():
    def __init__(self):
        pass
    def getName(self):
        return self.name
# organization class, initializtion function, functions to get organization's attributes, 
# and function to display organization's attributes on user interface and output-file
class Organization:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role
    def getName(self):
        return self.name
    def getRole(self):
        return self.role
    def getAllAttributes(self):
        attributes = [self.name, self.role]
        attributes_str = " - ".join(attributes) if attributes else "NULL"
        return attributes_str
    def getAllAttributes_OutputFile(self):
        attributes = [f"organization_name: {self.name}", f"organization_role: {self.role}"]
        attributes_str = ", ".join(attributes) if attributes else "NULL"
        return attributes_str

# company class, initializtion function, functions to get camany's name and role, 
# and function to display company's name on output-file
class Company:
    def __init__(self, name) -> None:
        self.name = name
    def getName(self):
        return self.name
    def getName_OutputFile(self):
        return f"company_name: {self.name}"

# category class, initializtion function, functions to get category's attributes, 
# and function to display category's attributes on user interface and output-file
class Category:
    def __init__(self, name, achievement) -> None:
        self.category_name = name
        self.achievement = achievement
    def getName(self):
        return self.category_name
    def getAchievement(self):
        return self.achievement
    def getAllAtrributes(self):
        attributes = [self.category_name, self.achievement]
        attribute_str = " - ".join(attributes) if attributes else "NULL"
        return attribute_str
    def getAllAttributes_OutputFile(self):
        attributes = [f"category_name: {self.category_name}", f"category_achievement: {self.achievement}"]
        attribute_str = ", ".join(attributes) if attributes else "NULL"
        return attribute_str

# Observer Patter (Python design pattern class)
class Observer:
    def update(self, project):
        pass
class Project_Logger(Observer):
    def update(self, project):
        print(f"New project created: {project.getAllAttributes()}")
class Project_Statistics(Observer):
    def __init__(self):
        self.project_count = 0
    def update(self, project):
        self.project_count += 1
        print(f"Total projects: {self.project_count}")

# class Data_Diagram_Analysis():
#     def __init__(self):
#         pass
#     def drawing(self, data):
#         pass

class BaseException(Exception):
    """Base exception class for project exceptions"""
    pass
class Date_Error_InputType(BaseException):
    """Exception raised for date inputs."""
    def __init__(self, value):
        super().__init__(f"Date value input: {value}")

# system that manage all function of the program
class SystemController:
    def __init__(self):
        self.projects = []
        self.organizations = []
        self.companies = []
        self.categories = []
        self.observers = []

    # create a project form project class
    def createProject(self, title, location, status, rating, score, date, tool):
        newProject = Project(title, location, status, rating, score, date, tool)
        self.projects.append(newProject)
        self.notify_observer(newProject)
        return newProject
    # function to add observer class
    def add_observer(self, observer):
        self.observers.append(observer)
    def remove_observer(self, observer):
        self.observers.remove(observer)
    # notify the the project details and total projects when each project is created and add to system (in import file or when users enter by themselves)
    def notify_observer(self, project):
        for observer in self.observers:
            observer.update(project)

    # create a organization and add it to project
    def addOrganization(self, name, role):
        newOrganization = self.checkOrganization(name, role)
        if newOrganization:
            return newOrganization
        newOrganization = Organization(name, role)
        self.organizations.append(newOrganization)
        return newOrganization
    # create a company and add it to project
    def addCompany(self, name):
        newCompany = self.checkCompany(name)
        if newCompany:
            return newCompany
        newCompany = Company(name)
        self.companies.append(newCompany)
        return newCompany
    # create a category and add it to project
    def addCategory(self, name, achievement):
        newCategory = self.checkCategory(name, achievement)
        if newCategory:
            return newCategory
        newCategory = Category(name, achievement)
        self.categories.append(newCategory)
        return newCategory
    # check project's title wheather it already exists or not
    def checkProjectTitle(self, title):
        if title.strip() == "":
            return False
        for project in self.projects:
            if project.getTitle() == title:
                return False
        return True
    # check organization wheather it belongs to a project we want to check or not
    def checkOrganization(self, name, role):
        for organization in self.organizations:
            if organization.getName() == name and organization.getRole() == role:
                return organization
        return None
    # check company wheather it belongs to a project we want to check or not
    def checkCompany(self, name):
        for company in self.companies:
            if company.getName() == name:
                return company
        return None
    # check category wheather it belongs to a project we want to check or not
    def checkCategory(self, name, achievement):
        for category in self.categories:
            if category.getName() == name and category.getAchievement() ==  achievement:
                return category
        return
    def checkInsertStatus(self, status):
        if status != "Prepare" and status != "Process" and status != "Done":
            return False
        return True
    def checkInsertRating(self, rating):
        if not rating.isdigit():
            raise Exception("Project's rating is not a number!")
        rating = float(rating)
        if rating < 0 and rating > 10:
            return False
        return True
    def checkInsertScore(self, score):
        if not score.isdigit():
            raise Exception("Project's score is not a number!")
        score = float(score)
        if score < 0 and score > 100:
            return False
        return True
    def checkInsertDate(self, date):
        try:
            date = datetime.strptime(date, '%d/%m/%Y')
            if 2000 <= date.year <= 2024:
                return True
            else:
                return False
        except ValueError:
            return False
    def Time_Project_Line(self):
        year_dict = {year: 0 for year in range(2000, 2024 + 1)}
        for project in self.projects:
            proj_year = datetime.strptime(project.getDate(), '%d/%m/%Y').year
            year_dict[proj_year] += 1
        year = year_dict.keys()
        project_amount = year_dict.values()
        fig, ax = plt.subplots()
        ax = plt.plot(year, project_amount)
        ax = plt.xlabel("Year")
        ax = plt.ylabel("Number of Projects")
        plt.tight_layout()
        plt.savefig("Time_Project_LineChart.png")
        plt.show()
    def Location_Project_Pie(self):
        location_dict = {}
        for project in self.projects:
            project_location = project.getLocation()
            if project_location not in location_dict:
                location_dict[project_location] = 1
            else:
                location_dict[project_location] += 1
        locations = location_dict.keys()
        project_amount = location_dict.values()
        fig, ax = plt.subplots()
        ax = plt.pie(project_amount, labels = None, startangle=90, counterclock=False)
        # Calculate the percentage of the project amount per location
        total = sum(project_amount)
        percentages = [f'{location}: {count / total * 100:.1f}%' for location, count in zip(locations, project_amount)]
        ax = plt.legend(percentages, loc='upper right', bbox_to_anchor=(1.3, 1), prop={'size': 8})
        ax = plt.title("Location of projects")
        plt.tight_layout()
        plt.savefig("Location_Project_PieChart.png")
        plt.show()
    def Rating_Project_Pie(self):
        rating_dict = {"0-3": 0, "3-6": 0, "6-8": 0, "8-10": 0}
        for project in self.projects:
            project_rating = float(project.getRating())
            if project_rating <= 3:
                rating_dict["0-3"] += 1
            elif project_rating <= 6:
                rating_dict["3-6"] += 1
            elif project_rating <= 8:
                rating_dict["6-8"] += 1
            else:
                rating_dict["8-10"] += 1
        filtered_rating_dict = {key: value for key, value in rating_dict.items() if value > 0}
        ratings = filtered_rating_dict.keys()
        rating_group = filtered_rating_dict.values()
        plt.pie(rating_group, labels=None, startangle=90, counterclock=False)
        circle = plt.Circle((0, 0), 0.5, fc='white')
        plt.gcf().gca().add_artist(circle)
        total = sum(rating_group)
        percentages = [f'{rating}: {count/total*100:.1f}%' for rating, count in zip(ratings, rating_group)]
        plt.legend(percentages, loc='upper right', bbox_to_anchor=(1.3, 1), prop={'size': 8})
        plt.title("Rating group of projects")
        plt.tight_layout()
        plt.savefig("Rating_Project_PieChart.png")
        plt.show()
        
    def Score_Project_Pie(self):
        score_dict = {"0-20": 0, "21-40": 0, "41-60": 0, "61-80": 0, "81-100": 0}
        for project in self.projects:
            project_score = float(project.getScore())
            if project_score <= 20:
                score_dict["0-20"] += 1
            elif project_score <= 40:
                score_dict["21-40"] += 1
            elif project_score <= 60:
                score_dict["41-60"] += 1
            elif project_score <= 80:
                score_dict["61-80"] += 1
            else:
                score_dict["81-100"] += 1
        filtered_score_dict = {key: value for key, value in score_dict.items() if value > 0}
        scores = filtered_score_dict.keys()
        score_group = filtered_score_dict.values()
        plt.pie(score_group, labels=None, startangle=90, counterclock=False)
        total = sum(score_group)
        percentages = [f'{score}: {count/total*100:1f}%' for score, count in zip(scores, score_group)]
        plt.legend(percentages, loc='upper right', prop={'size': 8})
        plt.title("Score group of projects")
        plt.tight_layout()
        plt.savefig("Score_Project_PieChart.png")
        plt.show()
    def Status_Project_Pie(self):
        status_dict = {"Prepare": 0, "Process": 0, "Done": 0}
        for project in self.projects:
            project_status = project.getStatus()
            if project_status == "Prepare":
                status_dict["Prepare"] += 1
            elif project_status == "Process":
                status_dict["Process"] += 1
            elif project_status == "Done":
                status_dict["Done"] += 1
        status_list = status_dict.keys()
        status_amount = status_dict.values()
        print(status_amount)
        myexplode = [0, 0, 0.2]
        plt.pie(status_amount, labels=status_list, explode=myexplode, startangle=90, counterclock=False)
        total = sum(status_amount)
        percentages = [f'{status}: {count/total*100:1f}%' for status, count in zip(status_list, status_amount)]
        plt.legend(percentages, loc='upper right', prop={'size': 8})
        plt.title("Status of projects")
        plt.tight_layout()
        plt.savefig("Status_Project_PieChart.png")
        plt.show()
    def Company_Project_Barh(self):
        com_dict = {}
        for project in self.projects:
            project_com = project.getCompany().getName()
            if project_com not in com_dict:
                com_dict[project_com] = 1
            else:
                com_dict[project_com] += 1
        companies = list(com_dict.keys())
        project_amount = list(com_dict.values())
        fig, ax = plt.subplots()
        ax = plt.barh(companies, project_amount)
        ax = plt.title("Project amounts of company")
        ax = plt.xlabel('Project amount')
        ax = plt.ylabel('Company')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.savefig("Campany_Project_BarhChart.png")
        plt.show()
    def Organization_Project_Bar(self):
        organization_dict = {}
        for project in self.projects:
            organization_list = project.getOrganizations()
            for organization in organization_list:
                organization_name = organization.getName()
                if organization_name not in organization_dict:
                    organization_dict[organization_name] = 1
                else:
                    organization_dict[organization_name] += 1
        organizations = list(organization_dict.keys())
        project_amount = list(organization_dict.values())
        fig, ax = plt.subplots()
        ax = plt.bar(organizations, project_amount)
        ax = plt.title("Project amounts of organization")
        ax = plt.xlabel('Project amount')
        ax = plt.ylabel('Organization')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("Organization_Project_BarChart.png")
        plt.show()
    def Organization_Location_Line(self):
        location_dict = {}
        for project in self.projects:
            location = project.getLocation()
            organization_list = project.getOrganizations()
            if location not in location_dict:
                location_dict[location] = []
            for organization in organization_list:
                if organization not in location_dict[location]:
                    location_dict[location].append(organization.getName())
        
        location_dict = {key : len(value) for key, value in location_dict.items()}
        locations = location_dict.keys()
        organization_amount = location_dict.values()
        fig, ax = plt.subplots()
        ax = plt.plot(locations, organization_amount, '--', color="red", linewidth=2, marker="o")
        ax = plt.xlabel("Year")
        ax = plt.ylabel("Number of organization")
        plt.tight_layout()
        plt.savefig("Location_Organization_LineChart.png")
        plt.show()
    def Category_Location_Line(self):
        location_dict = {}
        for project in self.projects:
            location = project.getLocation()
            category_list = project.getCategories()
            if location not in location_dict:
                location_dict[location] = []
            for category in category_list:
                if category not in location_dict[location]:
                    location_dict[location].append(category.getName())
        
        location_dict = {key : len(value) for key, value in location_dict.items()}
        locations = location_dict.keys()
        category_amount = location_dict.values()
        fig, ax = plt.subplots()
        ax = plt.plot(locations, category_amount, '-.', color="green", linewidth=5)
        ax = plt.xlabel("Location")
        ax = plt.ylabel("Number of category")
        plt.tight_layout()
        plt.savefig("Location_Category_LineChart.png")
        plt.show()
    # when using searching function all projects, all organizations, all companies and all categories that relates the information user want to search by will be concatenated together to a dictionay variable
    # search all relevant information by project's title
    def searchByTitle(self, title):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        for project in self.projects:
            if project.getTitle() == title:
                result["projects"].append(project)
        for project in result["projects"]:
            result["organizations"] += project.getOrganizations()
            if project.getCompany() != None:
                result["companies"].append(project.getCompany())
            result["categories"] +=  project.getCategories()
        return result
    # this search function like the above but it has concatenation to return a string to display on output-file
    def searchByTitle_OutputFile(self, title):
        result_dict = {
            "project" : None,
            "company" : None}
        result_list = []
        for project in self.projects:
            if project.getTitle() == title:
                result_dict["project"] = project
                break
        if result_dict["project"]:
            result_list.append(result_dict["project"].getAllAttributes_OutputFile()) 
            for organization in project.getOrganizations():
                result_list.append(organization.getAllAttributes_OutputFile())
            result_dict["company"] = project.getCompany()
            if result_dict["company"]:
                result_list.append(result_dict["company"].getName_OutputFile())
            for category in project.getCategories():
                result_list.append(category.getAllAttributes_OutputFile())
            output = ", ".join(result_list)
        else:
            output = "The project's title you want to find is not exist"
        return output
    
    # search all relevant information by location
    def searchByLocation(self, location):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        for project in self.projects:
            if project.getLocation() == location:
                result["projects"].append(project)
        for project in result["projects"]:
            for organizaion in project.getOrganizations():
                if organizaion not in result["organizations"]:
                    result["organizations"].append(organizaion)
            company = project.getCompany()
            if company not in result["companies"]:
                result["companies"].append(company)
            for category in project.getCategories():
                if category not in result["categories"]:
                    result["categories"].append(category)
        return result
    # this search function like the above but it has concatenation to return a string to display on output-file    
    def searchByLocation_OutputFile(self, location):
        result_dict = {
            "projects" : [],
            "company" : None}
        result_list = []
        project_str_list = []
        for project in self.projects:
            if project.getLocation() == location:
                result_dict["projects"].append(project)
        if result_dict["projects"]:
            for project in result_dict["projects"]:
                result_list.append(project.getAllAttributes_OutputFile())
                for organization in project.getOrganizations():
                    result_list.append(organization.getAllAttributes_OutputFile())
                result_dict["company"] = project.getCompany()
                if result_dict["company"]:
                    result_list.append(result_dict["company"].getName_OutputFile())
                for category in project.getCategories():
                    result_list.append(category.getAllAttributes_OutputFile())
                project_str = ", ".join(result_list)
                result_list.clear()
                project_str_list.append(project_str)
            output = "\n".join(project_str_list) if project_str_list else "NULL"
        else:
            output = "The location you want to find is not exist"
        return output
    
    # search all relevant information by organization
    def searchByOrganization(self, name, role):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        search_organization = None
        for organization in self.organizations:
            if organization.getName() == name and organization.getRole() == role:
                search_organization = organization
                break
        if search_organization:
            result["organizations"].append(search_organization)
            for project in self.projects:
                if project.checkOrganization(name, role):
                    result["projects"].append(project)
                    company = project.getCompany()
                    if company not in result["companies"]:
                        result["companies"].append(company)
                    for category in project.getCategories():
                        if category not in result["categories"]:
                            result["categories"].append(category)
        return result
    # this search function like the above but it has concatenation to return a string to display on output-file    
    def searchByOrganization_OutputFile(self, name, role):
        result_dict = {
            "projects" : [],
            "company" : None}
        result_list = []
        project_str_list = []
        # result["organizations"].append(search_organization)
        for project in self.projects:
            if project.checkOrganization(name, role):
                result_dict["projects"].append(project)
        if result_dict["projects"]:
            for project in result_dict["projects"]:
                result_list.append(project.getAllAttributes_OutputFile())
                for organization in project.getOrganizations():
                    result_list.append(organization.getAllAttributes_OutputFile())
                result_dict["company"] = project.getCompany()
                if result_dict["company"]:
                    result_list.append(result_dict["company"].getName_OutputFile())
                for category in project.getCategories():
                    result_list.append(category.getAllAttributes_OutputFile())
                project_tr = ", ".join(result_list) if result_list else "NULL"
                result_list.clear()
                project_str_list.append(project_tr)
            output = "\n".join(project_str_list) if project_str_list else "NULL"
        else:
            output = "The organization you want to find is not exist"
        return output
    
    # search all relevant information by company
    def searchByCompany(self, name):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        search_company = None
        for company in self.companies:
            if company.getName() == name:
                search_company = company
                break
        if search_company:
            result["companies"].append(search_company)
            for project in self.projects:
                if project.checkCompany(name):
                    result["projects"].append(project)
                    for organization in project.getOrganizations():
                        if organization not in result["organizations"]:
                            result["organizations"].append(organization)
                    for category in project.getCategories():
                        if category not in result["categories"]:
                            result["categories"].append(category)
        return result
     # this search function like the above but it has concatenation to return a string to display on output-file   
    def searchByCompany_OutputFile(self, name):
        result_dict = {
            "projects" : [],
            "company" : None}
        result_list = []
        project_str_list = []
        for project in self.projects:
            if project.checkCompany(name):
                if project.getCompany().getName() == name:
                    result_dict["projects"].append(project) 
        if result_dict["projects"]:
            for project in result_dict["projects"]:
                result_list.append(project.getAllAttributes_OutputFile())
                for organization in project.getOrganizations():
                    result_list.append(organization.getAllAttributes_OutputFile())
                result_dict["company"] = project.getCompany()
                if result_dict["company"]:
                    result_list.append(result_dict["company"].getName_OutputFile())
                for category in project.getCategories():
                    result_list.append(category.getAllAttributes_OutputFile())
                project_str = ", ".join(result_list)
                result_list.clear()
                project_str_list.append(project_str)
            output = "\n".join(project_str_list) if project_str_list else "NULL"
        else:
            output = "The company you want to find is not exist"
        return output
    
    # search all relevant information by category
    def searchByCategory(self, name, achievement):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        search_category = None
        for category in self.categories:
            if category.getName() == name and category.getAchievement() == achievement:
                search_category = category
                break
        if search_category:
            result["categories"].append(search_category)
            for project in self.projects:
                if project.checkCategory(name, achievement):
                    result["projects"].append(project)
                    for organization in project.getOrganizations():
                        if organization not in result["organizations"]:
                            result["organizations"].append(organization)
                    company = project.getCompany()
                    if company not in result["companies"]:
                        result["companies"].append(company)
        return result
    # this search function like the above but it has concatenation to return a string to display on output-file    
    def searchByCategory_OutputFile(self, name, achievement):
        result_dict = {
            "projects" : [],
            "company" : None}
        result_list = []
        project_str_list = []
        # result["organizations"].append(search_organization)
        for project in self.projects:
            if project.checkCategory(name, achievement):
                result_dict["projects"].append(project)
        if result_dict["projects"]:
            for project in result_dict["projects"]:
                result_list.append(project.getAllAttributes_OutputFile())
                for organization in project.getOrganizations():
                    result_list.append(organization.getAllAttributes_OutputFile())
                result_dict["company"] = project.getCompany()
                if result_dict["company"]:
                    result_list.append(result_dict["company"].getName_OutputFile())
                for category in project.getCategories():
                    result_list.append(category.getAllAttributes_OutputFile())
                project_tr = ", ".join(result_list) if result_list else "NULL"
                result_list.clear()
                project_str_list.append(project_tr)
            output = "\n".join(project_str_list) if project_str_list else "NULL"
        else:
            output = "The company you want to find is not exist"
        return output
    # print all projects, organizations, conpanies and categories in system
    def displayAll(self):
        self.displayAllProjects()
        self.displayAllOrganizations()
        self.displayAllCompanies()
        self.displayAllCategories()

    # print all elements of all projects in system
    def displayAllProjects(self):
        print("PROJECT: ")
        if self.projects:
            for project in self.projects:
                print(project.getAllAttributes())
        else:
            print("No exist project.")
    # print all organization names and roles in the system
    def displayAllOrganizations(self):
        print("ORGANIZATION: ")
        if self.organizations:
            for organization in self.organizations:
                organization_elements = [organization.getName(), organization.getRole()]
                organization_str = " - ".join(organization_elements) if organization_elements else "No exist organization."
                print(organization_str)
        else:
            print("No exist organization.")
    # print all company names in the system
    def displayAllCompanies(self):
        print("COMPANY: ")
        if self.companies:
            for company in self.companies:
                print(company.getName())
        else:
            print("No exist company.")
    # print all category names and achievements in the system
    def displayAllCategories(self):
        print("CATEGORY:")
        if self.categories:
            for category in self.categories:
                print(category.getAllAtrributes())
        else:
            print("No exist category.")
    # print the result - the dictionary that gain from search function
    def printSearchResult(self, result):
        for i in result:
            if i == "projects":
                print("PROJECT:")
                if result[i]:
                    for project in result[i]:
                        print(project.getAllAttributes())
                else:
                    print("No exist project.")
            elif i == "organizations":
                print("ORGANIZATION:")
                if result[i]:
                    for organization in result[i]:
                        print(organization.getAllAttributes())
                else:
                    print("No exist organization.")
            elif i == "companies":
                print("COMPANY:")
                if result[i]:
                    for company in result[i]:
                        print(company.getName())
                else:
                    print("No exist company.")
            elif i == "categories":
                print("CATEGORY:")
                if result[i]:
                    for category in result[i]:
                        print(category.getAllAtrributes())
                else:
                    print("No exist category.")        
    
    # get the user's requirement functions
    def userInput(self):
        print("I - Insert new project | S - Search by Project, Location, Organization, Company, or Category | D - Display Projects, Organizations, Companies, and Categories | X - Quit the program", sep = "\n")
        print(  "1 to 9 - Making statistic diagram","1 Time (year) with amount of projects (Line chart)", "2 - Location with number of projects (Pie chart)", "3 - Rating of projects (Pie chart)", "4 - Score of projects (Pie chart)", "5 - Status of projects (Pie chart)", "6 - Project amount of company (Barh chart)", "7 - Project amount of organization (Bar chart)", "8 - Organization amount of location (Barh chart)", "9 - Category amount of location (Bar chart)", sep = "\n")
        user_input = input("Please enter the service you want: ").upper()
        return user_input
    def systemOperating(self, user):
        if user == 'I':
            print("Now you can insert a new project.")
            title = input("Please enter the new project title: ")
            while not self.checkProjectTitle( title):
                print("Your project title is already exist or project tile is not valid.")
                title = input("Please enter the new project title: ")
            location = input("Please enter the new project location: ")

            status = input("Please enter the new project status (Prepare - Process - Done): ")
            while not self.checkInsertStatus(status):
                print("Your project status is unappropriate !")
                status = input("Please enter again the new project status (Prepare - Process - Done): ")

            rating = input("Please enter the new project rating number (0-10): ")
            while not self.checkInsertRating(int(rating)):
                print("Your project raitng is out of range !")
                rating = input("Please enter the new project rating number (0-10): ")
                
            score = input("Please enter the new project score (0-100): ")
            while not self.checkInsertScore(int(score)):
                print("Your project raitng is out of range !")
                score = input("Please enter the new project score (0-100): ")
                
            date = input("Please enter the certified date (dd/mm/yyyy): ")
            while not self.checkInsertDate(date):
                print("Your project date is unappropriate !")
                date = input("Please enter the certified date (dd/mm/yyyy): ")           

            tool = input("Please enter the rating tool: ")
            newproject = self.createProject(title, location, status, rating, score, date, tool)

            company_name = input("What is the main company of this project?: ")
            if company_name != "":
                newCompany = self.addCompany(company_name)
            else:
                newCompany = None
            newproject.setCompany(newCompany)
            user_organization = input("Do you want to add new ORGANIZATION to this project? (Y - yes, N - no): ")
            while user_organization != 'N' and user_organization != 'n':
                if user_organization == 'Y' or user_organization == 'y':
                    organization_name = input("Please enter the ORGANIZATION name: ")
                    organization_role = input("Please enter the ORGANIZATION role: ")
                    newOrganization = self.addOrganization(organization_name, organization_role)
                    newproject.addOrganization(newOrganization)
                else:
                    print("System does not understand your command. Please enter again.")
                user_organization = input("Do you want to add new ORGANIZATION to this project? (Y - yes, N - no): ")
            user_category = input("Do you want to add new CATEGORY to this project? (Y - yes, N - no): ")
            while user_category != 'N' and user_category != 'n':
                if user_category == 'Y' or user_category == 'y':
                    category_name = input("Please enter the CATEGORY name: ")
                    achievement = input("Please enter the CATEGORY achievement: ")
                    newCategory = self.addCategory(category_name, achievement)
                    newproject.addCategory(newCategory)
                else:
                    print("System does not understand your command. Please enter again.")
                user_category = input("Do you want to add new CATEGORY to this project? (Y - yes, N - no): ")

        elif user == 'S':
            print(  "1 - Search by project title", "2 - Search by location", "3 - Search by organization", 
                    "4 - Search by company", "5 - Search by category", 
                    "X - Exit the search function", sep = "\n")
            search_option = input("Please select the search option that you want: ")
            while search_option != 'X' and search_option != 'x':
                if search_option == '1':
                    search_title = input("Project title: ")
                    result = self.searchByTitle(search_title)
                    self.printSearchResult(result)
                    output_str = self.searchByTitle_OutputFile(search_title)
                elif search_option == '2':
                    search_location = input("Location: ")
                    result = self.searchByLocation(search_location)
                    self.printSearchResult(result)
                    output_str = self.searchByLocation_OutputFile(search_location)
                elif search_option == '3':
                    print("Please enter the name and role of the organization for searching")
                    organ_name = input("Organization name: ")
                    organ_role = input("Organization role: ")
                    result = self.searchByOrganization(organ_name, organ_role)
                    self.printSearchResult(result)
                    output_str = self.searchByOrganization_OutputFile(organ_name, organ_role)
                elif search_option == '4':
                    company_name = input("Company name: ")
                    result = self.searchByCompany(company_name)
                    self.printSearchResult(result)
                    output_str = self.searchByCompany_OutputFile(company_name)
                elif search_option == '5':
                    category_name = input("Category name: ")
                    category_achievement = input("Category achievement: ")                
                    result = self.searchByCategory(category_name, category_achievement)
                    self.printSearchResult(result)
                    output_str = self.searchByCategory_OutputFile(category_name, category_achievement)
                else:
                    output_str = "System does not understand your command. Please enter again."
                    print("System does not understand your command. Please enter again.")
                # write the output to result file 
                self.exportOutputFile('output.txt', output_str)
                print("1 - Search by project title", "2 - Search by location", "3 - Search by organization", "4 - Search by company", "5 - Search by category", "X - Exit the search function", sep = "\n")
                search_option = input("Please select the search option that you want: ")
        elif user == "D":
            print("1 - Display all projects, organizations, comapanies, and categories", "2 - Display all projects", "3 - Display all organizations", "4 - Display all companies", "5 - Display all categories", sep="\n")
            if user == "1":
                self.displayAll()
            elif user == "2":
                self.displayAllProjects()
            elif user == "3":
                self.displayAllOrganizations()
            elif user == "4":
                self.displayAllCompanies()
            elif user == '5':
                self.displayAllCategories()
        elif user == '1':
            self.Time_Project_Line()
        elif user == '2':
            self.Location_Project_Pie()
        elif user == '3':
            self.Rating_Project_Pie()
        elif user == '4':
            self.Score_Project_Pie()
        elif user == '5':
            self.Status_Project_Pie()
        elif user == '6':
            self.Company_Project_Barh()
        elif user == '7':
            self.Organization_Project_Bar()
        elif user == '8':
            self.Organization_Location_Line()
        elif user == '9':
            self.Category_Location_Line()
        else:
            print("System does not understand your command. Please enter again.")
        print("- - - - - - - - - -")         

    # import input file to the program (the input file includes information about the project, organization, company, and category)
    # check the error when importing input file - title cannot be same as exist one, title cannot be empty
    # the checking error will notify that which row of input-file has the error 
    def importInputFile(self, input_file):
        with open(input_file) as file:
            datas = json.load(file)
            for data in datas:
                title = data['title']
                location = data['location']
                status = data['status']
                rating = data['rating']
                score = data['score']
                date = data['date']
                tool = data['tool']
                project = self.createProject(title, location, status, rating, score, date, tool)
                company = self.addCompany(data['company_name'])
                project.setCompany(company)
                for organ in data['organizations']:
                    organization = self.addOrganization(organ['organization_name'], organ['organization_role'])
                    project.addOrganization(organization)
                for cate in data['categories']:
                    category = self.addCategory(cate['category_name'], cate['category_achievement'])
                    project.addCategory(category)
                

    # this function is used to write the result (with string type) that gain from searching functions to an output-file
    def exportOutputFile(self, output_file, output_str):
        try:
            if output_str:
                with open(output_file, 'w') as file:
                    file.write(output_str)
            else:
                file.write("Program can not search for related projects, organizations, companies, and categories.")
        except Exception as e:
            print(f"An error accurred: {e}")

    # split the line to get the project attributes
    def getProjectValues(self, attributes):
        result = {"title" : "", 
                  "location" : "", 
                  "status": "", 
                  "rating": "", 
                  "score": "", 
                  "date": "", 
                  "tool": ""}
        i = 0
        for attribute in attributes:
            try:
                if "title" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    result["title"] = value
                elif "location" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()                
                    result["location"] = value
                elif "status" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    result["status"] = value
                elif "rating" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    result["rating"] = value
                elif "score" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    result["score"] = value
                elif "date" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    result["date"] = value
                elif "tool" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    result["tool"] = value
            except Exception as e:
                print(f"An error accurred: {e}")
        return result
    # get organization name and role in a line of input file
    def getOrganizationValues(self, attributes):
        result = []
        for i in range (len(attributes)):
            if "organization_name" in attributes[i]:
                colon_position = attributes[i].find(':')
                if colon_position == -1:
                    value1 = ""
                else:
                    value1 = attributes[i][colon_position + 1:].strip()
                # find the role of organization when we can collect the organization's name already
                if attributes[i+1]:
                    colon_position = attributes[i+1].find(':')
                    if colon_position == -1:
                        value2 = ""
                    else:
                        value2 = attributes[i+1][colon_position + 1:].strip()
                result.append((value1, value2))
        return result
    # get company name in a line of input file
    def getCompanyValues(self, attributes):
        result = []
        for attribute in attributes:
            if "company_name" in attribute:
                colon_position = attribute.find(':')
                if colon_position == -1:
                    value = ""
                else:
                    value = attribute[colon_position + 1:].strip()
                result.append(value)
        return result
    #get category name and achievement in a line of input file
    def getCategoryValues(self, attributes):
        result = []
        for i in range (len(attributes)):
            if "category_name" in attributes[i]:
                colon_position = attributes[i].find(':')
                if colon_position == -1:
                    value1 = ""
                else:
                    value1 = attributes[i][colon_position + 1:]
                # find the role of organization when we can collect the organization nam already
                i += 1
                if attributes[i]:
                    colon_position = attributes[i].find(':')
                    if colon_position == -1:
                        value2 = ""
                    else:
                        value2 = attributes[i][colon_position + 1:]
                result.append((value1.strip(), value2.strip()))       
        return result
    # def systemOperating(self):
    #     self.userServiceRequirement()

def main():
    system = SystemController()
    logger = Project_Logger()
    statistics = Project_Statistics()
    system.add_observer(logger)
    system.add_observer(statistics)

    system.importInputFile('input.json')
    user = system.userInput()
    while user != 'X' and user != 'x':
        system.systemOperating(user)
        user = system.userInput()

if __name__ == '__main__':
    main()