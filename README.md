# tzuser
## Description
tzuser.py is a Python script that retrieves user data from the Random User API and displays user names. You can optionally filter users by timezone.

## Usage
Without Timezone
Lists all users without any summary line.

`python3 tzusers.py` # Tested with python 3.12
With Timezone
Filters users by the specified timezone offset (e.g., +10:00) and displays a summary line indicating the count of users in that timezone.

`python list_users.py -t +10:00`
Example Output
```
2/50 users in timezone +10:00

Mr John Doe
Ms Jane Smith
```

## Requirements
Python 3.12
requests library (install with pip install requests)

## Notes
This script uses the [Random User API](https://randomuser.me) to fetch user data.
