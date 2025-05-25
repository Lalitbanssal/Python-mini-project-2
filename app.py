from user import Signup, Login 

user_list = []
def main_app():
    print(" This is a demo social media app")
    print("-" * 80)

    

    a = input("Do you want to login or signup? Please enter (or type 'exit' to quit): ")

    if a.lower() == 'exit':
        print("Goodbye! See you next time.")
        return  
    
    while a.lower() != 'login' and a.lower() != 'signup':
        print("Invalid option. Please enter either 'login' or 'signup' (or 'exit' to quit)")
        a = input("Do you want to login or signup? Please enter: ")
        if a.lower() == 'exit':
            print("Goodbye! See you next time.")
            return  

    if a.lower() == 'signup':
        print("Enter the user_id: Your first name + mobile number")
        print("Example: Name --> Lalit Bansal, Mobile No. --> 87***45694")
        print("So, user_id will be: Lalit87***45694")
        user_id = input("Enter the user_id to be created: ")

        
        exists = False
        for user in user_list:
            if user.user_id == user_id:
                exists = True
                break

        if exists:
            print(" User already exists. Please login.")
            main_app()  
        else:
            password = input("Enter the password (at least 6 characters): ")
            while len(password) < 6:
                password = input("Password too short. Please re-enter (at least 6 characters): ")
            new_user = Signup(user_id, password)
            user_list.append(new_user)
            print("Signup successful. You can now login.")
            main_app()  

    elif a.lower() == 'login':
        user_id = input("Enter your user_id: ")
        password = input("Enter your password: ")
        logged_in = Login(user_id, password, user_list)

        if hasattr(logged_in, 'logged_in_user'):  
            action = input("Do you want to make a post? (yes/no): ").lower()
            if action == 'yes':
                logged_in.logged_in_user.make_post()  

        main_app()  