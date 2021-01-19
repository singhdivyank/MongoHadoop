![](https://miro.medium.com/max/2760/1*kPKoXmHBDmGthbah-0549A.png)

An Apache open source framework written in Java that allows for the distributed processing of large data sets (big data) across clusters of computers using simple programming models. Designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures.

# Installation

Can be installed in two ways- Single Node Cluster and Multi Node Cluster

1. **Single Node Cluster**: Every data node on single machine and used for testing
2. **Multi Node Cluster**: Every data node on different machine and used for analyzing big data

## Pre-requisites

1. Operating System: Linux or Windows (I am using Windows)
2. Java JDK 1.8.0
3. Hadoop 2.7.3 or 2.8.0

# Hadoop Layers

1. **Map Reduce**: Parallel programming model for processing

    Components-
      * **Job tracker**: Takes care of job scheduling and assigns tasks to task trackers
      * **Task tracker**: Accepts the tasks and performs Map, Reduce and Shuffle operations

2. **HDFS**: A layer used for storage and runs on commodity hardware. Based on Google file system

    Components-
      * **Name node**: Master node having list of hosts for secondary name nodes. It manages and maintains blocks on DataNodes and informs about location of daemons
      * **Data node**: Slave nodes having list of hosts for DataNode and Task tracker. Serve read and write requests for clients and provides storage

# Ecosystem

1. **HBase**: A NoSQL column database that runs on top of Hadoop and HDFS
2. **Pig**: A scripting platform having ETL tools written in Pig Latin and used by Yahoo!
    
    Components-
      * Pig Latin: To analyze data
      * Execute program: Grunt shell
      * Syntax checker: Parser
      * Optimise: Optimizer
      * Compile: Compiler
      * Predict result: Execution engine
3. **Hive**: Uses SQL like query language to provide data summarization and analysis and makes use of map-reduce programming for query execution. Used by FaceBook

    Components-
      * Core components
      * Meta-store
      * Driver
      * Hive clients
4. **Sqoop**: A RDBMS database that populates tables using imports
5. **Zookeeper**: A centralized service for maintaining configuration information and providing distributed synchronization

# Configuration files

1. **core-site.xml**: Inform location of NameNode to daemons

```
<configuration>
   <property>
       <name>fs.defaultFS</name>
       <value>hdfs://localhost:9000</value>
   </property>
</configuration>
```

2. **mapred.xml**: Configuration settings for MapReduce, job and task tracker

```
<configuration>
   <property>
       <name>mapreduce.framework.name</name>
       <value>yarn</value>
   </property>
</configuration>

```
3. **Hdfs-site.xml**: Configuration settings for daemons, primary and secondary NameNodes and DataNode

```
<configuration>
   <property>
       <name>dfs.replication</name>
       <value>1</value>
   </property>
   <property>
       <name>dfs.namenode.name.dir</name>
       <value>C:\hadoop-2.8.0\data\namenode</value>
   </property>
   <property>
       <name>dfs.datanode.data.dir</name>
       <value>C:\hadoop-2.8.0\data\datanode</value>
   </property>
</configuration>

```

4. **Yarn-site.xml**: Tracks the CPU and memory

```
<configuration>
   <property>
    	<name>yarn.nodemanager.aux-services</name>
    	<value>mapreduce_shuffle</value>
   </property>
   <property>
      	<name>yarn.nodemanager.auxservices.mapreduce.shuffle.class</name>  
	<value>org.apache.hadoop.mapred.ShuffleHandler</value>
   </property>
</configuration>

```
**Yarn is framework for job scheduling and runs on clusters**

5. **Hadoop-env.xml**: Set the environment variable

```
set JAVA_HOME = C:\java
```

# Hadoop Commands

1. Create directory: **hadoop fs -mk dir (path)**
2. Listing contents of directory: **hadoop fs -ls (directory)**
3. Upload a file: **hadoop fs -put (local source file path) (HDFS destination path)**
4. Download a file: **hadoop fs -get (HDFS source file)(local destination)**
5. See contents of a file: **hadoop fs -cat (file name with path)**
6. Copy a file:    
    * within HADOOP- **hadoop fs -cp (HDFS source) (HDFS destination)**
    * from local source file to HADOOP- **hadoop fs -copyFromLocal (local source) (HDFS destination)**
    * from HDFS to local- **hadoop fs -copyToLocal (HDFS source) (local destination)**
7. Move from source to destination: **hadoop fs -mv (source) (destination)**
8. Remove file/directory: **hadoop fs -rm (file name)**
9. Display last few lines: **hadoop fs -tail (file name with path)**
10. Display aggregate length: **hadoop fs -du (file name with path)**

## Source files and destination files

* local source file- /home/...
* HDFS destination path- /user/...
* HDFS source file- /user/...
* local destination file- /home/...

# Hadoop administrative commands

These are the commands present in ~/hadoop/bin directory and used to launch Hadoop DFS and MapReduce daemons

| | Start | Stop |
|-| ----- | ---- |
| Daemons, NameNode, DataNode, job trackers, task trackers | start -all.sh | stop -all.sh |
| Map reduce dameons, job tracker, task tracker | start-mapred.sh | stop-mapred.sh |
| DFS daemons, namenode, datanode | start-dfs.sh | stop-dfs.sh |

# Mapper-Reducer working

Divide a task into small parts and assigns them to many computers. Later, the results are collected at one place and integrated to form the result dataset.

## Components

1. **Map**: Generate key-value pairs
2. **Combiner**: Group into identifiable sets
3. **Shuffle and sort**: Reducer tasks begin here and performs sorting by key value
4. **Reducer**: Takes key-value pairs as input
5. **Output phase**: Translates final key value pairs and writes onto a file using record writer
