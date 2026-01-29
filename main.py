from database import create_tables
from services.auth_service import AuthService

create_tables()

auth = AuthService()

# Try registering SAME email again
result = auth.register("Vikas", "vikas@gmail.com", "1234")

print("Register Result:", result)
