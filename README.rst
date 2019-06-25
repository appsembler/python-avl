====================================
Appsembler Virtual Labs API Bindings
====================================

Python bindings for the Appsembler API.


Usage 
=======

Set your token and endpoint by creating a `.env` file in the 
root directory, populating it with the following: 

.. code: bash 

    AVL_DOMAIN='https://yourAVLDashboard.domain.com'
    AVL_API_TOKEN='yourToken'

Update the planned expiration time of a lab:

.. code: python

    from avl import Lab
    from datetime import datetime

    lab = Lab(lab_id)

    expiration_time = datetime.today() + datetime.timedelta(days=2)

    data = {
        'id': '<yourLabID>',
        'expiration_time': expiration_time 
    }
    lab.patch(data)


Features
==========

* TODO

TODO 
=====

* Cover the following endpoints
  * '/isc/dashboard/userprojectdeployments/' GET
  * '/isc/dashboard/userprojectdeployments/delete_user_deployments/' POST (should be patch?)
  * '/isc/newdeploy/' POST (with project Token)

Credits
========

* package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
