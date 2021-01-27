![](https://miro.medium.com/max/900/1*b0TtGI6gWFLltL1QkRxVdg.png)

A cross-platform document oriented NoSQL database that stores data as JASON documents and provides high performance, high availaility and easy scalability. Used by Github and Cassandra

## Working concept

Works on the principle of collections and documents
  
  * Collection- group of MongoDB documents and does not enforce a schema
  * Document- set of key-value pairs having dynamic schema
  
![](https://studio3t.com/knowledge-base/wp-content/uploads/mongodb-document-structure.png)

## Terminology comparison with RDBMS databases

| RDBMS | MongoDB |
| ----- | --------|
| Database | Database |
| Table | Collection |
| Tuple/row | Document |
| Column | Field |
| Table join | Embedded documents |
| Primary Key | Primary Key |

* Database and client
  * Oracle - mongod
  * sqlplus - mongo

# Features

1. No support to SQL like query language and join operations
2. ACID complient
3. Manage semi-structured data
4. Supports shared nothing architecture
5. Can handle multiple and nested documents easily
6. Provides an API to retrieve documents based on their content
7. Built in support for map-reduce
8. Suitable for agile development

# Applications

1. Blogging systems and shopping carts
2. Content and inventory managment system
3. Mobile applications

# Running MongoDB on Ubuntu

**Note: I will be using MongoDB terminal**

* Install-
  * Import MongoDB public key: **sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10**
  * Create a /etc/apt/sources.list.d/mongodb.list file: **echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-uptart dist 10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list**
  * Update the repositry: **sudo apt-get update**
  * Final command to install: **apt-get install mongodb-10gen=2.2.3**
  
* Start server- sudo service mongodb start
* Stop server- sudo service mongodb stop
* Restart server- sudo service mongodb restart
* Connect to running instance- mongo
* Help- db.help()

# Syntax for some data types

1. _id: ObjectId(hexadecimal input)
2. string: 'value'
3. integer: number
4. list: ['string', integer]

# Commands

1. Databases

    * Create: use DATABASE_NAME
    * Show current: db
    * Show all: show dbs
    * Drop: db.drop(DATABASE_NAME)
    * Switch database: use acme

2. Collections

    * Create: db.createCollection(Name, options)
    
    | Option name | Type | Description |
    | ------------ | ---- | ----------- |
    | capped | boolean | automatically overwrites old entries |
    | autoIndexID | boolean | automatically create on_id field |
    | size | number | size (in bytes) for capped collection |
    | max | number | numeber of documents allowed in capped collection |
    
    * Drop: db.Collection_Name.drop()
    * Show: show collections
    
3. Documents

    * Insert: db.Collection_Name.insert()
        * insert single row- db.DATABASE_NAME.insert({})
        * insert multiple rows- db.DATABASE_NAME.insert({}, {}, ...)
          * if _id not specified- db.Collection_Name.save(document)
    * Delete: db.Collection_Name.remove(DELETION_CRITERIA)

## Functions used to querying documents

| Name | Purpose | Syntax |
| ---- | ------- | ------ |
| find() | display all rows as unformatted output | db.COLLECTION_NAME.find() |
| findOne() | return only one document | db.COLLECTION_NAME.findOne({key1: value})|
| pretty() | display all rows as formatted output | db.COLLECTION_NAME.find().pretty() |
| and() | perform and operation of SQL | db.COLLECTION_NAME.find({key1: value1, key2: value2}) |
| or() | perform or operation of SQL | db.COLLECTION_NAME.find({$or:[{key1: value1}, {key2: value2}]}) |
| update() | update values in existing document | db.COLLECTION_NAME.update(SELECTION_CRITERIA, UPDATED_DATA) |
| save() | replace existing document with new document | db.COLLECTION_NAME.save({_id: ObjectId(), NEW_DATA}) |
| limit() | to limit records | db.COLLECTION_NAME.find().limit(NUMBER) |
| count() | count rows | db.COLLECTION_NAME.find().count()|
| skip() | skip a number of arguments | db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER) |
| sort() | sort in ascending/descending (1 for ascending, -1 for descending) | db.COLLECTION_NAME.find().sort({Key: 1/-1}) |
| aggregate() | group vaues from multiple records together, perform variety of operations and return single result  | db.COLLECTION_NAME.aggregate(OPERATION) |
| forEach() | return only one document | db.COLLECTION_NAME.find().forEach(function(doc){})|
| createIndex() | add Index to row | db.COLLECTION_NAME.createIndex({key: VALUE}) |

### Using aggregate()

Consider a few database fields- city, state, total pop, _id

Show name and population of state based on cities- **db.docs.aggregate([{$match: {city: {$exists: true}}}, {$group: {_id: "$state", "Total Pop": {$sum: "$pop"}}}])**

Show total cities in New York as population- **db.docs.aggregate([{$match: {state: "NY"}}, {$group: {_id: "$state", "Total pop:" {$sum: "pop"}}}])**

### Projections

Selecting only necessary data rather than selected whole data of a document. Syntax- db.COLLECTION_NAME.find({}, {Key: Value})

Example- Display only title of document while querying the document in posts collection.

db.posts.find({}, {"title": 1, _id: 0})

### Additional options for functions

1. find()

    * $elemMatch - to find a row in the document with elements matching the query. Example: db.posts.find({comments:{$elemMatch:{user: 'Divyank Singh'}}})
    * $text - Performs text search. Example: db.posts.find({$text:{$search: "\ "Post 0\ "}})
        
        **"\ "Post 0\ "** returns documents having Post0 in a phrase while **"Post 0"** would return documents having Post 0 as a word
    * Clauses
    
    | Clause Name | Syntax |
    | ----------- | ------ |
    | Equality | db.COLLECTION_NAME.find({key: value}) |
    | Less than | db.COLLECTION_NAME.find({key: {$lt: value}}) |
    | Less than equals | db.COLLECTION_NAME.find({key: {$lte: value}}) |
    | Greater than equals | db.COLLECTION_NAME.find({key: {$gte: value}}) |
    | Not equals | db.COLLECTION_NAME.find({key: {$ne: value}}) |

2. update()

| Variations | Syntax |
| ---------- | ------ |
| findOneAndUpdate() | db.COLLECTION_NAME.findOneAndUpdate(SELECTION_CRITERIA, UPDATE_DATA) |
| updateOne() | db.COLLECTION_NAME.updateOne(SELECTION_CRITERIA, UPDATE_DATA) |
| updateMany() | db.COLLECTION_NAME.updateMany(SELECTION_CRITERIA, UPDATE_DATA) |
| sub documents | db.COLLECTION_NAME.update({title: VALUE}, {$set: {....}}) |

**$push** is used to update an element in a list 
