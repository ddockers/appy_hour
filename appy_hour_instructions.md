# Instructions and Troubleshooting

## Python

Image:
```
ddoxton/appy-hour
```

Container: 
```
appy-hour-python
```

Running `docker container inspect appy-hour-python` and scrolling to `Config` then `volumes` shows `null`.

![Imgur](https://i.imgur.com/HGwe1I4.png)

I've created a volume called `appy-hour-vol`. I think this needs to be mounted to the Python container.

Running the following:

```
docker container run --name appy-hour-python --mount source=appy-hour-vol,target=/app ddoxton/appy hour
```

gives the following output:

```
docker: Error response from daemon: invalid mount config for type "volume": invalid mount path: 'C:/Program Files/Git/app' mount path must be absolute.
See 'docker run --help'.
```

Running `docker volume inspect appy-hour-vol` shows the "Mountpoint" as `"/var/lib/docker/volumes/appy-hour-vol/_data"`

Amending the container run command to the following:

```
docker container run --name appy-hour-python --mount source=/var/lib/docker/volumes/appy-hour-vol,target=/app ddoxton/appy-hour
```

gave the following output:

```
docker: Error response from daemon: Conflict. The container name "/appy-hour-python" is already in use by container "d0aa2c69ed256e3f46746ab52220b93bd4b590dd11d815c567b2e73b1ef8d0f3". You have to remove (or rename) that container to be able to reuse that name.
See 'docker run --help'
```

The volume `appy-hour-vol` has been deleted. I need to create a container using the image `ddoxton/appy-hour` without an error occurring.

What I am currently trying to do is get appy_hour.py to run in a container called appy-hour-python. I want to create and run the container with appy-hour-vol mounted to it.

After multiple errors, the following command got the program to run:

```
docker container run --name appy-hour-python --mount type=bind,source=C:/Users/dedo2/personal_projects/appy_hour/appy_hour,target=/app/ddoxton/appy-hour/appy_hour.py ddoxton/appy-hour
```

Now to make sure the volume is mounted.

I've checked. Volumes=null.

**CORRECTION!**

The volume isn't under `Config`. It's under `Mounts`:

![Imgur](https://i.imgur.com/yRjL4do.png)

## React Container

I've tried running:

```
docker container run --name appy-hour-react --mount type=bind,source=C:/Users/dedo2/personal_projects/appy_hour/appy_hour,target=app/ddoxton/appy-hour/appy_hour.py ddoxton/appy-react
```

And I received the error about the mount path being absolute.

I think I was missing a `/`. However. I'm first checking with Chat if the correct course of action is to bind mount the program to the React app.

## Purpose of Volumes and Networks

### Volumes
Store and share data between containers.

For example, if you want to store the output from the Python container in a file and access it from the React container, you can use a volume to mount the same directory to both containers. This way, the React container can read the file from the volume and display it to localhost. However, this approach may not be very efficient or scalable, as it involves writing and reading files from the disk.

### Networks
Enable communication between containers.

Alternatively, if you want to send the output from the Python container to the React container as a response to a request, you can use a network to connect both containers. This way, the React container can send a request to the Python container using its service name or IP address, and the Python container can send back the output as a response. This approach may be more efficient and scalable, as it involves sending and receiving data over the network.

### Next Steps Taken

I have already created a network called `appy-hour-net`.

I have renamed the React container to `appy-hour-react`.

I hae connected each container to the newtork by running `docker network connect appy-hour-net <name of container>`.

```
docker network connect appy-hour-net appy-hour-python
```

```
docker network connect appy-hour-net appy-hour-react
```

I can't see the containers on the network by running `docker network inspect appy-hour-net`.

Inspecting each container by running `docker container inspect <name of container>` shows that the containers are connected to `appy-hour-net`.

![Imgur](https://i.imgur.com/xM2dTZV.png)

Next thing to do is to get the React container to send a request to the Python container to get its output.

Also, looking back at my volumes chat file, I should maybe send the Python output to a file in the shared volume directory.

## Building Image

Each time I update the code to then run in a container, I have to rebuild the image.

The source code has been updated, so I need to `cd` into the appy-hour code folder and run:

```
docker build -f Dockerfile.dev -t ddoxton/appy-hour .
```

A way to make the project run is to create docker-compose files. I can choose the image, volumes, networks and other config settings and run both containers.

Here's an example of the docker-compose file I could create:

```
version: '3'
services:
  appy-hour-python:
    image: ddoxton/appy-hour
    container_name: appy-hour-python
    command: python appy_hour.py
    volumes:
      - appy-hour-vol:/app
    networks:
      - appy-hour-net
  appy-hour-react:
    image: ddoxton/appy-react
    container_name: appy-hour-react
    ports:
      - '80:80'
    depends_on:
      - appy-hour-python
    networks:
      - appy-hour-net
volumes:
  appy-hour-vol:
networks:
  appy-hour-net:
```


I would need to include somewhere that the containers need to be built with Dockerfile.dev files, instead of the default Dockerfile.

`docker-compose.yml` will need to be saved in the project directory. The build context for each container will need to be included. E.g., the `appy-hour-python` container would need to have the context of `./appy-hour` and `appy-hour-react` would be `./appy-hour-react`

This file will create two services, appy-hour-python and appy-hour-react, each with their own image, container name, and command. The appy-hour-python service will run the appy_hour.py file from the appy-hour-vol volume, which will be mounted to the /app directory in the container. The appy-hour-react service will run on port 80 and depend on the appy-hour-python service. Both services will use the appy-hour-net network to communicate with each other.

The colon at the end of appy-hour-vol and appy-hour-net in the last four lines of the docker compose file is used to indicate that the volume and network are defined as top-level elements in the file. This means that they are not specific to any service, but can be shared by multiple services in the file. The colon separates the name of the volume or network from the next field, which is optional and can specify the configuration of the volume or network.

Here is an updated `docker-compose.yml` that I'll try to use:

```
version: '3'
services:
  appy-hour-python:
    image: ddoxton/appy-hour
    container_name: appy-hour-python
    command: python appy_hour.py
    build:
      dockerfile: Dockerfile.dev
      context: ./appy_hour
    volumes:
      - appy-hour-vol:/app
    networks:
      - appy-hour-net
  appy-hour-react:
    image: ddoxton/appy-react
    container_name: appy-hour-react
    build:
      dockerfile: Dockerfile.dev
      context: ./appy-hour-react
    ports:
      - '3000:80'
    depends_on:
      - appy-hour-python
    networks:
      - appy-hour-net
volumes:
  appy-hour-vol:
networks:
  appy-hour-net:
```

### Troubleshooting

`localhost` and `localhost:3000` cannot be reached. I need to remember the previous reasons for not showing up on localhost.

According to chat:

Yes, containers on the same network should be able to communicate with each other. However, in your `docker-compose.yml` file, you have not mapped the port `5000` of the `appy-hour-python` container to any port of the host machine. Therefore, the React container is not able to access the Python container at `localhost:5000`.

To fix this issue, you can add the following line to your `docker-compose.yml` file under the `appy-hour-python` service:

```
ports:
  - '5000:5000'
```

This will map the port `5000` of the Python container to the port `5000` of the host machine. Then, you can modify the `command` of the `appy-hour-react` service to use the IP address of the Python container instead of `localhost`. For example:

```
command: REACT_APP_API_URL=http://appy-hour-python:5000 npm run start
```

This will set the `REACT_APP_API_URL` environment variable to `http://appy-hour-python:5000`, which is the IP address of the Python container.

I hope this helps!

## Updated docker-compose file

```
version: '3'
services:
  appy-hour-python:
    image: ddoxton/appy-hour
    container_name: appy-hour-python
    command: python appy_hour.py
    build:
      dockerfile: Dockerfile.dev
      context: ./appy_hour
    volumes:
      - appy-hour-vol:/app
    networks:
      - appy-hour-net
    ports:
      - '5000:5000'
  appy-hour-react:
    image: ddoxton/appy-react
    container_name: appy-hour-react
    command: REACT_APP_API_URL=http://appy-hour-python:5000 npm run start
    build:
      dockerfile: Dockerfile.dev
      context: ./appy-hour-react
    ports:
      - '3000:80'
    depends_on:
      - appy-hour-python
    networks:
      - appy-hour-net
volumes:
  appy-hour-vol:
networks:
  appy-hour-net:
```

Doing this gave the following error:

![Imgur](https://i.imgur.com/rE95bmk.png)

### Troubleshooting

This error was because the environment variable was set in the command of the `appy-hour-react` service. 

The environment variable should be set in `environment` under `appy-hour-react`.

## Amended docker-compose file:

```
version: '3'
services:
  appy-hour-python:
    image: ddoxton/appy-hour
    container_name: appy-hour-python
    command: python appy_hour.py
    build:
      dockerfile: Dockerfile.dev
      context: ./appy_hour
    volumes:
      - appy-hour-vol:/app
    networks:
      - appy-hour-net
    ports:
      - '5000:5000'
  appy-hour-react:
    image: ddoxton/appy-react
    container_name: appy-hour-react
    command: npm run start
    build:
      dockerfile: Dockerfile.dev
      context: ./appy-hour-react
    ports:
      - '3000:80'
    depends_on:
      - appy-hour-python
    networks:
      - appy-hour-net
    environment: 
      - REACT_APP_API_URL=http://appy-hour-python:5000
      
volumes:
  appy-hour-vol:
networks:
  appy-hour-net:
```

### Troubleshooting

The webpack compiles successfully, but the page cannot be reached at localhost:3000 (or at http://appy-hour-python:5000 fwiw).

I corrected the port mapping under `appy-hour-react` to `ports: - '3000:3000`.

When I run `docker-compose up --build`, the react app can be viewed at `localhost:3000`. The Python output isn't displayed.

I assume I need to map the Python container to the React container.

I've amended `docker-compose.yml` several times; here is my latest iteration:

```
version: '3'
services:
  appy-hour-python:
    image: ddoxton/appy-hour
    container_name: appy-hour-python
    command: python appy_hour.py
    build:
      dockerfile: Dockerfile.dev
      context: ./appy_hour
    volumes:
      - appy-hour-vol:/app
    networks:
      - appy-hour-net
    ports:
      - '5000:5000'
  appy-hour-react:
    image: ddoxton/appy-react
    container_name: appy-hour-react
    command: npm run start
    build:
      dockerfile: Dockerfile.dev
      context: ./appy-hour-react
    ports:
      - '3000:3000'
    depends_on:
      - appy-hour-python
    networks:
      - appy-hour-net
    environment: 
      - REACT_APP_API_URL=http://appy-hour-python:3000
      
volumes:
  appy-hour-vol:
networks:
  appy-hour-net:
```

It still only shows the React app homepage at `localhost:3000`.

### Network Troubleshooting

I ran `docker network ls` and received a curious result:

![Imgur](https://i.imgur.com/IPjsUzT.png)

A new network called `appy_hour_appy-hour-net` has been created.

Running `docker network inspect appy_hour_appy-hour-net` showed that only `appy-hour-react` is connected to the network, not `appy-hour-python`.

Running inspect on `appy-hour-net` showed that no containers are connected. It could be because the Python container stops running upon completion, or that the Python container isn't even running on `appy-hour-net`.

`appy_hour_appy-hour-net` was created because Docker automatically prepends the name of a project directory to the network name.

Potential amendments to be made:

```
services:
  appy-hour-python:
    # other configuration options
    networks:
      - appy-hour-net
  appy-hour-react:
    # other configuration options
    networks:
      - appy-hour-net
networks:
  appy-hour-net:
    external: true

```

Running `docker-compose up` after making the above amendments caused the Python container to run end exit, but the React container doesn't appear to start.

According to Docker Dexktop, the React app is running, despite there being no indication of this in the GitBash terminal. The React container is in fact running, seeing as the React homepage is displayed at `localhost:3000`.