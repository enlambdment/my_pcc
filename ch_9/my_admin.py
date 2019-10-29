from admin import Privileges, Admin

my_privs = Privileges(('can add post', 'can ban user'))
my_privs.show_privileges()

my_admin = Admin('einstein', 'q rembrandt', my_privs)
my_admin.privileges.show_privileges()