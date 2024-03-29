class Project:
    def __init__(self, title, location, status, rating, score, date, tool) -> None:
        self.title = title
        self.location = location if location else "NULL"
        self.status = status
        self.rating = rating
        self.score = score
        self.date = date
        self.tool = tool
        self.organizations = []
        self.company = None
        self.categories = []

    def addOrganization(self, organization):
        self.organizations.append(organization)
    def setCompany(self, company):
        self.company = company
    def addCategory(self, category):
        self.categories.append(category)

    def getTitle(self):
        return self.title
    def getLocation(self):
        return self.location
    def getStatus(self):
        return self.rating
    def getRating(self):
        return self.rating
    def getScore(self):
        return self.score
    def getDate(self):
        return self.date
    def getTool(self):
        return self.tool
    def getAllAttributes(self):
        attributes = [self.title, self.location, self.status, self.score, self.date, self.tool]
        attributes_str = " - ".join(attributes) if attributes else "The project does not exist !!!"
        return attributes_str
    def getOrganizations(self):
        return self.organizations
    def getCompany(self):
        return self.company
    def getCategories(self):
        return self.categories
    def checkOrganization(self, name, role):
        for organization in self.organizations:
            if organization.getName() == name and organization.getRole() == role:
                return True
    
class Organization:
    def __init__(self, name, role, title, location) -> None:
        self.name = name
        self.role = role
        self.project_title = title
        self.location = location
    def getName(self):
        return self.name
    def getRole(self):
        return self.role
    def getProjectTitle(self):
        return self.project_title
    def getLocation(self):
        return self.location
    def getAllAttributes(self):
        attributes = [self.name, self.role]
        attributes_str = " - ".join(attributes) if attributes else "NULL"
        return attributes_str
    
class Company:
    def __init__(self, name, title, location) -> None:
        self.name = name
        self.project_title = title
        self.location = location
    def getName(self):
        return self.name
    def getProjectTitle(self):
        return self.project_title
    def getLocation(self):
        return self.location

class Category:
    def __init__(self, name, acheivement, title, location) -> None:
        self.category_name = name
        self.acheivement = acheivement
        self.project_title = title
        self.location = location
    def getName(self):
        return self.category_name
    def getAcheivement(self):
        return self.acheivement
    def getProjectTitle(self):
        return self.project_title
    def getLocation(self):
        return self.location
    def getAllAtrributes(self):
        attributes = [self.category_name, self.acheivement]
        attribute_str = " - ".join(attributes) if attributes else "NULL"
        return attribute_str

class SystemController:
    def __init__(self) -> None:
        self.projects = []
        self.organizations = []
        self.companies = []
        self.categories = []
    def createProject(self, title, location, status, rating, score, date, tool):
        newProject = Project(title, location, status, rating, score, date, tool)
        self.projects.append(newProject)
        return newProject
    def addOrganization(self, name, role, title, location):
        newOrganization = Organization(name, role, title, location)
        self.organizations.append(newOrganization)
        return newOrganization
    def addCompany(self, name, title, location):
        newCompany = Company(name, title, location)
        self.companies.append(newCompany)
        return newCompany
    def addCategory(self, name, acheivement, title, location):
        newCategory = Category(name, acheivement, title, location)
        self.categories.append(newCategory)
        return newCategory
    def checkProjectTitle(self, title):
        if title == None:
            return False
        for project in self.projects:
            if project.getTitle() == title:
                return False
        return True
    def searchByTitle(self, title):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        for project in self.projects:
            if project.getTitle() == title:
                result["projects"].append(project)
        for organization in self.organizations:
            if organization.getProjectTitle() == title:
                result["organizations"].append(organization)
        for company in self.companies:
            if company.getProjectTitle() == title:
                result["companies"].append(company)
        for category in self.categories:
            if category.getProjectTitle() == title:
                result["categories"].append(category)
        self.printSearchResult(result)
    def searchByLocation(self, location):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        for project in self.projects:
            if project.getLocation() == location:
                result["projects"].append(project)
        for organization in self.organizations:
            if organization.getLocation() == location:
                result["organizations"].append(organization)
        for company in self.companies:
            if company.getLocation() == location:
                result["companies"].append(company)
        for category in self.categories:
            if category.getLocation() == location:
                result["categories"].append(category)
        self.printSearchResult(result)
    def searchByOrganization(self, name, role):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        search_organization = None
        for organization in self.organizations:
            if organization.getName() == name and organization.getRole():
                search_organization = organization
                break
        if search_organization:
            for project in self.projects:
                if project.checkOrganization(name, role):
                    result["projects"].append(project)
                    result["companies"].append(project.getCompany())
                    result["categories"] += project.getCategories()
            result["organizations"].append(search_organization)
        self.printSearchResult(result)
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
            for project in self.projects:
                if project.getCompany().getName() == name:
                    result["projects"].append(project)
                    result["organizations"] += project.getOrganizations()
                    result["categories"] += project.getCategories()
        self.printSearchResult(result)
    def searchByCategory(self, category):
        pass
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        search_category = None
        for category in self.categories:
            if category.getName() == name:
                search_category = category
                break
    def displayAll(self):
        self.displayAllProjects()
        self.displayAllOrganizations()
        self.displayAllCompanies()
        self.displayAllCategories()
    def displayAllProjects(self):
        print("Project: ")
        if self.projects:
            # print("Project Title - Location - Status - Green Star Rating - Final Score - Date Certified - Rating Tool")
            for project in self.projects:
                print(project.getAllAttributes())
        else:
            print("No exist project.")
    def displayAllOrganizations(self):
        print("Organization: ")
        if self.organizations:
            # print("Name - Role")
            for organization in self.organizations:
                organization_elements = [organization.getName(), organization.getRole()]
                organization_str = " - ".join(organization_elements) if organization_elements else "No exist organization."
                print(organization_str)
        else:
            print("No exist organization.")
    def displayAllCompanies(self):
        print("Company: ")
        if self.companies:
            for company in self.companies:
                print(company.getName())
        else:
            print("No exist company.")
    def displayAllCategories(self):
        print("Category:")
        if self.categories:
            for category in self.categories:
                print(category.getAllAtrributes())
        else:
            print("No exist category.")
    def printSearchResult(self, result):
        for i in result:
            if i == "projects":
                print("Project:")
                if result[i]:
                    for project in result[i]:
                        print(project.getAllAttributes())
                else:
                    print("No exist project.")
            elif i == "organizations":
                print("Organization:")
                if result[i]:
                    for organization in result[i]:
                        print(organization.getAllAttributes())
                else:
                    print("No exist organization.")
            elif i == "companies":
                print("Company:")
                if result[i]:
                    for company in result[i]:
                        print(company.getName())
                else:
                    print("No exist company.")
            elif i == "categories":
                print("Category:")
                if result[i]:
                    for category in result[i]:
                        print(category.getAllAtrributes())
                else:
                    print("No exist category.")        
    def userInput(self):
        print("I - Insert new project | S - Search by Project, Location, Organization, Company, or Category | X - Quit the program", sep = "\n")
        print( "1 - Display all projects, organizations, comapanies", "2 - Display all projects", "3 - Display all organizations", "4 - Display all companies", "5 - Display all categories", sep = "\n")
        user_input = input("Please enter the service you want: ")
        return user_input

system = SystemController()

p1 = system.createProject('p1', 'l1', 'status1', 'rating1', 'score1', 'date1', 'tool1')
com1 = system.addCompany('com1', 'p1', 'l1')
o1 = system.addOrganization('o1', 'role1', 'p1', 'l1')
cate1 = system.addCategory('c1', 'a1', 'p1', 'l1')
cate2 = system.addCategory('c2', 'a2', 'p1', 'l2')
p1.addOrganization(o1)
p1.setCompany(com1)
p1.addCategory(cate1)
p1.addCategory(cate1)

# Creating a new project with associated entities
p2 = system.createProject('p2', 'l2', 'status2', 'rating2', 'score2', 'date2', 'tool2')
com2 = system.addCompany('com2', 'p2', 'l2')
o2 = system.addOrganization('o2', 'role2', 'p2', 'l2')
cate3 = system.addCategory('c3', 'a3', 'p2', 'l2')
cate4 = system.addCategory('c4', 'a4', 'p2', 'l3')
# Linking the created entities to the project
p2.addOrganization(o2)
p2.setCompany(com2)
p2.addCategory(cate3)
p2.addCategory(cate4)

# Creating another new project with associated entities
p3 = system.createProject('p3', 'l1', 'status3', 'rating3', 'score3', 'date3', 'tool3')
com3 = system.addCompany('com1', 'p3', 'l1')
o31 = system.addOrganization('o1', 'role1', 'p3', 'l1')
o32 = system.addOrganization('o1', 'role2', 'p3', 'l1')
cate5 = system.addCategory('c1', 'a1', 'p3', 'l1')
cate6 = system.addCategory('c6', 'a6', 'p3', 'l1')

# Linking the created entities to the project
p3.addOrganization(o31)
p3.addOrganization(o32)
p3.setCompany(com3)
p3.addCategory(cate5)
p3.addCategory(cate6)



user = system.userInput()
while user != 'X' and user != 'x':
    if user == 'I' or user == 'i':
        print("Now you can insert a new project.")
        title = input("Please enter the new project title: ")
        while not system.checkProjectTitle( title):
            print("Your project tile is already exist.")
            title = input("Please enter the new project title: ")
        location = input("Please enter the new project location: ")
        status = input("Please enter the new project status: ")
        rating = input("Please enter the new project rating number: ")
        score = input("Please enter the new project score: ")
        date = input("Please enter the certified date (dd/mm/yyyy): ")
        tool = input("Please enter the rating tool: ")
        newproject = system.createProject(title, location, status, rating, score, date, tool)
        company_name = input("What is the main company of this project?: ")
        newCompany = system.addCompany(company_name, title, location)
        newproject.setCompany(newCompany)
        user_organization = input("Do you want to add new ORGANIZATION to this project? (Y - yes, N - no): ")
        while user_organization != 'N' and user_organization != 'n':
            if user_organization == 'Y' or user_organization == 'y':
                organization_name = input("Please enter the ORGANIZATION name: ")
                organization_role = input("Please enter the ORGANIZATION role: ")
                newOrganization = system.addOrganization(organization_name, organization_role, title, location)
                newproject.addOrganization(newOrganization)
            else:
                print("System does not understand you command. Please enter again.")
            user_organization = input("Do you want to add new ORGANIZATION to this project? (Y - yes, N - no): ")
        user_category = input("Do you want to add new CATEGORY to this project? (Y - yes, N - no): ")
        while user_category != 'N' and user_category != 'n':
            if user_category == 'Y' or user_category == 'y':
                category_name = input("Please enter the CATEGORY name: ")
                acheivement = input("Please enter the CATEGORY acheivement: ")
                newCategory = system.addCategory(category_name, acheivement, title, location)
                newproject.addCategory(newCategory)
            else:
                print("System does not understand you command. Please enter again.")
            user_category = input("Do you want to add new CATEGORY to this project? (Y - yes, N - no): ")

    elif user == 'S' or user == 's':
        print("1 - Search by project title", "2 - Search by location", "3 - Search by organization", "4 - Search by company", "5 - Search by organization", "X - Exit the search function", sep = "\n")
        search_option = input("Please select the search option that you want: ")
        while search_option != 'X' and search_option != 'x':
            if search_option == '1':
                search_title = input("Please enter the project title you want to search: ")
                system.searchByTitle(search_title)
            elif search_option == '2':
                search_location = input("Please enter the project location you want to search: ")
                system.searchByLocation(search_location)
            elif search_option == '3':
                print("Please enter the name and role of the organization for searching")
                organ_name = input("Organization name: ")
                organ_role = input("Organization role: ")
                # unique organization
                system.searchByOrganization(organ_name, organ_role)
            elif search_option == '4':
                company_name = input("Please enter the company name for searching: ")
                system.searchByCompany(company_name)
            elif search_option == '5':
                category_name = input("Please enter the category name for searching: ")
                system.searchByCategory(category_name)
            else:
                print("System does not understand you command. Please enter again.")
            print("1 - Search by project title", "2 - Search by location", "3 - Search by organization", "4 - Search by company", "5 - Search by organization", "X - Exit the search function", sep = "\n")
            search_option = input("Please select the search option that you want: ")
    elif user == "1":
        system.displayAll()
    elif user == "2":
        system.displayAllProjects()
    elif user == "3":
        system.displayAllOrganizations()
    elif user == "4":
        system.displayAllCompanies()
    elif user == '5':
        system.displayAllCategories()
    else:
        print("System does not understand you command. Please enter again.")
    print("\n", end = "")
    user = system.userInput()