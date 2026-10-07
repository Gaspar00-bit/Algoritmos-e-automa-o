server=[{
"hostname":"localhost",
"ip":"192.168.299.0",
"port":3360,
"status":"online"


},
{
"hostname":"localhost",
"ip":"200.168.299.0",
"port":4454,
"status":"off"


}]
for serv in server:
    print(serv["ip"],serv["status"])