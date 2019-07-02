# Appsembler Virtual Labs API Bindings


Python bindings for the Appsembler API.


## Install

- Clone this repo
- Create a virtualenv, if that's how you normally manage your Python packages
- `$ git fetch; git checkout -b bdant/patch origin/bdant/patch`
- `$ pip install -r requirements_dev.txt`
- `$ chmod 700 ./add2path.sh`
- `$ ./add2path.sh`  # Add this repo to your Python path.
- `$make test`  # Run the tests.

## Usage 

Copy the env file:

```
$ cp env.example .env
```

Modify the token and domain in the .env file:

```
AVL_DOMAIN='https://yourAVLDashboard.domain.com'
AVL_API_TOKEN='yourToken'
```

Update the planned expiration time of a lab:


```
from avl import Lab
from datetime import datetime

lab = Lab(lab_id)

planned_expiration_time = datetime.today() + datetime.timedelta(days=2)

data = {
    'id': '<yourLabID>',
    'planned_expiration_time': planned_expiration_time 
}

lab = lab.patch(data)

if lab.response.ok:  # i.e., 20x
    do_something()
else:
    do_something_else()
```

For more on engaging with the `Lab.response` object, see: 
https://2.python-requests.org/en/master/api/#requests.Response. It's 
simply a copy of `request.Response`.


## TODO 

* Cover the following endpoints
  * '/isc/dashboard/userprojectdeployments/' GET
  * '/isc/dashboard/userprojectdeployments/delete_user_deployments/' POST (should be patch?)
  * '/isc/newdeploy/' POST (with project Token)
* Install the requirements upon `setup.py install`, etc.
