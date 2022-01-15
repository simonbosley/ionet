# Run the database docker image that we built (if it doesn't exist, build first).
docker run --name database_container -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d database_image

# Now run bash on running container, in interactive mode so that we can start playing with it.
#docker exec -it database_container /bin/bash