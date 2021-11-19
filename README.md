# c-base-oauth2
A OAuth2 service to authenticate c-base members and allow them access to c-base-owned services

# apache

```
    <Location "/oauth/">
        RequestHeader set X-Forwarded-Proto 'https' env=HTTPS

        ProxyPass "http://127.0.0.1:8000/oauth/"
        ProxyPassReverse "http://127.0.0.1:8000/oauth/"
    </Location>
```

# Install 

```
apt install python3 python3-dev libldap2-dev libsasl2-dev
adduser oauth
sudo -u oauth -i
# then install poetry as user oauth
```

Generate RSA key for OpenID Connect:

see: https://django-oauth-toolkit.readthedocs.io/en/latest/oidc.html

```
openssl genrsa -out /home/oauth/oidc.key 4096
```
