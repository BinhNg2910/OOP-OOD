class User:
    def __init__(self):
        self.service = ""
    def askService(self):
        self.service = input()

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
        self.categories.append[category]

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
    def getCategoryName(self):
        return self.category_name
    def getAcheivement(self):
        return self.acheivement
    def getProjectTitle(self):
        return self.project_title
    def getLocation(self):
        return self.location
    def getAllAtrributes(self):
        attributes = [self.name, self.acheivement]
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
        self.categories.append[newCategory]
        return newCategory
    
    def checkProjectTitle(self, title):
        if title == None:
            return False
        for project in self.projects:
            if project.getTile == title:
                return False
        return True
    
    def searchByTitle(self, title):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        check = False
        print("Project: ")
        for project in self.projects:
            if project.getTitle() == title:
                # print(project.getAllAttributes)
                result["projects"].append(project)
                # check = True
        # if not check:
            # print("No exist project.") 
        # check = False
        # print("Organization: ")
        for organization in self.organizations:
            if organization.getProjectTile() == title:
                # print(organization.getAllAttributes())
                result["organizations"].append[organization]
                # check = True
        # if not check:
            # print("No exist organization.") 
        # check = False
        # print("Company:")
        for company in self.companies:
            if company.getProjectTitle() == title:
                # print(company.getName())
                result["organizations"].append[organization]
                # check = True
        # if not check:
            # print("No exist company.")
        # check = False
        # print("Category:")
        for category in self.categories:
            if category.getProjectTitle() == title:
                # print(category.getAllAtrributes())
                result["categories"].append[category]
                # check = True
        # if not check:
            # print("No exist category.") 

    def searchByLocation(self, location):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        check = False
        print("Project: ")
        for project in self.projects:
            if project.getLocation() == location:
                print(project.getAllAttributes())
                result["projects"].append[project]
                check = True
        if not check:
            print("No exist project.")
        check = False
        print("Organization: ")
        for organization in self.organizations:
            if organization.getLocation() == location:
                print(organization.getAllAttributes())
                result["organizations"].append[organization]
                check = True
        if not check:
            print("No exist organization.")
        check = False
        print("Company:")
        for company in self.companies:
            if company.getLocation() == location:
                print(company.getName())
                result["companies"].append[company]
                check = True
        if not check:
            print("No exist company.")
        check = False
        print("Category:")
        for category in self.categories:
            if category.getLocation() == location:
                print(category.getAllAtrributes())
                result["categories"].append[category]
                check = True
        if not check:
            print("No exist category.")

    def searchByOrganization(self, name, role):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        search_organization = None
        for organization in self.organizations:
            if organization.getName() == name and organization.getRole():
                search_organization = organization
                result["organizations"].append(search_organization)
                break
        if search_organization:
            check = False
            print("Projects: ")
            for project in self.projects:
                if project.checkOrganization(name, role):
                    print(project.getAllAttributes())
                    result["projects"].append(project)
                    check = True
            if not check:
                print("No exist project.")
            print("Organization: ")
            print(name, " - ", role)
            check = False
            print("Company: ")
            for project in self.projects:
                if project.checkOrganization(name, role):
                    print(project.getCompany())
                    result["companies"].append(project.getCompany())
                    check = True
        else:
            print("This organization does not exist.")
    def searchByCompany(self, name):
        search_company = None
        for company in self.companies:
            if company.getName == name:
                search_company = company
                break
        if search_company:
            print("Projects: ")
            for project in self.projects:
                if project.getCompany().getName() == name:
                    project.getAllAttributes()
            print("Organization: ")
            for project in self.projects:
                if project.getCompany().getName() == name:
                    organ_list = project.getOrganization()
                    for organ in organ_list:
                        print(organ.getAllAttributes())
        else:
            print("There is no exist company.")
        
    def displayAll(self):
        self.displayAllProjects()
        self.displayAllOrganizations()
        self.displayAllCompanies()

    def displayAllProjects(self):
        print("Project: ")
        if self.projects:
            print("Project Title - Location - Status - Green Star Rating - Final Score - Date Certified - Rating Tool")
            for project in self.projects:
                # project_elements = project.getAllElements()
                # project_str = " - ".join(project_elements) if project_elements else "No exist project."
                print(project.getAllAttributes())
        else:
            print("No exist project.")
    def displayAllOrganizations(self):
        print("Organization: ")
        if self.organizations:
            print("Role - name")
            for organization in self.organizations:
                organization_elements = [organization.getRole(), organization.getName()]
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
            print("No exist company")

    def userInput(self):
        print("I to insert - S to search - X to quit", "1 to display all projects, organizations, comapanies", "2 to display all projects", "3 to display all organizations", "4 to display all companies", sep = "\n")
        user = input("Please enter the service you want: ")
        return user

system = SystemController()
user = system.userInput()

while user != 'X':
    if user == 'I':
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
        user_organization = input("Do you want to add new organization to this project? (Y - yes, N - no): ")
        while user_organization != 'N':
            if user_organization == 'Y':
                organization_name = input("Please enter the organization name: ")
                organization_role = input("Please enter the organization role: ")
                newOranization = system.addOrganization(organization_name, organization_role, title, location)
                newproject.addOrganization(newOranization)
            else:
                print("System does not understand you command. Please enter again.")
            user_organization = input("Do you want to add new organization to this project? (Y - yes, N - no): ")
    elif user == 'S':
        print("1 - Search by project title", "2 - Search by location", "3 - Search by organization", "4 - Search by company", sep = "\n")
        search_option = int(input("Please select the search option that you want: "))
        if search_option == 1:
            search_title = input("Please enter the project title you want to search: ")
            system.searchByTitle(search_title)
        elif search_option == 2:
            search_location = input("Please enter the project location you want to search: ")
            system.searchByLocation(search_location)
        elif search_option == 3:
            print("Please enter the role and name of the organization for searching")
            organ_name = input("Organization name: ")
            organ_role = input("Organization role: ")
        elif search_option == 4:
            company_name = input("Please enter the company name for searching")

    elif user == "1":
        system.displayAll()
    elif user == "2":
        system.displayAllProjects()
    elif user == "3":
        system.displayAllOrganizations()
    elif user == "4":
        system.displayAllCompanies()
    # user = input("Please enter the service you want (I to insert, S to search, or X to quit): ")
    print("\n", end = "")
    user = system.userInput()