import functools

user = {"username": "Jone",  "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(panel):
        if user["access_level"] == "admin":
            return func(panel)
        else:
            return f"No admin permissions for {user['username']}."
    
    return secure_function

@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return  "supper_secure_password"

print(get_admin_password("billing"))