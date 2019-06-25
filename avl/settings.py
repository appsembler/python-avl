from os import environ

from dotenv.main import load_dotenv


# dotenv
load_dotenv(verbose=True)


def _fix_booleans(var):
    FALSIES = ['False', 'false', '0', 0, 'No', 'no']
    TRUTHIES = ['True', 'true', '1', 1, 'Yes', 'yes']

    if var in FALSIES:
        return False
    if var in TRUTHIES:
        return True
    else:
        return var


def get_env_variable(var_name, default=None):
    """ Get the environment variable or return exception """
    if default is not None:
        return _fix_booleans(environ.get(var_name, default))
    try:
        return _fix_booleans(environ[var_name])
    except KeyError:
        error_msg = "Please set the %s environment variable" % var_name
        raise KeyError(error_msg)


AVL_DOMAIN = get_env_variable("AVL_DOMAIN")
AVL_API_TOKEN = get_env_variable("AVL_API_TOKEN")
