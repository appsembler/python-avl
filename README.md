# Appsembler Virtual Labs API Bindings


Python bindings for the Appsembler API.


## Install

1. Clone this repo
2. `git fetch; git checkout -b bdant/patch origin/bdant/patch`
3. `pip install -r requirements_dev.txt`

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

For more on engaging with the response object, see: 
https://2.python-requests.org/en/master/api/#requests.Response


## TODO 

* Cover the following endpoints
  * '/isc/dashboard/userprojectdeployments/' GET
  * '/isc/dashboard/userprojectdeployments/delete_user_deployments/' POST (should be patch?)
  * '/isc/newdeploy/' POST (with project Token)
