class Signup():
    def __init__(self, user_id, password):
        self.user_id = user_id
        self.password = password
        self.totalpost = 0  

    def make_post(self):
        
        self.totalpost += 1
        print(f"Post made successfully! Total posts: {self.totalpost}")


class Login():
    def __init__(self, user_id, password, user_list):
        self.user_id = user_id
        self.password = password

        found = False
        for user in user_list:
            if user.user_id == self.user_id:
                found = True
                if user.password == self.password:
                    print('Successful login')
                    self.logged_in_user = user  
                    self.show_user_info()  
                else:
                    print(' Invalid password')
                break

        if not found:
            print('User ID not found. Please sign up.')

    def show_user_info(self):
        print(f"Welcome {self.user_id}! You have made {self.logged_in_user.totalpost} posts.")
