# Configuring solr-7.0.0, python and dependencies
## Setting up apache solr
Download latest version of apache solr
```
wget http://www-eu.apache.org/dist/lucene/solr/7.0.0/solr-7.0.0.tgz
```
And follow these commands to total setup
```
tar xzf solr-7.0.0.tgz solr-7.0.0/bin/install_solr_service.sh  --strip-components=2
sudo bash ./install_solr_service.sh solr-7.0.0.tgz
```
You can check the status of solr with
```
sudo service solr status
```
To start solr:
```
sudo service solr start
```
To stop :
```
sudo service solr stop
```
To start/stop with/to solr user
```
sudo -u solr service solr start/stop
```

## Python setup with dependencies & other
We are using python2.7 anyhow it how it doesn't matter. All you should have is latest version of JDK and these packages installed:
* urllib2 (or urllib3)
* simplejson
* curl (for the purpose CRUD operations - use this command to install ``` sudo apt-get install curl ```)
* JDK (latest version)

*Done configuring*
