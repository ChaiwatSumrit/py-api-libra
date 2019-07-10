# py-api-libra
py-api-libra

## Function 
- registerAccount
- mintMonnyAccount
- transfer
- inquiryBalance
- comming zoon***inquiryTransaction***

# Requiry python3 & pip3
https://vitux.com/install-python3-on-ubuntu-and-set-up-a-virtual-programming-environment/
https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/


# Install Lib

```
pip3 install flask flask-jsonpify flask-sqlalchemy flask-restful
```

## ERROR

```
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/werkzeug'
Consider using the `--user` option or check the permissions.
```

```
sudo pip3 install flask flask-jsonpify flask-sqlalchemy flask-restful
#RO
pip3 install flask flask-jsonpify flask-sqlalchemy flask-restful --user
```


# Start API

```
cd py-api-libra

python3 py-app.py 
```
# Test by PostMan

import ***py-api-libra.postman_collection.json*** to Postman
