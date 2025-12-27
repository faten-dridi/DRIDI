from netmiko import ConnectHandler

def acces_netmiko():
    routeur = {
        "device_type": "cisco_iosxr",
        "host": "sandbox-iosxr-1.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "port": 22,
    }

    print("Connexion au routeur Cisco C8000V...")
    connexion = ConnectHandler(**routeur)

    # Affiche la date côté routeur
    clock = connexion.send_command("show clock")
    print("Date du routeur :")
    print(clock)

    # Affiche les interfaces et les sauvegarde dans un fichier
    interfaces = connexion.send_command("show interfaces")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)

    connexion.disconnect()

def dire_bonjour():
    print("Hello, Git!")

if __name__ == "__main__":
    dire_bonjour()
    acces_netmiko()
