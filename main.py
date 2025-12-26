from netmiko import ConnectHandler

routeur = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxe-1.cisco.com",
    "username": "admin",
    "password": "cisco12345",
    "port": 22,
}

def main():
    print("Connexion au routeur...")
    connection = ConnectHandler(**routeur)
    connection.enable()

    print(connection.send_command("show clock"))

    interfaces = connection.send_command("show ip interface brief")
    with open("interface.txt", "w") as f:
        f.write(interfaces)

    config = [
        "interface loopback0",
        "ip address 10.8.8.8 255.255.255.240",
        "no shutdown"
    ]

    connection.send_config_set(config)
    connection.disconnect()

if __name__ == "__main__":
    main()
    