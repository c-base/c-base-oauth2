# c-base-oauth2
A OAuth2 service to authenticate c-base members and allow them access to c-base-owned services


# apache

```
    <Location "/oauth/">
        ProxyPass "http://127.0.0.1:8000/oauth/"
        ProxyPassReverse "http://127.0.0.1:8000/oauth/"
    </Location>
```
