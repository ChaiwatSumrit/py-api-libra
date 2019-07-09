# py-api-libra
py-api-libra

## Function 
- registerAccount
- mintMonnyAccount
- transfer
- inquiryBalance
- comming zoon***inquiryTransaction***

# Requiry python3 & pip3
http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/
```
sudo apt install python3-pip

sudo pip3 install pylibra
```

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

python py-app.py 
```
# Test by PostMan

import ***py-api-libra.postman_collection.json*** to Postman
