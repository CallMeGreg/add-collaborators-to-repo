from gh import client
import sys
import os
import logging

# Get Arguments
list_of_users = sys.argv[1]
target_repo = sys.argv[2]
permission = sys.argv[3]
owner = sys.argv[4]

full_repo = owner + '/' + target_repo

# Get Environment Variables
admin_token = os.environ.get('GITHUB_TOKEN')

# Setup client
admin_client = client.Client(admin_token)

def translate_permission(permission):
    if permission == "write":
        return "push"
    elif permission == "read":
        return "pull"
    elif permission == "admin":
        return "admin"
    elif permission == "maintain":
        return "maintain"
    elif permission == "triage":
        return "triage"
    else:
        e = f"Invalid permission: {permission}"
        logging.error(e)
        raise Exception(e)

def get_attendees(list_of_users):
    attendees = []
    list_of_users = list_of_users.split(',')
    for user in list_of_users:
        attendees.append(user.strip())
    return attendees

def add_collaborators_to_repo(attendees, full_repo, permission):
    for attendee in attendees:
        try:
            admin_client.repo.add_collaborator(full_repo, attendee, permission)
        except Exception as e:
            logging.error(e)
            pass

def main():

    logging.info("Starting collaborator automation...")
    
    # split and trim list of users:
    attendees = get_attendees(list_of_users)

    #translate permission:
    permission_to_set = translate_permission(permission)

    logging.info(f"Number of users to be added: " + str(len(attendees)))
    logging.info(f"Target repo: {full_repo}")
    logging.info(f"Permission: {permission_to_set}")
    
    # invite attendees to repo
    error_count = 0
    for attendee in attendees:
        try:
            admin_client.repo.add_collaborator(full_repo, attendee, permission)
        except Exception as e:
            logging.error(e)
            error_count += 1
            pass
    logging.info(f"Number of errors while adding users: {error_count}")

if __name__ == "__main__":
    main()