FROM apache/dolphinscheduler-worker
LABEL maintainer="xx@qq.com"

ADD mysql-connector-j-8.0.33.jar /opt/dolphinscheduler/libs/

RUN rm -rf /opt/dolphinscheduler/bin/start.sh

COPY start.sh /opt/dolphinscheduler/bin/start.sh

RUN apt-get -y install curl
