# project class
class Project:
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
        attributes_str = " - ".join(attributes) if attributes else "NULL"
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
        return False
    def checkCategory(self, name, achievement):
        for category in self.categories:
            if category.getName() == name and category.getachievement() == achievement:
                return True
        return False

# organization class
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

# company class
class Company:
    def __init__(self, name) -> None:
        self.name = name
    def getName(self):
        return self.name

# category class
class Category:
    def __init__(self, name, achievement) -> None:
        self.category_name = name
        self.achievement = achievement
    def getName(self):
        return self.category_name
    def getachievement(self):
        return self.achievement
    def getAllAtrributes(self):
        attributes = [self.category_name, self.achievement]
        attribute_str = " - ".join(attributes) if attributes else "NULL"
        return attribute_str

# system that manage all function of the program
class SystemController:
    def __init__(self) -> None:
        self.projects = []
        self.organizations = []
        self.companies = []
        self.categories = []

    # create a project form project class
    def createProject(self, title, location, status, rating, score, date, tool):
        newProject = Project(title, location, status, rating, score, date, tool)
        self.projects.append(newProject)
        return newProject
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
            if category.getName() == name and category.getachievement() ==  achievement:
                return category
        return
    
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
                if project.getCompany().getName() == name:
                    result["projects"].append(project)
                    for organization in project.getOrganizations():
                        if organization not in result["organizations"]:
                            result["organizations"].append(organization)
                    for category in project.getCategories():
                        if category not in result["categories"]:
                            result["categories"].append(category)
        return result
    # search all relevant information by category
    def searchByCategory(self, name, achievement):
        result = {"projects" : [], 
                  "organizations" : [], 
                  "companies" : [],
                  "categories" : []}
        search_category = None
        for category in self.categories:
            if category.getName() == name and category.getachievement() == achievement:
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
    
    # print all projects, organizations, conpanies and categories in system
    def displayAll(self):
        self.displayAllProjects()
        self.displayAllOrganizations()
        self.displayAllCompanies()
        self.displayAllCategories()

    # print all elements of all projects in system
    def displayAllProjects(self):
        print("Project: ")
        if self.projects:
            for project in self.projects:
                print(project.getAllAttributes())
        else:
            print("No exist project.")

    # print all organization names and roles in the system
    def displayAllOrganizations(self):
        print("Organization: ")
        if self.organizations:
            for organization in self.organizations:
                organization_elements = [organization.getName(), organization.getRole()]
                organization_str = " - ".join(organization_elements) if organization_elements else "No exist organization."
                print(organization_str)
        else:
            print("No exist organization.")

    # print all company names in the system
    def displayAllCompanies(self):
        print("Company: ")
        if self.companies:
            for company in self.companies:
                print(company.getName())
        else:
            print("No exist company.")
    
    # print all category names and achievements in the system
    def displayAllCategories(self):
        print("Category:")
        if self.categories:
            for category in self.categories:
                print(category.getAllAtrributes())
        else:
            print("No exist category.")

    # print the result - the dictionary that gain from search function
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
    
    # get the user's requirement functions
    def userInput(self):
        print("I - Insert new project | S - Search by Project, Location, Organization, Company, or Category | X - Quit the program", sep = "\n")
        print( "1 - Display all projects, organizations, comapanies, and categories", "2 - Display all projects", "3 - Display all organizations", "4 - Display all companies", "5 - Display all categories", sep = "\n")
        user_input = input("Please enter the service you want: ")
        return user_input
    def userServiceRequirement(self):
        if user == 'I' or user == 'i':
            print("Now you can insert a new project.")
            title = input("Please enter the new project title: ")
            while not self.checkProjectTitle( title):
                print("Your project title is already exist or project tile is not valid.")
                title = input("Please enter the new project title: ")
            location = input("Please enter the new project location: ")
            status = input("Please enter the new project status: ")
            rating = input("Please enter the new project rating number: ")
            score = input("Please enter the new project score: ")
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
                    print("System does not understand you command. Please enter again.")
                user_organization = input("Do you want to add new ORGANIZATION to this project? (Y - yes, N - no): ")
            user_category = input("Do you want to add new CATEGORY to this project? (Y - yes, N - no): ")
            while user_category != 'N' and user_category != 'n':
                if user_category == 'Y' or user_category == 'y':
                    category_name = input("Please enter the CATEGORY name: ")
                    achievement = input("Please enter the CATEGORY achievement: ")
                    newCategory = self.addCategory(category_name, achievement)
                    newproject.addCategory(newCategory)
                else:
                    print("System does not understand you command. Please enter again.")
                user_category = input("Do you want to add new CATEGORY to this project? (Y - yes, N - no): ")

        elif user == 'S' or user == 's':
            print("1 - Search by project title", "2 - Search by location", "3 - Search by organization", "4 - Search by company", "5 - Search by category", "X - Exit the search function", sep = "\n")
            search_option = input("Please select the search option that you want: ")
            while search_option != 'X' and search_option != 'x':
                if search_option == '1':
                    search_title = input("Please enter the project title you want to search: ")
                    result = self.searchByTitle(search_title)
                    self.printSearchResult(result)
                    self.exportOutputFile('output.txt', result, "project")
                elif search_option == '2':
                    search_location = input("Please enter the project location you want to search: ")
                    result = self.searchByLocation(search_location)
                    self.printSearchResult(result)
                    self.exportOutputFile('output.txt', result, "location")
                elif search_option == '3':
                    print("Please enter the name and role of the organization for searching")
                    organ_name = input("Organization name: ")
                    organ_role = input("Organization role: ")
                    result = self.searchByOrganization(organ_name, organ_role)
                    self.printSearchResult(result)
                    self.exportOutputFile('output.txt', result, "organization")
                elif search_option == '4':
                    company_name = input("Please enter the company name for searching: ")
                    result = self.searchByCompany(company_name)
                    self.printSearchResult(result)
                    self.exportOutputFile('output.txt', result, "company")
                elif search_option == '5':
                    category_name = input("Please enter the category name for searching: ")
                    category_achievement = input("Please enter the category achievement for searching: ")                
                    result = self.searchByCategory(category_name, category_achievement)
                    self.printSearchResult(result)
                    self.exportOutputFile('output.txt', result, "category")
                else:
                    print("System does not understand your command. Please enter again.")
                print("1 - Search by project title", "2 - Search by location", "3 - Search by organization", "4 - Search by company", "5 - Search by category", "X - Exit the search function", sep = "\n")
                search_option = input("Please select the search option that you want: ")
        elif user == "1":
            self.displayAll()
        elif user == "2":
            self.displayAllProjects()
        elif user == "3":
            self.displayAllOrganizations()
        elif user == "4":
            self.displayAllCompanies()
        elif user == '5':
            self.displayAllCategories()
        else:
            print("System does not understand you command. Please enter again.")
        print("- - - - - - - - - -")

    def check_DataType_Input(self, attribute_input, data_type):
        try:
            if attribute_input == "project_title":
                raise DataType_Input_Error("Wrong input data type for score")
            if attribute_input == "location":
                raise DataType_Input_Error("Wrong input data type for location")
            if attribute_input == "score":
                raise DataType_Input_Error("Wrong input data type for status")
            if attribute_input == "score":
                if type(attribute_input) == int:
                    raise DataType_Input_Error("Wrong input data type for score")
        except DataType_Input_Error as e:
            print(f'This {e}')
        except ValueError as e:
            print(f'This {e}')            

    # import input file to the program (the input file includes information about the project, organization, company, and category)
    # check the error when importing input file - title cannot be same as exist one, title cannot be empty
    def importInputFile(self, input_file):
        with open(input_file, 'r') as file:
            lines = file.readlines()
            for row_number, line in enumerate(lines, 1):
                try:
                    if line.strip() == "":
                        raise Exception("Empty row")
                    attributes = line.split(',')
                    project_dict = self.getProjectValues(attributes)
                    if project_dict["title"].strip() == "":
                        raise Exception("Project's title is not valid")
                    elif not self.checkProjectTitle(project_dict["title"]):
                        raise Exception("Project's title already exists")
                    organization_arr = self.getOrganizationValues(attributes)
                    company_arr = self.getCompanyValues(attributes)
                    category_arr = self.getCategoryValues(attributes)
                    
                    p = self.createProject(project_dict["title"], project_dict["location"], project_dict["status"], project_dict["rating"], project_dict["score"], project_dict["date"], project_dict["tool"])
                    for i in organization_arr:
                        organization = self.addOrganization(i[0], i[1])
                        p.addOrganization(organization)
                    for i in company_arr:
                        compayny = self.addCompany(i)
                        p.setCompany(compayny)
                    for i in category_arr:
                        category = self.addCategory(i[0], i[1])
                        p.addCategory(category)
                except Exception as e:
                    print(f'At line {row_number}: ERROR when importing project: {e} !!!')
        # except IOError as e:
        #     print(f"An error occureed while accesing the files: {e}")
        # except Exception as e:
        #     print(f"An error accurred: {e}")
    def exportOutputFile(self, output_file, result, searching_attribute):
        if result:
            with open(output_file, 'w') as file:
                for i in result:
                    if i == "projects":
                        file.write("Project:")
                        file.write("\n")
                        if result[i]:
                            for project in result[i]:
                                file.write(project.getAllAttributes())
                                file.write("\n")
                        else:
                            file.write("No exist project.")
                            file.write("\n")
                    elif i == "organizations":
                        file.write("Organization:")
                        file.write("\n")
                        if result[i]:
                            for organization in result[i]:
                                file.write(organization.getAllAttributes())
                                file.write("\n")
                        else:
                            file.write("No exist organization.")
                            file.write("\n")
                    elif i == "companies":
                        file.write("Company:")
                        file.write("\n")
                        if result[i]:
                            for company in result[i]:
                                file.write(company.getName())
                                file.write("\n")
                        else:
                            file.write("No exist company.")
                            file.write("\n")
                    elif i == "categories":
                        file.write("Category:")
                        file.write("\n")
                        if result[i]:
                            for category in result[i]:
                                file.write(category.getAllAtrributes())
                                file.write("\n")
                        else:
                            file.write("No exist category.")
                            file.write("\n")
        else:
            file.write("Program can not search for related projects, organizations, companies, and categories.")

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
                    # key, value = attribute.split(':')
                    result["title"] = value
                elif "location" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    # key, value = attribute.split(':')                   
                    result["location"] = value
                elif "status" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    # key, value = attribute.split(':')
                    result["status"] = value
                elif "rating" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    # key, value = attribute.split(':')
                    result["rating"] = value
                elif "score" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    # key, value = attribute.split(':')
                    result["score"] = value
                elif "date" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    # key, value = attribute.split(':')
                    result["date"] = value
                elif "tool" in attribute:
                    colon_position = attribute.find(':')
                    if colon_position == -1:
                        value = ""
                    else:
                        value = attribute[colon_position + 1:].strip()
                    # key, value = attribute.split(':')
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
                # find the role of organization when we can collect the organization nam already
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
                    value1 = attributes[i][colon_position + 1:].strip()
                # find the role of organization when we can collect the organization nam already
                i += 1
                if attributes[i]:
                    colon_position = attributes[i].find(':')
                    if colon_position == -1:
                        value2 = ""
                    else:
                        value2 = attributes[i][colon_position + 1:].strip()
                result.append((value1, value2))
                result.append((value1.strip(), value2.strip()))       
        return result
class DataType_Input_Error(Exception):
    "The data type is not appropriate"
class InputFile_Error(Exception):
    def __init__(self, message):
        super().__init__(message)
class CustomeError(Exception):
    def __init__(self, message = "Error!!!"):
        message = message
        super().__init__(message)

system = SystemController()
system.importInputFile('input.txt')

# p1 = system.createProject('p1', 'l1', 'status1', 'rating1', 'score1', 'date1', 'tool1')
# com1 = system.addCompany('com1')
# o1 = system.addOrganization('o1', 'role1')
# o1_2 = system.addOrganization('o1_2', 'role1_2')
# cate1 = system.addCategory('c1', 'a1')
# cate2 = system.addCategory('c2', 'a2')
# p1.addOrganization(o1)
# p1.addOrganization(o1_2)
# p1.setCompany(com1)
# p1.addCategory(cate1)
# p1.addCategory(cate2)

# # Creating a new project with associated entities
# p2 = system.createProject('p2', 'l2', 'status2', 'rating2', 'score2', 'date2', 'tool2')
# com2 = system.addCompany('com2')
# o2 = system.addOrganization('o2', 'role2')
# cate3 = system.addCategory('c3', 'a3')
# cate4 = system.addCategory('c4', 'a4')
# # Linking the created entities to the project
# p2.addOrganization(o2)
# p2.setCompany(com2)
# p2.addCategory(cate3)
# p2.addCategory(cate4)

# # Creating another new project with associated entities
# p3 = system.createProject('p3', 'l1', 'status3', 'rating3', 'score3', 'date3', 'tool3')
# com3 = system.addCompany('com1')
# o31 = system.addOrganization('o1', 'role1')
# o32 = system.addOrganization('o1', 'role2')
# cate5 = system.addCategory('c1', 'a1')
# cate6 = system.addCategory('c6', 'a6')

# # Linking the created entities to the project
# p3.addOrganization(o31)
# p3.addOrganization(o32)
# p3.setCompany(com3)
# p3.addCategory(cate5)
# p3.addCategory(cate6)

user = system.userInput()
while user != 'X' and user != 'x':
    system.userServiceRequirement()
    user = system.userInput()