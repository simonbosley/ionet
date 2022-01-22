# Remove the container (and stop first if reqiured)
docker rm -f app_server_container

# Delete the container
docker rmi app_server_image:1.0.0