# django_quiz
This is a dockerized django rest framework example. Once docker-compose is UP, there will be two services running based on own dockerfiles sitting in the docker_compose directory. App code is in app folder. 

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

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

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
