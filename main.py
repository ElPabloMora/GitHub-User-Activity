import argparse
from api_github import get_activity,get_request

def main():
    parser = argparse.ArgumentParser(description="GitHub User Activity")
    subparser = parser.add_subparsers(dest='command', required= True)
    
    get_user = subparser.add_parser('get', help='get the github user')
    get_user.add_argument('user', type=str , help='Username')
    
    args = parser.parse_args()
    
    if args.command in ['get']:
        activities = get_request(args.user)
        if not activities:
            return
        user_activities = get_activity(activities)
        print('Output:')
        print('\n'.join(user_activities))
    
if __name__ == "__main__":
    main()