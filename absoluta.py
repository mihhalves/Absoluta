from flask import Flask, render_template, request, redirect, flash, url_for 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'random_super_secret_text'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/absoluta.db"
db = SQLAlchemy(app)

class Role(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String)
	employees = db.relationship('Employee', backref='role')

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    admin = db.Column(db.Boolean)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/role', methods=['POST','GET'])
def role():
    if request.method == 'POST':
        role_name = request.form['role']
        new_role = Role(name=role_name)

        try:
            db.session.add(new_role)
            db.session.commit()
            output = {'success': True, 'content':f"Cargo: { role_name } cadastrado!"}
            roles = Role.query.all()
            return render_template('role.html', roles=roles, message=output)
        except:
            output = {'success': False, 'content':'Falha ao efetuar cadastro'}
            roles = Role.query.all()
            return render_template('role.html', roles=roles, message=output)
    else:
        roles = Role.query.all()
        return render_template('role.html', roles=roles)

@app.route('/role/update/<int:id>', methods=['POST','GET'])
def role_update(id):
    role_to_update = Role.query.get_or_404(id)
    if request.method == 'POST':
        role_to_update.name = request.form['role']
        try:
            db.session.commit()
            output = {'success': True, 'content':f"Cargo: {role_to_update.name} atualizado!"}
            roles = Role.query.all()
            return render_template('role.html', roles=roles, message=output)
        except:
            return "Erro inesperado"
    else:
        roles = Role.query.all()
        return render_template('role.html', roles=roles, update=True, role=role_to_update )

@app.route('/role/delete/<int:id>')
def role_delete(id):
    role_to_delete = Role.query.get_or_404(id)

    try:
        db.session.delete(role_to_delete)
        db.session.commit()
        output = {'success': True, 'content':f"Cargo: {role_to_delete.name} removido!"}
        roles = Role.query.all()
        return render_template('role.html', roles=roles, message=output)
    except:
        return "Erro inesperado"

@app.route('/employee', methods=['POST','GET'])
def employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role_id = request.form['role']
        admin = request.form.get('admin', False)
        if admin:
            if admin == 'on':
                admin = True

        role = Role.query.get_or_404(role_id)

        new_employee = Employee(name=name, email=email, password=password, role=role, admin=admin)
        db.session.add(new_employee)
        db.session.commit()
        
        return redirect(url_for('employee'))

    
    all_roles = Role.query.all()
    return render_template('employee.html', roles=all_roles)

@app.route('/supplier')
def supplier():
    return render_template('supplier.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/teste')
def teste():
    return render_template('teste.html')

# fotografos = Role.query.filter_by(name='fotógrafo').first()

# print(fotografos.id)
# print(fotografos.name)
# for employee in fotografos.employees:
#     print(employee.name)
#     print(employee.email)