from oauth2_provider.oauth2_validators import OAuth2Validator


class CustomOAuth2Validator(OAuth2Validator):
    def get_oidc_claims(self, token, token_handler, request):
        scopes = request.scopes
        if request.access_token is not None and request.access_token.scope is not None:
            scopes = request.access_token.scope.split()

        claims = {
            "sub": request.user.username,
            "nickname": request.user.username,
            "preferred_username": request.user.username,
        }

        if 'email' in scopes:
            claims["email"] = request.user.email
            claims["email_verified"] = True

        if 'groups' in scopes:
            claims["groups"] = [str(group) for group in request.user.groups.all()]

        return claims
