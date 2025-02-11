
import requests
import json
from datetime import datetime
from connectors.core.connector import get_logger, ConnectorError


logger = get_logger('azure-purview')

class AzurePurview(object):
    def __init__(self, config):
        self.base_url = config.get("resource")
        if self.base_url.startswith('https://') or self.base_url.startswith('http://'):
            self.base_url = self.base_url.strip('/')
        else:
            self.base_url = 'https://{0}'.format(self.base_url.strip('/'))
        self.client_id = config.get("client_id")
        self.tetnat_id = config.get("tenant_id")
        self.client_secret = config.get("client_secret")
        self.grant_type = "client_credentials"
        self.resource = "https://purview.azure.net"
        self.verify_ssl = config.get("verify_ssl")
        self.error_msg = {
            400: 'The parameters are invalid.',
            401: 'Invalid credentials were provided',
            403: 'Access Denied',
            404: 'The requested resource was not found',
            409: 'The requested settings conflict with the current settings',
            410: 'Cannot find the specified object',
            422: 'Unable to process the request because system lockdown is currently disabled, or some file fingerprint lists or file names were already assigned',
            423: 'The resource to update is locked and cannot be updated',
            500: 'Internal Server Error',
            503: 'Service Unavailable',
            'time_out': 'The request timed out while trying to connect to the remote server',
            'ssl_error': 'SSL certificate validation failed'}

def get_token(config):
        try:
            payload = {
                "grant_type": "client_credentials",
                "client_id": config.get("client_id"),
                "client_secret": config.get("client_secret"),
                "resource":  config.get("resource")
                }
            url = f"https://login.microsoftonline.com/{config.get('tenant_id')}/oauth2/token"
            response = requests.post(url, data=payload)
            response.raise_for_status()
            token = response.json().get("access_token")
            return token
        except Exception as e:
            print(f"Error getting token: {e}")
            return None

       

def build_payload(self, params):
        result = {k: v for k, v in params.items() if v is not None and v != ''}
        return result



def get_Alerts(config, params):
    response = get_token(config)
    return response


def update_Alerts(config, params):
    response=0
    return response

def get_all_Alerts(config, params):
    response=0
    return response


def check_health_ext(config):
    try:
        response = get_token(config)
#        token = response.json().get("access_token")
        token = response
        if token:
            return True
    except Exception as err:
        logger.error("{0}".format(str(err)))
        raise ConnectorError(str(err))




operations = {
    'get_Alerts': get_Alerts,
    'update_Alerts': update_Alerts,
    'get_all_Alerts': get_all_Alerts
}

