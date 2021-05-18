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
APP creates PKCE code verifier 43 - 128 ---> Public hash -> Construct link and send to OAuth Server
authorization code injection

```
https://dev-45411978.okta.com/oauth2/default/v1/authorize? response_type=code& scope=photos&
client_id=0oarndnbmQUO7zu7d5d6& state=6d5d482f0005cc4ba0af9122e1bf7803675e927827ce419f0f0f5922&
redirect_uri=https://example-app.com/redirect&
code_challenge=n_BdpJDoP3WeU2kVP8z0KzT3FEkr1hL0KRRVTf9SH0U& code_challenge_method=S256
````
Use the Authorization Code from the redirected url and construct token request
```
curl -X POST https://dev-45411978.okta.com/oauth2/default/v1/token \
-d grant_type=authorization_code \
-d redirect_uri=https://example-app.com/redirect \
-d client_id=0oarndnbmQUO7zu7d5d6 \
-d client_secret=A1bVR1d8u_J3K51cjzAYcTX_WiDiCed3hEqqCREo \
-d code_verifier=f2e6fbac089f6bd4504109e5579c4622a3c4830236c4089add15d14a \
-d code=93k58TFomgz05Fg0LkyBD9CCb4-tqGlAYb0HW0p1CTM
```
Get the access token as response
```
    {"token_type":"Bearer","expires_in":3600,"access_token":"eyJraWQiOiJqX3N1NmZnY2xnZkxOOTF6YUZrNVMtV1ByMDNQcTR1cjNXc21la2RmOVdNIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmpoU1hwRl9sLVkzS3pfbDAzdEFrZzY0ZG9SR3dGa2IydTIzcmtCR0hYS0EiLCJpc3MiOiJodHRwczovL2Rldi00NTQxMTk3OC5va3RhLmNvbS9vYXV0aDIvZGVmYXVsdCIsImF1ZCI6ImFwaTovL2RlZmF1bHQiLCJpYXQiOjE2MjEzMjk0ODgsImV4cCI6MTYyMTMzMzA4OCwiY2lkIjoiMG9hcm5kbmJtUVVPN3p1N2Q1ZDYiLCJ1aWQiOiIwMHVya3ZlbmV6VzZsaDdGSjVkNiIsInNjcCI6WyJwaG90b3MiXSwic3ViIjoiYWJoaW5hbmQ1YWlAZ2l0aHViLm9rdGFpZHAifQ.SdxPzizP4sMJw743FcaNgoFIOwjFVIz0Yb8P4D333uUvOGppM7WsABcxtUJ9RMzti5VXBfU4zL5XdxEFqOm4iVtzxkaSAeANaB9DEyBo-UwXvdL9vVz-szGAEBEOmuU6AWoiKScfBpXSgj6j3RMSReSUviiMN86-vW_yweQvR2txfqap3iRC45OgMMowMTGx1rSrqhyHEWMGt2QsYkATQzItrd9JmidAAckQ8dSqHVhYSKUYDFJAVNMBtVrwVHUUFub9jXvmFGEvEyHSU-kDzBdcXAzgBkjxAQyDSwB83-6h-cgxg6Az1F8q6YWFBuAWAFOxJA9dqzgWHeEVtkGAgg"
    ,"scope":"photos"}
```