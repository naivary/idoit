# Install i-doit using Ansible

## Restore from Backup

!!IMPORTANT!!: When you are loading the backup make sure that the tenant
connections details are set to the correct database. You can check them by
running the following query on the `idoit_system` database:

```sql
USE idoit_system;
SELECT isys_mandator__title, isys_mandator__db_host, isys_mandator__db_port, isys_mandator__db_name, isys_mandator__db_user, isys_mandator__db_pass, isys_mandator__apikey FROM isys_mandator;
```


error_log(print_r($mandators, TRUE));


in der config von argo2i zu bcrypt umstellen

Passwörter werden generiert durch <hash><password> -> bcrypt (hash kommt aus
config.inc.php)

ppa:ondrej/php
ppa:ondrej/apache


php8.1 hat das problem das das mysqli modul denkt das socket von mysql ist unter
/var/lib man muss es unter /etc/php/8.1/{cli,apache2}/conf.d/20-mysqli.ini
umstellen auf: mysqli.default_socket = /var/run/mysqld/mysqld.sock

26 -> 29 (AUTH_DOMAIN_... muss auskommentiert werden in beiden PHP Dateien) ->
30 -> 33 -> 34 -> 35

Updates können hier gefunden werden: https://kb.i-doit.com/de/download-links.html

src/idoit/Console/Command/Idoit/FeatureManagerCommand.php
src/idoit/Console/Command/Idoit/SetEnvVarCommand.php

Ini Setting: max_input_vars > 10000:  failed   WARN
Ini Setting: post_max_size > 128M:  failed     WARN
php-ext: mod_rewrite:  failed                  WARN

        ## - Apache HTTPD >= 2.4 with enabled modules:
        ##   - rewrite
        ##   - expires
        ##   - headers
        ##   - authz_core

