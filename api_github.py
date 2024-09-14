from urllib.request import Request, urlopen
import json

#This function makes a get request to the API
def get_request(user):
    
    url = f'https://api.github.com/users/{user}/events'
    
    request = Request(url)
    with urlopen(request) as response:
        return json.loads(response.read().decode())

#this function does is obtain the activities by parameter and then classify them with the if
def get_activity(activities):
    
    user_activities = []
    for activity in activities:
        
        user = activity['actor']['login']
        repo = activity['repo']['name']
        
        if activity['type'] == 'CreateEvent':
            user_activities.append(f'{user} create repository : {repo}')
        elif activity['type'] == 'PushEvent':
            user_activities.append(f'{user} commits {len(activity['payload']['commits'])} to : {repo}')
        elif activity['type'] == 'WatchEvent':
            user_activities.append(f'{user} looked at the repository: {repo}')
        elif activity['type'] == 'PublicEvent':
            user_activities.append(f'{user} made repository : {repo} public')

    return user_activities
