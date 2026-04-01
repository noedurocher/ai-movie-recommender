from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db = {}

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_user(username, password):
    hashed = get_password_hash(password)
    users_db[username] = {"username": username, "password":hashed}
    
def get_user(username):
    return users_db.get(username) 