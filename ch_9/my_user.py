from user import User

my_user = User('blue', 'kirby', True, False)

my_user.describe_user()
my_user.greet_user()

my_user.increment_login_attempts()
print(my_user.login_attempts)

my_user.increment_login_attempts()
print(my_user.login_attempts)

my_user.increment_login_attempts()
print(my_user.login_attempts)

my_user.reset_login_attempts()
print(my_user.login_attempts)