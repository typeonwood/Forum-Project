# Versatile Online Forum
This project contains one app, which is the back-end for a reusable online forum. It can easily be exported into a variety of other projects, including company websites, online stores, and more. In addition, it could serve as a standalone back-end for any straightforward forum website. Potential examples include hobbyist forums, video game forums, and tech forums.
<br><br>
Using this API, unauthenticated users are able to browse categories, posts (threads), and replies to those posts. Filtering, ordering, and searching are all enabled on the post (thread) lists. 
<br><br>
Authenticated users are able to perform CRUD operations on their own posts and replies, and they're also able to upvote and downvote posts/replies. Posts have a built-in media link field, which could be used by the system to point to a static file that the user uploaded. Users are unable to access this field themselves.
<br><br>
Admin users gain additional privileges, including the ability to perform CRUD operations on all categories, posts, replies, and upvotes/downvotes. Whereas regular users can only see the replies/upvotes for the selected post, admin users are able to call all replies/upvotes in the database as well as order, filter, and search them. 
<br><br>
All of this functionality is available through the endpoints in the app's urls file, so the use of the Django admin site is unnecessary. You're still welcome to access it using the admin account listed below in the "Users" section.
<br><br>
Thank you for viewing this project, and I hope you enjoy it :)
<p>&nbsp;</p>

# Setting up project
## 1. Activate virtual environment
Navigate to the django project directory and use command `source venv/bin/activate` to activate the virtual environment.
## 2. Install dependencies
Dependencies are written in requirements.txt and can be downloaded using `python3 -m pip install -r requirements.txt` from within the django project directory.
## 3. Create database
Back out to repository directory, and use `mysql < dump.sql` to copy the project database to your machine.
## 4. Configure database
Open settings.py. Under `DATABASES`, ensure that `USER` and `PASSWORD` match a mysql user on your machine, and ensure that this user has permission to access the `forum_project` database with all privileges. The easiest way to do this is to just use the `root` user.
## 5. Run migrations and start server
<p>&nbsp;</p>

# Users
## testuser
* type: admin/superuser
* password: lemon@123!
## somefella
* type: user
* password: lemon@123!
## anotherfella
* type: user
* password: lemon@123!
<p>&nbsp;</p>

# Endpoints
## Important notes
* Admin users will see more detail or slightly different data at a given endpoint. For instance, when an authenticated user calls the `categories/<int:category>/threads/` endpoint, they'll see data such as the title of the post, the user, the category, etc. When an admin calls this endpoint, they will be able to see this information, but they will also be able to see the number of replies a given post has, the id of the post, and any static media links the post has.
## Djoser/authentication
`auth/users`<br>
`auth/users/me`<br>
`auth/token/login`
## Forum
`categories/`
* queryset: all categories
* methods: GET, POST
* permissions required: 
    * POST: admin

`categories/<int:pk>/`
* queryset: category with given pk
* methods: GET, PUT, PATCH, DELETE
* permissions required: admin

`categories/<int:category>/threads/`
* queryset: all threads within the given category
* methods: GET, POST
* permissions required:
    * GET: none
    * POST: authenticated
* order: date_time_added, threadvotes, replies
* search: title, user, content
* filter: date_time_added (gte, lte), user, locked

`categories/<int:category>/threads/<int:pk>/`
* queryset: thread with given pk
* methods: GET, PUT, PATCH, DELETE
* permissions required: 
    * GET: none
    * all other methods: thread owner or admin

`categories/<int:category>/threads/<int:thread>/replies/`
* queryset: all replies
* methods: GET, POST
* permissions required:
    * GET: admin
    * POST: authenticated
* order: date_time_added, replyvotes, replies
* search: user, thread, content
* filter: date_time_added (gte, lte), user, thread

`categories/<int:category>/threads/<int:thread>/replies/<int:pk>/`
* queryset: reply with given pk
* methods: GET, PUT, PATCH, DELETE
* permissions required:
    * GET: none
    * all other methods: reply owner or admin

`threads/<int:thread>/thread-votes/`
* queryset: all votes for all threads
* methods: GET, POST
* permissions required:
    * GET: admin
    * POST: authenticated
* search: user, thread
* filter: upvote, user, thread

`threads/<int:thread>/thread-votes/<int:pk>/`
* queryset: thread vote with given pk
* methods: GET, PUT, PATCH, DELETE
* permissions required:
    * PUT or PATCH: vote owner
    * DELETE: vote owner or admin

`threads/<int:thread>/reply-votes/`
* queryset: all votes for all replies
* methods: GET, POST
* permissions required:
    * GET: admin
    * POST: authenticated
* search: user, reply
* filter: upvote, user, reply

`threads/<int:thread>/reply-votes/<int:pk>/`
* queryset: reply vote with given pk
* methods: GET, PUT, PATCH, DELETE
* permissions required:
    * PUT or PATCH: vote owner
    * DELETE: vote owner or admin


