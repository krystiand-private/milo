#!/bin/bash
./manage.py migrate
./manage.py shell -c "import datetime; from app.models import User; User.objects.create_superuser('user1', 'user1', date_of_birth=datetime.date(1990,1,1))"
./manage.py shell -c "import datetime; from app.models import User; User.objects.create_superuser('user2', 'user2', date_of_birth=datetime.date(2010,1,1))"
./manage.py shell -c "import datetime; from app.models import User; User.objects.create_superuser('user3', 'user3')"
