# pip install infomaniakclient

from infomaniakclient import Client
from infomaniakclient import Action

def __main__():

    """ Initialize the Class, timeout is optional, but set by default at 5 sec. """
    newsletter = Client('API_KEY', 'API_SECRET', timeout = 5)
    
    #Ping
    r = newsletter.ping()
    print(r)

    """ CreateCampaign """
    args = {
        'data': [{
            'subject' : '2019-12-25 13:37:00',
            'email_from_name' : 'Foo',
            'lang' : 'en',
            'email_from_addr': 'Bar',
            'content': 'content',
            'mailinglistIds' : [1]
        }]
    }
    #r = newsletter.post(API.CAMPAIGN, args = args)

    """ DeleteCampaign """
    args = {'id': 1}
    #r = newsletter.delete(API.CAMPAIGN, args)

    """ GetCampaign """
    args = {'id': 1}
    #r = newsletter.get(API.CAMPAIGN, args)   

    """ GetCampaigns """
    args = {'page': 2}
    #r = newsletter.get(API.CAMPAIGN)  

    """ GetScheduleCampaign """
    args = {'action': Action.SCHEDULE, 'id': 1}
    #r = newsletter.get(API.CAMPAIGN, args)    
    
    """ ScheduleCampaign """
    args = {
        'action': Action.SCHEDULE, 
        'id': 1, 
        'data': [{
            'scheduled_at': '2019-09-04 23:10:00'
        }]
    }
    #r = newsletter.post(API.CAMPAIGN, args) 

    """ SendCampaign, not possible to send an already scheduled campaign """
    args = {'action': Action.SEND, 'id': 1}
    #r = newsletter.post(API.CAMPAIGN, args)    

    """ TestCampaign """
    args = {
        'action': Action.TEST, 
        'id': 1,
        'data': [{
            'email': 'email@mail.com'
        }]
    }
    #r = newsletter.post(API.CAMPAIGN, args) 

    """ UnscheduleCampaign """
    args = {'action': Action.UNSCHEDULE, 'id': 1}
    #r = newsletter.post(API.CAMPAIGN, args)   

    """ UpdateCampaign """
    args = {
        'id': 1,
        'data': [{
            'subject': 'updated subject'
        }]
    }
    #r = newsletter.put(API.CAMPAIGN, args)   

    """ GetCampaignStatistics """    
    args = {'action': Action.STATISTICS, 'id': 1}
    #r = newsletter.get(API.CAMPAIGN, args)

    """ DeleteContact """
    args = {'id': 1}
    #r = newsletter.delete(API.CONTACT, args)

    """ GetContact """
    args = {'id': 1}
    #r = newsletter.get(API.CONTACT, args)

    """ UpdateContact """
    args = {
        'id': 1, 
        'data': [{
            'firstname': 'firstname'
        }]
    }
    #r = newsletter.put(API.CONTACT, args)

    """ CreateMailinglist """
    args = {'data': [{ 'name' : 'foo' }] }
    #r = newsletter.post(API.MAILINGLIST, args)

    """ updateMailinglist """
    args = {'id': 1, 'data': [{ 'name' : 'bar' }] }
    #r = newsletter.put(API.MAILINGLIST, args)

    """ DeleteMailinglist """
    args = {'id': 1}
    #r = newsletter.delete(API.MAILINGLIST, args)

    """ GetContacts """
    args = {'action': Action.LISTCONTACT, 'id': 1}
    #r = newsletter.get(API.MAILINGLIST, args)

    """ GetMailinglist """
    args = {'id': 1}
    #r = newsletter.get(API.MAILINGLIST, args)

    """ GetMailinglists """
    #r = newsletter.get(API.MAILINGLIST, args)

    """ ImportContact """
    args = {
        'action': Action.IMPORTCONTACT,
        'id': 1, 
        'data': [{
            'contacts': {
                'email' : 'newmail@123.com',
                'email' : '2newmail@123.com',
                'email' : '2newmail@123.com'
            }
        }]
    }
    #r = newsletter.post(API.MAILINGLIST, args)
    
    """ ManageContact """
    args = {
        'action': Action.MANAGECONTACT,
        'id': 1, 
        'data': [{
            'email': '2newmail@123.com',
            'status':  Action.DELETE
        }]
    }
    #r = newsletter.post(API.MAILINGLIST, args)

    """ GetTask """
    args = {'id': 1}
    #r = newsletter.get(API.TASK, args)

    """ GetCredit """
    #r = newsletter.get(API.CREDIT)

if __name__ == "__main__":
    __main__()