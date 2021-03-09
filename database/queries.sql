-- INSERT INTO role(name) VALUES('fotógrafo');
-- INSERT INTO role(name) VALUES('diagramador');
-- INSERT INTO role(name) VALUES('analista');
-- INSERT INTO role(name) VALUES('diretor');
-- INSERT INTO role(name) VALUES('recepcionista');

SELECT * FROM roles;

-- INSERT INTO employee(name, email, password, role_id, admin) VALUES('fabio','fabio@gmail.com','123',1,0);
-- INSERT INTO employee(name, email, password, role_id, admin) VALUES('viviane','viviane@gmail.com','abc',3,0);
-- INSERT INTO employee(name, email, password, role_id, admin) VALUES('nicole','nicole@gmail.com','000',5,0);
-- INSERT INTO employee(name, email, password, role_id, admin) VALUES('michelle','michelle@gmail.com','999',2,0);
-- INSERT INTO employee(name, email, password, role_id, admin) VALUES('joao','joao@gmail.com','123',1,0);
-- INSERT INTO employee(name, email, password, role_id, admin) VALUES('maria','maria@gmail.com','123',1,0);

SELECT * FROM employee;

SELECT 
	employee.name,
	employee.email,
	role.name AS role
FROM 
    employee
INNER JOIN role 
    ON employee.role_id = role.id;
