### Simple country currency exchange api

## Purpose 
This API allow to obtain a list of from which country and to which country
we can exchange currencies.

The REST api over HTTP protocol could be queried for:

* Get the source contries list
* Get the destination countries list

The output will be always in [JSON](http://www.json.org) format

## API Reference

* Get the source:       /v1/countries?target=source
* Get the destination   /v1/countries?target=destination

## API Example usage (using curl utility)

* Protocol: http
* Port: 8080
* Host Address: localhost
* Special http header: Accept application/json

```bash
curl -H "Accept: application/json" 'http://localhost:8080/v1/countries?target=source'

curl -H "Accept: application/json" 'http://localhost:8080/v1/countries?target=destination'
```

### How to Install/Test/Run the API service

#### Install the api
```bash
make install
```

#### Test the api
```bash
make test
```

### Execute the api service
```bash
make run
```

### Dependecies
* python 2.7
* pip
* gnu make

