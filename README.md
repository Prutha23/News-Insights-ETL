# News-Insights-ETL

- Organizations often gain data from multiple sources, filter and clean it and then load the data onto different systems for visualizations and analysis. Over time, many of these systems may become disconnected and not performing optimally. 

- In this project, I am trying to combine data from multiple sources into one or more other sources. The go-to technologies for transferring data are often Apache Kafka and Spark Streaming. So, in this Project I am creating an ETL pipeline using Spark Streaming and different data sources.

- Steps followed for the ETL process are:
  1. Setup a Kafka broker with Zookeeper
  2. Integrate NewsAPI in python code
  3. Setup Kafka producer to ingest articles
  4. Setup Spark Streaming to read articles

- Additional pipeline component added to the ETL process is Hive table to read data and do queries in Hive.
