# Install i-doit using Ansible

To install i-doit with mariadb on two servers the following pre-requirements are
needed:
1. a python virtual environment
2. all pkgs listed in `requirements.txt`
3. ssh connection between the control node and the two servers
4. connection between the i-doit node and mariadb node

# Create inventory

In the `inventory.ini` set the ip-address or hostname of the mariadb server
under `mariadb` and i-doit unter `idoit`. 

# Run install playbook

```bash
ansible-playbook -i inventory.ini -b install.yml
```

# Update i-doit

To update i-doit use the `update.yml` playbook. The versions to which you want
update and the order of the updates can be set in the `versions` list. All
available updates can be found under: https://kb.i-doit.com/de/download-links.html

Before running update.yml make sure the admin user (admin center) can login
succesfully.

# Post install

If you already have used i-doit before than some config changes have to be done
manually in `config.inc.php`:
1. encryption method for passwords (argo2i -> bcrypt)

# Important

If you restored the last state of your i-doit from a MariaDB backup then make
sure that the tenant connection detauls are to the correct database. You can
check them by running the following query on the `idoit_system` database:

```sql
USE idoit_system;
SELECT isys_mandator__title, isys_mandator__db_host, isys_mandator__db_port, isys_mandator__db_name, isys_mandator__db_user, isys_mandator__db_pass, isys_mandator__apikey FROM isys_mandator;
```


