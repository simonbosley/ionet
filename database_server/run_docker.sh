# Run the database docker image that we built (if it doesn't exist, build first).
docker run --name database_server_container -p 5432:5432 -d database_server_image:1.0.0

# The container is now hopefully running in detached mode, let's give it some time to start up.
sleep 1

# Print the logs from the server now that it has had a chance to start up.
docker logs --details --timestamps database_server_container