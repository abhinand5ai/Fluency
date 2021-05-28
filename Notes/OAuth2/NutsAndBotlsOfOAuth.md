# OAUTH BASICS

Cookie Based : Takes password gives a cookie and is used by application

OAuh : OAuth Server takes the credentials and gives access token to the application

* OAUTH : Delegated Authorization Server
* OpenIDConnect :  On top of OAuth Can provide identity

### Roles

1. User (Resource Owner)
2. Device (User Agent)
3. Application (OAuth Client)
4. Api (Resource Server)

5. Authorization Server

### OAuth Client Types

1. Confidential
    * Aps running on a server and can have client stored in the server (api keys in backend servers)
2. Public
    * Can't have credentials  (Mobile applications, Single Page App)
3. Credential Client
    * Gets one client secret during initialization and uses it to redeem the tokens (but still unidentified client)

### User Consent

User is redirected to Authorization Server which shows consent screen with the requested permission MultiFactor
Authentication can be added as extension easily to the authorization server

Confidential Clients can skip these

### Front Channel and Back Channel

Back Channel -> password taken by application encrypted and sent

Front Channel -> Pass it through address bar to oauth server and get access token

### Application Identity

* Application creates a secret key during the initialization uses it to redeem authorization code given by Authorization
  server
* Redirect URL is the only way now to decide the identity in mobile applications for the authorization server

## OAuth Clients

https://dev-45411978.okta.com/oauth2/default

### Registering Application

Give

1. Redirect URLs
2. Type of Application -> oAuthServer gives client ID. Client Secret is given only for the secured types like server ide
   applications

### Authorization Code flow

#### Web Application

APP creates PKCE code verifier 43 - 128 ---> Public hash -> Construct link and send to OAuth Server authorization code
injection

```
https://dev-45411978.okta.com/oauth2/default/v1/authorize? response_type=code& scope=photos&
client_id=0oarndnbmQUO7zu7d5d6& state=6d5d482f0005cc4ba0af9122e1bf7803675e927827ce419f0f0f5922&
redirect_uri=https://example-app.com/redirect&
code_challenge=n_BdpJDoP3WeU2kVP8z0KzT3FEkr1hL0KRRVTf9SH0U& code_challenge_method=S256
````

Use the Authorization Code from the redirected url and construct token request

```commandline
curl -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
-d grant_type=authorization_code \
-d redirect_uri=https://example-app.com/redirect \
-d client_id=0oarndnbmQUO7zu7d5d6 \
-d client_secret=A1bVR1d8u_J3K51cjzAYcTX_WiDiCed3hEqqCREo \
-d code_verifier=f2e6fbac089f6bd4504109e5579c4622a3c4830236c4089add15d14a \
-d code=93k58TFomgz05Fg0LkyBD9CCb4-tqGlAYb0HW0p1CTM
```

Get the access token as response

```json
    {
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmpoU1hwRl9sLVkzS3pfbDAzdEFrZzY0ZG9SR3dGa2IydTIzcmtCR0hYS0EiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjEzMjk0ODgsImV4cCI6MTYyMTMzMzA4OCwiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJwaG90b3MiXSwic3ViIjoiYWJoaW5hbmQ1YWlAZ2l0aHViLm9rdGFpZHAifQ.SdxPzizP4sMJw743FcaNgoFIOwjFVIz0Yb8P4D333uUvOGppM7WsABcxtUJ9RMzti5VXBfU4zL5XdxEFqOm4iVtzxkaSAeANaB9DEyBo-UwXvdL9vVz-szGAEBEOmuU6AWoiKScfBpXSgj6j3RMSReSUviiMN86-vW_yweQvR2txfqap3iRC45OgMMowMTGx1rSrqhyHEWMGt2QsYkATQzItrd9JmidAAckQ8dSqHVhYSKUYDFJAVNMBtVrwVHUUFub9jXvmFGEvEyHSU-kDzBdcXAzgBkjxAQyDSwB83-6h-cgxg6Az1F8q6YWFBuAWAFOxJA9dqzgWHeEVtkGAgg",
  "scope": "photos"
}
```

### OAuth Native Applications

ChromeCustomTabs

1. User clicks login
2. App Generates PKCE string calculates code challenge (hash)
3. builds url to oAuthServer inApp browser
4. OAuth Login (inApp Browser can share cookies)
5. OAuthServer redirects to app with authorization code
6. App makes call in backchannel with auth code and PKCE . OAuth verifies PkCE hash and gives access token

### Refresh tokens

scope=offline_access -> Authorization policies decide whether to give stored in a secure storage (application code cant
access ). Requires device biometric or password to access.

```
https://dev-45411978.okta.com/oauth2/default/v1/authorize?
  response_type=code&
  scope=offline_access+photos&
  client_id=0oarndnbmQUO7zu7d5d6&
  state=1234&
  redirect_uri=https://example-app.com/redirect&
  code_challenge=n_BdpJDoP3WeU2kVP8z0KzT3FEkr1hL0KRRVTf9SH0U&
  code_challenge_method=S256

```

Refresh Token Generation and Usage

```commandline
curl -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
  -d grant_type=authorization_code \
  -d redirect_uri=https://example-app.com/redirect \
  -d client_id=0oarndnbmQUO7zu7d5d6 \
  -d client_secret=A1bVR1d8u_J3K51cjzAYcTX_WiDiCed3hEqqCREo \
  -d code_verifier=f2e6fbac089f6bd4504109e5579c4622a3c4830236c4089add15d14a \
  -d code=09Myr2rDPFjrlZVE7rz4XPBY69dnWQZTdVVx0Xgt2D8
```

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkNMSWZRSXZvOHpMWnppM0w3MXRoT004TFRUMDhGQWUwMGNMY190eEFob28ub2FyMXM5eDBzblR4RDBGd0Y1ZDYiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjE0MTEwNTgsImV4cCI6MTYyMTQxNDY1OCwiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInBob3RvcyJdLCJzdWIiOiJhYmhpbmFuZDVhaUBnaXRodWIub2t0YWlkcCJ9.aTNZEjD53INaQQVpoktlt46sJYrJNU_AuPgG-InNj0OXeIfggBk9fDO6B5o92zCFHnY-xCjroRr2GTmom2srJJI3_llpiF1U7YR1oTnFPPbqek-LZiq22DON4ZBhjPIQakllF9cZzdXGV3u_3ha_OKPwoiuRVrNOuhyx13lp5LAM78WdnM7ImouCCZ0gqBgFSi9DeAbLDDNtYRzYC1-Ju_oe1i_2rVhCwZLP7UPUXKZmEMlgfcQ9Ib7lr4uG7XqnlEb6lNKXvS41qO5CWpoGTIKQH1yiQ3W_HOE3Y5aQ6ZJse-frEuNkiYCLlVvcARNnjF-EhHYmSSa0FYylIF6FXA",
  "scope": "offline_access photos",
  "refresh_token": "jm4U5rXWy0kBt9IjYgM7w8pLorJ9cc8gUhimNcsGAwU"
}
```

```commandline
curl -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
  -d grant_type=refresh_token \
  -d client_id=0oarndnbmQUO7zu7d5d6 \
  -d client_secret=A1bVR1d8u_J3K51cjzAYcTX_WiDiCed3hEqqCREo \
  -d refresh_token=jm4U5rXWy0kBt9IjYgM7w8pLorJ9cc8gUhimNcsGAwU
```

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmhGNTYzLTZpUjlJTmdQLV9LYzVkcnRuTGtkc3c5WjBuTmgxWWJpOFJsLVEub2FyMXM5eDBzblR4RDBGd0Y1ZDYiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjE0MTEzNTcsImV4cCI6MTYyMTQxNDk1NywiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInBob3RvcyJdLCJzdWIiOiJhYmhpbmFuZDVhaUBnaXRodWIub2t0YWlkcCJ9.YpZMiYbOVBHv4wsWVHSRW4R3ayk9mjLS8qAz8_REWpNHHXQ3laBYQlDtULHFi-lhbbpQKmLtV0Ta13hCv1GKVj6LCukyLYv09lx-bPPqaMcC0n44P3me6stdDeniPjpW9d6BnRnSquT3jPyiYaT2zrr3e25QGem3M5E1HDsXpcV_TYY07uZLkcAgdbyzwj8kTOcG-SGyBKlr851Aokh6qWPZNXtjIiD90ByQASTbVTGJU8vBJ82pD2_hsmli1P7nhX22jX_d2FtZu3fF6k2nvG02JjbJu1Ks8xSqXtJrnrOS_Wie4j7192SUuJYkxhayNWq_658bIEaqpq9bMdkveA",
  "scope": "offline_access photos",
  "refresh_token": "jm4U5rXWy0kBt9IjYgM7w8pLorJ9cc8gUhimNcsGAwU"
}
```

## OAUth for Single Page Applications

### Problem with browser Env

Noway to store secret in browser XSS

### OAUTH flow

```
https://dev-45411978.okta.com/oauth2/default/v1/authorize?
  response_type=code&
  scope=photos&
  client_id=0oasvrqyzNZAe0cJV5d6&
  state=402cff69c890d49b5ad6c7f49ab0aa94aa13802384a2aee226e7447f&
  redirect_uri=https://example-app.com/redirect&
  code_challenge=ezonrHJZulMwAfmjIVlRY0zRa0graNe6C9DKJxXJ3uU&
  code_challenge_method=S256
```

```commandline

curl -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
  -d grant_type=authorization_code \
  -d redirect_uri=https://example-app.com/redirect \
  -d client_id=0oasvrqyzNZAe0cJV5d6 \
  -d code_verifier=d1a52242993bd0e1bc13ee6c60da1ed4b6fcd2e0747638d4c0e6359c \
  -d code=fZ4GwOvFz14aC3ksYkwDD4B0y0x83fqb1djs5PU8FgA
```

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlEwemVkNDZhT1hwRGo5UEFBSkR2ZUJXZ0EwWXdpZnV5cjdLSVdUbHcxaGsiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjIxMTUwMDQsImV4cCI6MTYyMjExODYwNCwiY2lkIjoiMG9hc3dmdnNhU2F3eWFMVEs1ZDYiLCJzY3AiOlsicGhvdG9zIl0sInN1YiI6IjBvYXN3ZnZzYVNhd3lhTFRLNWQ2In0.EmDPqfn5KAtdCH7_gamEmxYAZkr2nZ3oyE83TlcAgYh-LRhhSD_Qz7gKUhjHmFGglviBsrkvO2egDDrNbtPrJ4g28DjaKDqHDXTFykNwHKYok2zNY0g9c3vifn3ksZDRs7eaqznivehVNd7HKGRGI1_fgCYQ8sP0rsKSe6Xc6aBTDHSyoNiT3NZmYycHSGU8Uzjx-DuMgrYqRM-kr1rpbqXVEUQlpqDP9btd6PTOttIXPFugzOMYNJhWd82FIu0ZUFp5FjAN2KnryJJjvo0u01fPIzon00tmPJE1vsoKPtgdbKD3jGe-6cDSHmidO_G5qhjEZSo4BMyJOuo65COJew",
  "scope": "photos"
}
```

## Client Credentials flow

```commandline

  curl -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
  -d grant_type=client_credentials \
  -d client_id=0oaswfvsaSawyaLTK5d6 \
  -d client_secret=UcOyv1bbJI9_Lc8zKOoa2MKnwDpB5GZMObmBvINm \
  -d scope=photos
```

## OpenID Connect

ID token only has identity details Access token gives api access

Ways of getting Id token:

1. Along with access token (add openid to list of scopes)
2. Implicit flow returns in redirect URL (front channel)
   Needs to be validated Has lesser info

some servers use apis to get user details

### Hybrid flows (response_type combinations)

code token code + token

### ID token flow

```commandline
https://dev-45411978.okta.com/oauth2/default/v1/authorize?
  response_type=code&
  scope=openid+profile+email&
  client_id=0oarndnbmQUO7zu7d5d6&
  state=aa7d3f69ecff3ac6e1e3bdd9d3809bf0935dbaa95d6f702b186613fb&
  redirect_uri=https://example-app.com/redirect&
  code_challenge=lsgudXL8IO7-EH71zNKTFOos8Z7iwfcfPNxh1I-SM54&
  code_challenge_method=S256
```

```commandline
curl -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
  -d grant_type=authorization_code \
  -d redirect_uri=https://example-app.com/redirect \
  -d client_id=0oarndnbmQUO7zu7d5d6 \
  -d client_secret=A1bVR1d8u_J3K51cjzAYcTX_WiDiCed3hEqqCREo \
  -d code_verifier=e3b6519effe45e4f02d7c056961abaab9e5b3b48f18cf7dfb916e457 \
  -d code=SIut_TjAbt6kXHVcGapt-21k9XYpKmUfJYc5F9DOdLs
```

## How api handles access tokens

* reference tokens
    * Pros:
        * Easy to Revoke
        * Hides sensitive info
    * Cons:
        * Must be stored
        * Requires db-lookup to validate
* self encoded (JsonWebToken)
    * Pros
        * No Storage required
        * No db-lookup
        * External OAuthServers can be used
    * Cons
        * All info is available to decode
        * No way to revoke before expiry (Authorization server has to handle)
        * Stale data

## API validation of access tokens

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkx0ZGlBb3ZXRWRBcjNZRHpabzg5bXpJTmw1dDRWMWJ6eE5hSnZHWHdGS00ub2FyMXZkYXY5emRYcWhuWFk1ZDYiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjIxMTM2MTgsImV4cCI6MTYyMjExNzIxOCwiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInBob3RvcyJdLCJzdWIiOiJhYmhpbmFuZDVhaUBnaXRodWIub2t0YWlkcCJ9.Y8o4ZjumTRuNzjoG3hmH6lE9mrM25IYS6ncb9CillpJPv-l2BeiE7asoBM7SgjXyhJSNGPtK2iOy8XWos9_SQBcKD6MGDUpNjhtWzyzbQrs5a1y0qOkGCr6CvELIYtPI2F970BQX0E-3c-c7At1745rpBNBC_wiqhSMe_30wFH4MVY8Skcf8lPZAgQAjv2KLtcqfOopg_FJr0Rxq7oUeEB2XarF2LQjPM-ZI0lbJX22aB7TWJ94BegrHV3w22Bj7F6qJyjmpcPkNZwwZ46JXKZLp72b0pJqLZ1WF8N4y2pgXzvelLVd86hWHkvgz4dQ67icVHW6YBKk7_gXuDOk9jQ",
  "scope": "offline_access photos",
  "refresh_token": "j5pd3uSuv4K5gwj5-3XIJuy9d-I8odmvV0-TsyI7OmY"
}
```

```commandline
curl https://dev-45411978.okta.com/oauth2/default/v1/introspect \
  -d client_id=0oatncjmcWNG5FcES5d6 \
  -d client_secret=Hub8jd_hieus3gpirctf4ElsMtTaiEahu_E6LPjM \
  -d token=eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlp1RmVNUVc1cENsa0RpVnIyUnAyRURhMmM1eDF0WTRxNHBwcHJONFdsVVkub2FyMXZjd24yd0tWeldKbGc1ZDYiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjIxMTQ4MDYsImV4cCI6MTYyMjExODQwNiwiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJvZmZsaW5lX2FjY2VzcyIsInBob3RvcyJdLCJzdWIiOiJhYmhpbmFuZDVhaUBnaXRodWIub2t0YWlkcCJ9.R8sfrgXgbxXS-eYjQYN7fRdKNtgWYsnT2f0rfvgE8bYcGiMwYw_cMKk6ONpFJqXiv0YEus31YR1ni0uUQ8dYMG9YbwamB2VenpzfiNymO_Tkjd4qKTQWzsQPb9eTmAg4cCRUTiYFb2bAeiOylLAEa5Ec6h3Qff7rkqzylPaHjgijEqy1kZbrIScChkqPbnlVEHUJsOhDLNr7dAUFkpzxs1bhS120IdBmLoTzYEzTyeRQArQn4pUDZLQvREmakJyh8DX8NU7DZRL8tLUvYh7RcNg7IENR06Ep3wRn507EioBjwiyMOfmSy6RdsSZiVQRC3SvZb2t9S3Nfl5GIQXRoxQ
```

```json
{
  "active": true,
  "scope": "offline_access photos",
  "username": "abhinand5ai@github.oktaidp",
  "exp": 1622118406,
  "iat": 1622114806,
  "sub": "abhinand5ai@github.oktaidp",
  "aud": "api://default",
  "iss": "https://dev-45411978.okta.com/oauth2/default",
  "jti": "AT.ZuFeMQW5pClkDiVr2Rp2EDa2c5x1tY4q4ppprN4WlUY.oar1vcwn2wKVzWJlg5d6",
  "token_type": "Bearer",
  "client_id": "0oarndnbmQUO7zu7d5d6",
  "uid": "00urkvenezW6lh7FJ5d6"
}
```

If inactive

```json
{
  "active": false
}
```

### JWT Access token

#### JWT Profile for OAuth2 Access tokens

### Token Lifetimes

Shorter token lifetime ---> more security Longer token lifetimes ---> Improve experience

### Revocation endpoint

```commandline
curl https://dev-7533118.okta.com/oauth2/default/v1/revoke \
  -d client_id={YOUR_CLIENT_ID} \
  -d client_secret={YOUR_CLIENT_SECRET} \
  -d token={ACCESS_TOKEN}
```

Always returns 200

make another inspection call to check if still active If you’re having trouble here double check that the credentials
you’re using in the revocation request belong to the same client that you used to get the access token.

```commandline
https://dev-45411978.okta.com/oauth2/default/v1/authorize?
  response_type=code&
  scope=photos+photos:create+photos:delete&
  client_id=0oarndnbmQUO7zu7d5d6&
  state=1234&
  redirect_uri=https://example-app.com/redirect&
  code_challenge=n_BdpJDoP3WeU2kVP8z0KzT3FEkr1hL0KRRVTf9SH0U&
  code_challenge_method=S256
```

```commandline
curl -k -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
  -d grant_type=authorization_code \
  -d redirect_uri=https://example-app.com/redirect \
  -d client_id=0oarndnbmQUO7zu7d5d6 \
  -d client_secret=A1bVR1d8u_J3K51cjzAYcTX_WiDiCed3hEqqCREo \
  -d code_verifier=f2e6fbac089f6bd4504109e5579c4622a3c4830236c4089add15d14a \
  -d code=TZ8Cm-PGFEgauaR6OZfM-KB8uqFCkJEjq7J-2we1RWM
```

```json
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlRjdGp6allTbmRsN0RvR2xfOFY5WU5WWllNc0hMWURkTjJCU1FfbTE0S1EiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjIxMzEwODcsImV4cCI6MTYyMjEzNDY4NywiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJwaG90b3MiLCJwaG90b3M6Y3JlYXRlIiwicGhvdG9zOmRlbGV0ZSJdLCJzdWIiOiJhYmhpbmFuZDVhaUBnaXRodWIub2t0YWlkcCJ9.CN5xD52TtK_pBg5Cx2D3NcjNOdpT6YzGOTdffQW1u7oteD3KYYob06ztpXJhXJP0CmP51GAwunE9tLjKXzXeaWuT1k9iEi0dkVyVE2LM9nd7819A86xE3rr2OG-OKb1uL8u53658lipC51Jrwf07XIYdb2Ojrgbsy1Fn831xFbwRyRLoD8eYHWJWbn9j3mPa27nvYUITITrvAkBuU_hu-bsxV9fCWLgmS5KNXguwlnP0iO1zcGqA2bdfeXIXeWD1Z83FJps0uf_i-UxXbOTqMusXgG0JGKB-4F1F97Wnk2LeUhD7EO3usYdV6Tnt17n1PMTTmucoOOT3SHGgvIww3A",
  "scope": "photos photos:create photos:delete"
}
```

```commandline
curl -k https://dev-45411978.okta.com/oauth2/default/v1/introspect \
  -d client_id=0oatncjmcWNG5FcES5d6 \
  -d client_secret=Hub8jd_hieus3gpirctf4ElsMtTaiEahu_E6LPjM \
  -d token=eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULlRjdGp6allTbmRsN0RvR2xfOFY5WU5WWllNc0hMWURkTjJCU1FfbTE0S1EiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjIxMzEwODcsImV4cCI6MTYyMjEzNDY4NywiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJwaG90b3MiLCJwaG90b3M6Y3JlYXRlIiwicGhvdG9zOmRlbGV0ZSJdLCJzdWIiOiJhYmhpbmFuZDVhaUBnaXRodWIub2t0YWlkcCJ9.CN5xD52TtK_pBg5Cx2D3NcjNOdpT6YzGOTdffQW1u7oteD3KYYob06ztpXJhXJP0CmP51GAwunE9tLjKXzXeaWuT1k9iEi0dkVyVE2LM9nd7819A86xE3rr2OG-OKb1uL8u53658lipC51Jrwf07XIYdb2Ojrgbsy1Fn831xFbwRyRLoD8eYHWJWbn9j3mPa27nvYUITITrvAkBuU_hu-bsxV9fCWLgmS5KNXguwlnP0iO1zcGqA2bdfeXIXeWD1Z83FJps0uf_i-UxXbOTqMusXgG0JGKB-4F1F97Wnk2LeUhD7EO3usYdV6Tnt17n1PMTTmucoOOT3SHGgvIww3A

```

```json
{
  "active": true,
  "scope": "photos photos:create photos:delete",
  "username": "abhinand5ai@github.oktaidp",
  "exp": 1622134687,
  "iat": 1622131087,
  "sub": "abhinand5ai@github.oktaidp",
  "aud": "api://default",
  "iss": "https://dev-45411978.okta.com/oauth2/default",
  "jti": "AT.TctjzjYSndl7DoGl_8V9YNVZYMsHLYDdN2BSQ_m14KQ",
  "token_type": "Bearer",
  "client_id": "0oarndnbmQUO7zu7d5d6",
  "uid": "00urkvenezW6lh7FJ5d6"
}
```