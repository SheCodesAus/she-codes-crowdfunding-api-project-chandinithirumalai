# {{ my project title }}
​
{{ 
    a paragraph detailing the purpose 

Crowdfunding website for international students or people who don’t 
know how to drive a car (and don’t have access to learning how to drive) but 
want to learn. People can either donate their time (to teach and log 100 hours) or
they can donate money towards driving school lessons.

and target audience 

International students, grads 
(international), people who don’t have access to learning how to drive 

}}
​
## Features
​1. Favourites (Projects that are favourited by users)
2. Aggregate models 
3. Changing passwords 

### User Accounts
​
- [Admin] Username
- [admin@admin.com] Email Address
- [admin] Password
​
### Project
​
- [X] Create a project
  - [X] Title 
  - [X] Owner (a user)
  - [X] Description
  - [X] Image 
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [ ] Limit who can create 
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
- Pledge
  - [ ] Limit who can create
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
- Pledge
  - [ ] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
​
### Implement relevant status codes
​
- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [ ] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] impliment /api-token-auth/
​
## Additional features
​
- [ Favourites] {Title Feature 1}
​
{{ This feature enables us to see the projects that are favourited by different users }}
​
- [Aggregate models] {Title Feature 2}
​
{{ This feature enables us to see the total amount pledged for a certain project and the total amount pledged by a certain user }}
​
- [Changing password ] {Title Feature 3}
​
{{ User can change password if they wish to.}}

## Features that I need to work on 

- Adding a time feature next to the amount: This is because my project states that people can donate their time or money. 

- Creating new users 

- Adding a progress bar next to the amount and time for each project 
​
### External libraries used
​
- [ ] django-filter
​
​
## Part A Submission
​
- [ ] A link to the deployed project.


- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.

https://docs.google.com/document/d/1UtWXqeRh5HevpJF_hHCC9_MnT2WlSuw7SHHxxXl58ms/edit?usp=sharing 


- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.

https://docs.google.com/document/d/1UtWXqeRh5HevpJF_hHCC9_MnT2WlSuw7SHHxxXl58ms/edit?usp=sharing 

- [ ] A screenshot of Insomnia, demonstrating a token being returned.

https://docs.google.com/document/d/1UtWXqeRh5HevpJF_hHCC9_MnT2WlSuw7SHHxxXl58ms/edit?usp=sharing


- [ ] Your refined API specification and Database Schema.
https://docs.google.com/document/d/1UtWXqeRh5HevpJF_hHCC9_MnT2WlSuw7SHHxxXl58ms/edit 
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"email": "not@myemail.com",
	"password": "not-my-password"
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser",
	"password": "not-my-password"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token 5b8c82ec35c8e8cb1fac24f8eb6d480a367f322a' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Donate a cat",
	"description": "Please help, we need a cat for she codes plus, our class lacks meows.",
	"goal": 1,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-28T05:53:46.113Z"
}'
```
