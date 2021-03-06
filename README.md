[![Build Status](https://travis-ci.org/betsybeth/betsybeth.github.io.svg?branch=flask-develop)](https://travis-ci.org/betsybeth/betsybeth.github.io)
[![Coverage Status](https://coveralls.io/repos/github/betsybeth/betsybeth.github.io/badge.svg?branch=develop)](https://coveralls.io/github/betsybeth/betsybeth.github.io?branch=develop)
# Bright Event
### Introduction
Bright Events application lets you create and manage events.

[click here to access bright events github pages][2]

#### Getting Started
To start using the Bright Event:
git clone:
`https://github.com/betsybeth/Bright_event.git`  
into your computer
* change your directory into `cd Bright_event`
#### Usage
with Bright Event you can:
* create an account
* login into the account
* create an event
* update an event
* view an event
* delete an event
* add RSVP into the event
* update RSVP card
* delete an RSVP card
* logout
#### Setting
* First install the virtual environment globally `sudo pip instal virtualenv`
* create the virtual enviroment `virtualenv --python=python3 myenv`
* activate virtual environment `source myenv/bin/activate`
#### How to run flask
* Run  `python run.py`

#### Testing:
* Install nosetests `pip install nose`
* Run the tests `nosetests -v`
#### Flask API endpoints

| Endpoints                                       |       Functionality                  |
| ------------------------------------------------|:------------------------------------:|
| `POST /api/auth/register`                       |  registers a user                    |
| `POST /api/auth/login`                          |  login a user                        |   
| `POST /api/v1/events                            |  create an event                     |
| `GET /api/v1/events`                            |  Retrieves an event                  |
| `PUT /api/v1/events/<eventId>`                  |  updates an event                    |
| `DELETE /api/v1/events/<eventId>`               |  deletes an event                    |
| `POST /api/v1/event/<eventId>/rsvp`             |  create an rsvp                      |
| `GET /api/v1/event/<eventId>/rsvp`              |  retrieves an rsvp                   |
|` PUT /api/v1/event/<eventId>/rsvp/<rsvpId>`     |  updates an rsvp                     |
|` DELETE /api/v1/event/<eventId>/rsvp/<rsvpId>`  |  delete an rsvp                      |
|` POST /api/v1/logout`                           |  logout a user                       |

### Credits
* [Beth][1]

[1]: https://github.com/betsybeth
