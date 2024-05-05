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
        return self.rating
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
        attributes = [self.title, self.location, self.status, self.score, self.date, self.tool]
        attributes_str = " - ".join(attributes) if attributes else "NULL"
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

# system that manage all function of the program
class SystemController:
    def __init__(self):
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
            if category.getName() == name and category.getAchievement() ==  achievement:
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

        elif user == 'S' or user == 's':
            print("1 - Search by project title", "2 - Search by location", "3 - Search by organization", "4 - Search by company", "5 - Search by category", "X - Exit the search function", sep = "\n")
            search_option = input("Please select the search option that you want: ")
            while search_option != 'X' and search_option != 'x':
                if search_option == '1':
                    search_title = input("Project title: ")
                    result = self.searchByTitle(search_title)
                    self.printSearchResult(result)
                    output_str = self.searchByTitle_OutputFile(search_title)
                    # self.exportOutputFile('output.txt', output_str)
                elif search_option == '2':
                    search_location = input("Location: ")
                    result = self.searchByLocation(search_location)
                    self.printSearchResult(result)
                    output_str = self.searchByLocation_OutputFile(search_location)
                    # self.exportOutputFile('output.txt', output_str)
                elif search_option == '3':
                    print("Please enter the name and role of the organization for searching")
                    organ_name = input("Organization name: ")
                    organ_role = input("Organization role: ")
                    result = self.searchByOrganization(organ_name, organ_role)
                    self.printSearchResult(result)
                    output_str = self.searchByOrganization_OutputFile(organ_name, organ_role)
                    # self.exportOutputFile('output.txt', output_str)
                elif search_option == '4':
                    company_name = input("Company name: ")
                    result = self.searchByCompany(company_name)
                    self.printSearchResult(result)
                    output_str = self.searchByCompany_OutputFile(company_name)
                    # self.exportOutputFile('output.txt', output_str)
                elif search_option == '5':
                    category_name = input("Category name: ")
                    category_achievement = input("Category achievement: ")                
                    result = self.searchByCategory(category_name, category_achievement)
                    self.printSearchResult(result)
                    output_str = self.searchByCategory_OutputFile(category_name, category_achievement)
                    # self.exportOutputFile('output.txt', output_str)
                else:
                    output_str = "System does not understand your command. Please enter again."
                    print("System does not understand your command. Please enter again.")
                self.exportOutputFile('output.txt', output_str)
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
            print("System does not understand your command. Please enter again.")
        print("- - - - - - - - - -")         

    # import input file to the program (the input file includes information about the project, organization, company, and category)
    # check the error when importing input file - title cannot be same as exist one, title cannot be empty
    # the checking error will notify that which row of input-file has the error 
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
                        company = self.addCompany(i)
                        p.setCompany(company)
                    for i in category_arr:
                        category = self.addCategory(i[0], i[1])
                        p.addCategory(category)
                except Exception as e:
                    print(f'At line {row_number}: ERROR when importing project: {e} !!!')

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
    def systemOperating(self):
        try:
            self.userServiceRequirement()
        except Exception as e:
            print(f"An error accurred: {e}")

system = SystemController()
system.importInputFile('input.txt')
user = system.userInput()
while user != 'X' and user != 'x':
    system.systemOperating()
    user = system.userInput()