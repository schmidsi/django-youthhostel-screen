#/bin/bash

# push all the commited stuff to heroku
git push

# collect static files locally -> faster to deploy on s3
foreman run "venv/bin/python manage.py collectstatic --noinput"

# syncing the db, you never know
heroku run "python manage.py syncdb"

# migrate
heroku run "python manage.py migrate"