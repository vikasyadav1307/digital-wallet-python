from database import connect_db


class AuthService:

    # Register User
    def register(self, name, email, password):
        try:
            conn = connect_db()
            cur = conn.cursor()

            cur.execute(
                "INSERT INTO users(name,email,password) VALUES(?,?,?)",
                (name, email, password)
            )

            conn.commit()
            conn.close()

            return "SUCCESS"

        except Exception as e:
            if "UNIQUE constraint failed" in str(e):
                return "EMAIL_EXISTS"
            else:
                return "ERROR"

    # Login User
    def login(self, email, password):
        try:
            conn = connect_db()
            cur = conn.cursor()

            cur.execute(
                "SELECT * FROM users WHERE email=? AND password=?",
                (email, password)
            )

            user = cur.fetchone()
            conn.close()

            return user

        except Exception as e:
            print("Login Error:", e)
            return None
