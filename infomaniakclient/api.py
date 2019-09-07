import requests
import json

class Action:

    SCHEDULE      = "schedule"
    UNSCHEDULE    = "unschedule"
    SEND          = "send"
    TEST          = "test"
    STATISTICS    = "statistics"

    LISTCONTACT   = "contact"
    MANAGECONTACT = "managecontact"
    IMPORTCONTACT = "importcontact"
    
    DELETE        = "delete"
    UNSUBSCRIBE   = "unsub"

class Client:
    """Infomaniak Newsletter API client"""

    BASE = 'https://newsletter.infomaniak.com/api/v1/public'

    headers = {'Content-type': 'Content-Type: application/json'}
    timeout = 5

    """Client.resource"""
    CAMPAIGN = 'campaign'
    CONTACT = 'contact'
    MAILINGLIST = 'mailinglist'
    TASK = 'task'
    CREDIT = 'credit'
    
    def __init__(self, API_KEY: str , API_SECRET: str, headers: dict = None, timeout: int = None ):
        self.timeout = timeout
        self.API_KEY = API_KEY
        self.API_SECRET = API_SECRET

    def __request(self, method: str, resource, args: dict = {}) -> requests:
        """Builds the request which is then passed to the 'requests' module to get the API"""
        uri = self.__buildURL(resource, args)

        collection = 'params' if method is 'GET' else 'data'
        paramsVar = json.dumps(args[collection][0]) if 'params' in args else {}
        dataVar = json.dumps(args[collection][0]) if 'data' in args else {}

        try:
            if collection == 'data':
                r = getattr(requests, method.lower())(uri, 
                auth=(self.API_KEY, self.API_SECRET), 
                data = dataVar, 
                headers = self.headers, 
                timeout = self.timeout)
            else:
                r = getattr(requests, method.lower())(uri, 
                auth=(self.API_KEY, self.API_SECRET), 
                params = paramsVar, 
                headers = self.headers, 
                timeout = self.timeout)

            r.raise_for_status()
            return r

        except requests.exceptions.Timeout as e:
            print(e)
        except requests.exceptions.RequestException as e:
            print(e, r.json())
            
    def __buildURL(self, resource, args: dict = {}) -> str:
        """Builds the URL to use in the 'requests' request""" 
        url = [self.BASE, resource, str(args['id']) if 'id' in args else '', str(args['action']) if 'action' in args else ''] 
        url = [el for el in url if el != '']
        return '/'.join(url)

    def get(self, resource, args: dict = {}) -> requests:
        """Makes a GET request to the API"""
        return self.__request('GET', resource, args) 
    
    def post(self, resource, args: dict = {}) -> requests:
        """Makes a POST request to the API"""
        return self.__request('POST', resource, args) 

    def put(self, resource, args: dict = {}) -> requests:
        """Makes a PUT request to the API"""
        return self.__request('PUT', resource, args) 

    def delete(self, resource, args: dict = {}) -> requests:
        """Makes a DELETE request to the API"""
        return self.__request('DELETE', resource, args) 
    
    def ping(self):
        """Pings the API's server"""
        return self.get('ping')     