class User:

    # Constructor
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    # Show User Info (for testing)
    def show_user(self):
        print("User ID:", self.user_id)
        print("Name:", self.name)
        print("Email:", self.email)
