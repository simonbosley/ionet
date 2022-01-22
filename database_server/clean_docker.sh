# Remove the container (and stop first if reqiured)
docker rm -f database_container

# Delete the container
docker rmi database_image:1.0.0