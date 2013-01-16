import requests
import json

import data


class Github(object):
    def __init__(self, auth=None):
        self.auth = auth

    def requests_wrapper(self, url):
        r = requests.get(url, auth=self.auth)
        data = json.loads(r.content)
        return data


    def organization_members(self, org_name):
        members = self.requests_wrapper('https://api.github.com/orgs/%s/members' % org_name)
        return map(data.user_info, members)


    def user_activity(self, user_name):
        events = self.requests_wrapper('https://api.github.com/users/%s/events' % user_name)
        return map(data.event_info, events)



if __name__ == "__main__":
    g = Github()
    users = g.organization_members('FOSSRIT')
    print(users[0]['login'])
    print(g.user_activity(users[0]['login']))
