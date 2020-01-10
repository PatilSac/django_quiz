# django_quiz
This is a dockerized django rest framework example. Once docker-compose is UP, there will be two services running based on own Dockerfiles sitting in the docker_compose directory. App code is in app folder. 

## Prerequisites

Ensure that you have docker, docker-compose installed

```
sudo apt-get update
sudo apt-get install docker-ce
sudo apt-get install docker-compose
```

### Getting Started

Want to run this on local linux? (find out windows alternatives for your windows machine)

1. Ensure that you have docker, docker-compose installed
```
sudo apt-get update
sudo apt-get install docker-ce
sudo apt-get install docker-compose
```
2. Clone git repo
```
git clone https://github.com/PatilSac/django_quiz.git
```
3. Build the services written in docker_compose
```
docker-compose -f docker-compose.yml build
```
4. Run the services using docker_compose
```
docker-compose -f docker-compose.yml up
```

## Containers

There are two servers. Dockerfiles for them are located at:
django_server : docker_compose/docker/Dockerfile
nginx_server  : docker_compose/nginx/Dockerfile


### Network

## Gunicorn
Python Web Server Gateway Interface HTTP server, running at 0.0.0.0:8000 in the django_server container. This is something that executes Python as Python isn't the best at handling all types of requests.

## Nginx
Web server, reverse proxy, load balancer, mail proxy and HTTP cache combination being used here for django rest framework. It is running at port 80 in its docker container and serving Gunicorn.

### CI/CD

```
TBD:

  GitHub                             Nexus 
    |                                  Λ
    | webhook on checkin               | backup
    |                                  |
  Jenkins  - - - - - - - - - - - -  > Host - - - - - - - - - - > Kubernetes (configure, scale, monitor)
              code trans                     unit/int test
```

### DO NOT READ BEYOND THIS. ITS A TEMPLATE FOR README FILE IN GITHUB.

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
