# Serial-War

A benchmark project of Avro, JSON, Protocol Buffer created at Insight.
Slides can be checked at http://www.slideshare.net/XuechaoWu/xuechao-serial-war-63753460
The dashboard currently has no data feed. Leave an issue for a live demo.

+ Metrics
  + Use raw JSON, data serialized in avro and data serialized in protocol buffer to benchmark their performance under
    - High volume throughput
    - Narrow/Wide/Nested data type
    - real-time MapReduce

+ Data Source
  - JSON formatted
  - real-time data from Twitter Streaming API
  - Synthesized person info data
  
+ Ingestion
  - 3 different producers into 3 topics
    - avro
    - json
    - protobuf
  
+ Stream Processing
  - Spark Streaming API 
  
+ Cache
  - Redis cluster
  
+ API
  - Written in Flask

+ Front-End
  - Bootstrap, d3.js and highcharts.js
