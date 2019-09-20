from flask import Flask, request, escape

app = Flask(__name__)
users = [{'id': 1, 'name': 'Matt', 'age': 25}]

@app.route("/user/<int: id>")
def user(id):
	return dictionary()

@app.route("/users")
def get_users():
	return users[0]

@app.route("/dictionary") 
def dictionary():
	name = input("Enter your name: ")
	age  = input("Enter your age: ")
	id   = input("Enter your id: ")
	name = str(name)
	age  = int(age)
	id   = int(id)
	new_user = {'id': id, 'name': name, 'age': age}
	users.append(new_users)
	return new_user

@app.route("/")
def myName():
	return "Your name is cool!!!"

if __name__ == '__main__':
	app.run(debug=True)