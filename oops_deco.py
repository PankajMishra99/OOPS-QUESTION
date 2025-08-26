# Requirement
# You are building a User Access System for an application.
# Features:
# Each user has a name and role (e.g., 'Admin', 'Editor', 'Viewer').
# Some actions (methods) should only be accessible to specific roles.
# If a user tries to access a method without the correct role, they should get an “Access Denied” message.

def decorator(role):
    def wrapper(func):
        def inner_function(self,*args,**kwargs):
            if self.user.role==role:
                return func(self,*args,**kwargs)
            else:
                return f"Access denied { self.user.name} and does not have {role}"
        return inner_function
    return wrapper

class User:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    

class Content_system:
    def __init__(self,user):
        self.user=user
    
    @decorator('Admin')
    def delete_content(self):
        return f"{self.user.name} deleted the content.."

    @decorator('Editer')
    def editer_content(self):
        return f"{self.user.name} edited the content.."
    
    @decorator('Viwer')
    def viwer_content(self):
        return f"{self.user.name} view the content.."


if __name__=='__main__':
    admin=Content_system(User('Amit','Admin'))
    editer=Content_system(User('Mr.A','Editer'))
    view_content=Content_system(User('Mr.B','Viwer'))

    print(admin.delete_content())
    print(admin.editer_content())
    print(admin.viwer_content())

    