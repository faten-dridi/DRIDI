# Mon Projet Netmiko
## Commandes Git utilisées

### Initialisation du dépôt
```bash
mkdir fatendridinetmiko
cd fatendridinetmiko
git init

git add README.md
git commit -m "Ajout du fichier README"

git add main.py
git commit -m "Ajout du script Python principal"

git checkout -b feature/netmiko
git checkout main
git merge feature/netmiko

git remote add origin https://github.com/USERNAME/prenom-nom-netmiko.git
git push -u origin main
git fetch origin
git checkout -b feature/salut origin/feature/salut
git push origin feature/salut
git pull origin main
