import requests
import os
import sys
import json
import argparse

def api_call():
    """
       Returns 50 Users from randomuser.me
    """
    response = requests.get("https://randomuser.me/api?results=50") 
    response.raise_for_status() # Check if the response is successful
    return response.json()["results"]

def get_timezone_users(users, timezone):
    """
       Return all users in the timezone
    """
    users_in_timezone= [
            user for user in users if user["location"]["timezone"]["offset"] == timezone
            ]            
    print(f"{len(users_in_timezone)}/{len(users)} users in timezone {timezone}\n")
    return users_in_timezone

def format_users(users):
    """
       Format and print users in the format
       'Title FirstName LastName'
    """
    for user in users:
        name = user["name"]
        print(f"{name['title']} {name['first']} {name['last']}")

def get_users(users, timezone=None):
    """
       Prints Users
    """
    if timezone:
        users_to_print= get_timezone_users(users, timezone)
        
    else:
        users_to_print = users

    # Print each user's name in the specified format
    format_users(users_to_print)

def main():
    parser = argparse.ArgumentParser(description="List users optionally filtered by timezone.")
    parser.add_argument("-t", "--timezone", help="Filter users by timezone (e.g., +10:00)")
    args = parser.parse_args()

    try:
        users = api_call()
        get_users(users, timezone=args.timezone)
    except requests.RequestException as e:
        print(f"Failed to fetch users: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
