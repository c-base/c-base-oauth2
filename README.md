# c-base-oauth2
A OAuth2 service to authenticate c-base members and allow them access to c-base-owned services

# apache

```
    <Location "/oauth/">
        ProxyPass "http://127.0.0.1:8000/oauth/"
        ProxyPassReverse "http://127.0.0.1:8000/oauth/"
    </Location>
```

# Install 

```
apt install python3 python3-dev libldap2-dev libsasl2-dev
adduser oauth
sudo -u oauth -i
# install poetry 
```

# How to create the first superuser

If you username is not 'uk', please replace 'uk' with your own username.

```
$ ./manage.py shell
...
>>> from c_base_oauth2.apps.users.models import User
>>> User.objects.get(username="uk")
<User: uk>
>>> u = User.objects.get(username="uk")
>>> u.is_s
u.is_staff      u.is_superuser
>>> u.is_staff = True
>>> u.is_superuser = True
>>> u.save()
>>>
```