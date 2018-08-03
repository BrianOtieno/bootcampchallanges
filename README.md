
# BADGES

[![Build Status](https://travis-ci.org/BrianOtieno/bootcampchallanges.svg?branch=challange3)](https://travis-ci.org/BrianOtieno/bootcampchallanges)
[![Coverage Status](https://coveralls.io/repos/github/BrianOtieno/bootcampchallanges/badge.svg?branch=challange2)](https://coveralls.io/github/BrianOtieno/bootcampchallanges?branch=challange2)


# DIARY API

# What the API Does

This is an API endpoint application consumable with applications like Postman of Insomnia. It automatically creates necessary tables (users, diary, API version). You can create users, add events, edit events and delete events.

# Try It Out!
Click <a href="https://bootcmpdiary.docs.apiary.io/#">Here </a> To try out the API

# Installation
Install modules in the requirements.txt file

Run the diary.py file. This will generate the relations necessary in the setting up of the database.

# Unit Testing
The test file is test_diary.

The command below runs the test:

Test run command: python -m unit test test_diary

The Endpoints in this API
GET "/api/v1" - The API home page

POST /api/v1/register : Registers the user

POST /api/v1/login : Users can login here

POST /api/v1/entries : Logged in users can make posts

GET /api/v1/entries : Returns all the diary entries

GET /api/v1/entries/<int:entry_id> :Returns a specific diary entry

PUT /api/v1/entries/<int:entry_id> : Modifies Entries

DELETE /api/v1/entries/<int:entry_id> : Deletes the requested diary entry
