#!/bin/bash
# build container
docker build -t django_expense_tracker .
# Remove all existing containers
docker stop `docker ps -aq`; docker rm `docker ps -aq`
# create django_network to connect both containers
docker network create --driver bridge django_network
# Create database directory
mkdir /tmp/database
if [[ "$OSTYPE" == "linux-gnu" ]]; then
	sudo chown -R postgres:postgres /tmp/database
	sudo semanage fcontext -a -t container_file_t  '/tmp/database(/.*)?'
	sudo restorecon -Rv /tmp/database
fi
# run postgres container
docker run --rm -p 5432:5432 -d  --network=django_network \
 -h 'postgresql' \
 --net-alias postgresql \
 -e POSTGRES_PASSWORD=pwd \
 -e POSTGRES_USER=user \
 -e POSTGRES_DB=expenseDB \
 -e PGDATA=/var/lib/postgresql/data/pgdata \
 -v /tmp/database/:/var/lib/postgresql/data/pgdata \
 postgres:latest


echo "If you need to create superuser you may 'docker exec -it container_id /bin/bash'"
echo "and run python manage.py createsuperuser"

sleep 30
# run django container
docker run --rm -p 8000:8000 --network=django_network -v $PWD:/code/ django_expense_tracker
