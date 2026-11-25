def add_student():
    name= input("Enter Your Name :")
    std = input("Enter Your Standard :")
    department = input("Enter your department :")
    with open("student_management.txt","a") as file:
        file.write(f"Hi myname is {name}.\n")
        file.write(f"I am currently studying {std} std\n")
        file.write(f"My department name is  {department}\n")
        print("successfull")
        
        
def view_students():
    try:
        with open("student_management.txt","r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File is not Exists")
        
def search_student():
    search_name = input("Enter the Search Name : ")
    try:
        with open("student_management.txt","r") as file:
            content = file.read()
            if(search_name.lower() in content.lower() ):
                print(f"file exists the name {search_name}")
            else:
                print(f"file doesn't exists the name {search_name}")
    except FileNotFoundError:
        print("Text isn't Exists")
        
while True:
    print("\nWelcome to student Management System")
    print("1.Add student")
    print("2.View Students")
    print("3.Search Student")
    print("4.Close Program")
    try:
        choice = int(input(("Please Enter your choice :")))
    except ValueError:
        print("Please enter vaild Integer Number :")
    
    if(choice == 1):
        add_student()
    elif(choice == 2):
        view_students()
    elif(choice == 3):
        search_student()
    elif(choice == 4):
        print("exit Student Management")
    else:
        print("Invaild Choice ! please Enter 1, 2, or 3.")    
