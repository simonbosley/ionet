# Run the database docker image that we built (if it doesn't exist, build first).
docker run --name database_container -p 5432:5432 -d database_image

# Print the logs from the server as it's starting up... TODO: Set this to a time period so we don't keep following it.
docker logs --details --follow database_container