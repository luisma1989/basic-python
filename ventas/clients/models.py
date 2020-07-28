import uuid


class Client:  # Crea el objeto cliente
    # Inicializa las instancias del objeto Cliente
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        # Si no recibe como parametro la variable "uid", devuelve el ID UUID4(), que se utiliza
        # para generar ID'S en generral.
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        # Chequea lo que regresa el metodo __dict__ y nos realiza un diccionario de nuestro objeto
        return vars(self)

    @staticmethod  # Metodo estaticos dentro de nuestra clase, es un metodo que se puede ejecutar
    # sin la necesidad de una instancia de clase
    # No hace falta pasar por parametro SELF porque el decorador @staticmethod nos permite hacerlo.
    def schema():
        # devuelve una lista de las variables que existen en el objeto CLIENT'
        return ['name', 'company', 'email', 'position', 'uid']
