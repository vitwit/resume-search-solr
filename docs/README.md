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

## Some useful apache-solr commands
As the configuration done, solr will be in /opt directory:
solr command path is ``` /opt/solr/bin/solr ```
post command path is ``` /opt/solr/bin/post ```

*Note :-* we can create the symbolic link to solr and post as 
```
sudo ln -s /opt/solr/bin/solr /bin/solr
sudo ln -s /opt/solr/bin/post /bin/post
```
To create a core :
```
sudo -u solr solr create -c core_name
```
To delete :
```
sudo -u solr solr delete -c core_name
```
For command line help on post:
```
sudo -u solr post -h
```

## CRUD Operations
We can do crud operatoins with different content types. We are going to use 3 of all:
* JSON,
* XML and
* CSV

create the core with core name, details.
```
sudo -u solr solr create -c details
```
### ADDING
```
curl http://localhost:8983/solr/details/update?commit=true -H "Content-Type: text/xml" --data-binary '
<add> 
   <doc> 
      <field name = "id">001</field> 
      <field name = "first name">f1</field> 
      <field name = "last name">l1</field> 
      <field name = "phone">9999999991</field> 
      <field name = "city">City1</field> 
   </doc>  
   <doc> 
      <field name = "id">002</field> 
      <field name = "first name">f2</field> 
      <field name = "last name">l2</field> 
      <field name = "phone">9999999992</field> 
      <field name = "city">City2</field> 
   </doc>  
   <doc> 
      <field name = "id">001</field> 
      <field name = "first name">f1</field> 
      <field name = "last name">l1</field> 
      <field name = "phone">9999999993</field> 
      <field name = "city">City3</field> 
   </doc>  
   <doc> 
      <field name = "id">001</field> 
      <field name = "first name">f1</field> 
      <field name = "last name">l1</field> 
      <field name = "phone">9999999994</field> 
      <field name = "city">City4</field> 
   </doc>  
   <doc> 
      <field name = "id">001</field> 
      <field name = "first name">f1</field> 
      <field name = "last name">l1</field> 
      <field name = "phone">9999999995</field> 
      <field name = "city">City5</field> 
   </doc>
</add>
'
```
or simply using xml file [people.xml](https://github.com/vitwit/resume-search-solr/tree/master/docs/data/people.xml)
```
curl http://localhost:8983/solr/details/update?commit=true -H "Content-Type: text/xml" --data @/path/to/xml/file
```

### DELETING
Deleting all the data in the collection
```
curl http://localhost:8983/solr/details/update?commit=true -H "Content-Type: text/xml" -d '
  <delete>
    <query>*:*</query>
  </delete>
'
```
Deleting some particular document by query
```
curl http://localhost:8983/solr/details/update?commit=true -H "Content-Type: text/xml" -d '
  <delete>
    <query>
      <id>005</id>
    </query>
  </delete>
'
```

Deleting multiple documents
```
curl http://localhost:8983/solr/details/update?commit=true -H "Content-Type: text/xml" -d '
  <delete>
    <query>
      <id>004</id>
      <id>003</id>
    </query>
  </delete>
'
```

### RETRIEVING OR SELECTING
Retrieve all the data from the collection
```
curl "http://localhost:8983/solr/details/select?indent=on&q=*:*&wt=json"
```
Retrieving some particular document
```
curl "http://localhost:8983/solr/details/select?indent=on&q="{id:001}"&wt=json"
```

### UPDATING
Update documents
```
curl http://localhost:8983/solr/temp/update?commit=true -H "Content-Type: text/xml" -d '
  <add>
    <doc>
      <field name="id">001</field>
      <field name="first_name" update="set">f1*</field>
    </doc>
  </add>
'