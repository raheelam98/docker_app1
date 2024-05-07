# poetry add fastapi sqlmodel uvicorn\[standard\] psycopg  psycopg2 
# pip install "passlib[bcrypt]"
# pip install pytest
# poetry add pytest
# poetry add httpx

<!-- compose yaml 
 Declarative (Standardization , can’t change or fix )
 Multi-compose ( multiple containers in one file)

docker compose up -d 
 builds the images (if needed) and starts the container in detached mode (background)
 Note :- -d, --detach  (Detached mode: Run containers in the background) -->

# docker compose stop
 <!-- ### stops the container -->
# docker compose down
 <!-- ### stops and removes the container -->
# docker-compose logs
 <!-- ### to view logs from detached containers -->
# docker compose config 
<!-- ### detail  -->
# docker compose ps    
<!-- view runing images ### NAME ,  IMAGE,   COMMAND,  SERVICE,  CREATED , STATUS ,  PORTS -->
# docker compose ls     
 <!-- view list  ###  NAME  - STATUS  -  CONFIG FILES -->
# docker compose up -d --build 
 <!-- ###  rebuild the new image -->
