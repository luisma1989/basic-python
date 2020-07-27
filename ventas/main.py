import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as file:
        reader = csv.DictReader(file, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
        os.rename(tmp_table, CLIENT_TABLE)


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already exists in the client\'s list')


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients

    for idx in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def list_clients():
    global clients

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {email} | {company} | {postion} '.format(
            uid=idx,
            name=client['name'],
            email=client['email'],
            company=client['company'],
            postion=client['position']
        ))


def _print_welcome():
    print('Welcome')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    print('[L]ist clients')


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))

    return field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the update client name?')
        update_client(client_name, updated_client_name)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is  in the client\'s list.')
        else:
            print('The client: {} is not in the client\'s list'.format(client_name))
    elif command == 'L':
        list_clients()
    else:
        print('Invalid command')

    _save_clients_to_storage()
