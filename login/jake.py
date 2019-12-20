from login.driver.casbin import access_driver

res = access_driver.enforce("viewer", "/test", "GET")
print(res)
