mode con cols=100 lines=35

d:

cd JJDK\kafka_2.11-2.1.1\bin\windows

chcp 65001

kafka-console-consumer.bat --bootstrap-server bigdata04:9092 --topic campus-user-info-input-test --from-beginning

cmd