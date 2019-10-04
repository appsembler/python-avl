[![Build Status](https://travis-ci.org/appsembler/python-avl.svg?branch=bdant%2Fpatch)](https://travis-ci.org/appsembler/python-avl)

# Appsembler Virtual Labs API Bindings


Python bindings for the Appsembler API.

## Supported Python versions

- Python 3.5, 3.6

## Install

- Clone this repo
- Create a virtualenv, if that's how you normally manage your Python packages

## Option 1: Install via cloning the repo

Fetch the repo and pip install the dependancies:

```
$ git fetch; git checkout -b bdant/patch origin/bdant/patch
$ pip install -r requirements_dev.txt
```

You'll then need to add the the directory to your path. On \*nix environments,
run the helper script included in this repo:

```
$ chmod 700 ./add2path.sh
$ ./add2path.sh
```

## Option 2: Install with `pip`

Install the package in editable mode, which will allow you to edit the code 
while also treating it like an installed package:

```
pip install -e git+git@github.com:appsembler/python-avl@bdant/patch#egg=avl .
```

## Configure the package for your domain

Copy the env file:

```
$ cp env.example .env
```

Modify the token and domain in the .env file:

```
AVL_DOMAIN='https://yourAVLDashboard.domain.com'
AVL_API_TOKEN='yourToken'
```

## Usage 

Update the planned expiration time of a lab:


```
from avl import Lab
from datetime import datetime, timedelta

lab = Lab(lab_id)

planned_expiration_time = datetime.today() + timedelta(days=2)

data = {
    'pk': lab.pk,
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
