import napalm
import json

driver = napalm.get_network_driver("ios")

device = driver(
    hostname="192.168.122.20",
    username="u1",
    password="cisco",
    optional_args={"secret": "cisco", "port": 22}
)

device.open()

interfaces = device.get_interfaces()

with open("interfaces.txt", 'w') as file:
    file.write(json.dumps(interfaces))

users = device.get_users()

with open("users.txt", 'w') as file:
    file.write(json.dumps(users))

device.close()

