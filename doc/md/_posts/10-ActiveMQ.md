title: ActiveMQ

date: 2021-05-28 15:20:36

tags: MQ

categories: MQ

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/10.jpg)

</span>

<!--more-->

# ActiveMQ介绍

##  连接

```
private static final String url = "tcp://127.0.0.1:61616"; 
private static final String topicName = "topic-list"; 
```

##主题模式生产者

```
//1.创建连接工程
ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
//2.创建Connenction
Connection connection = connectionFactory.createConnection();
//3.启动连接
connection.start();
//4.创建会话
Session session = connection.createSession(false,Session.AUTO_ACKNOWLEDGE);
//5.创建一个目标
Destination destination = session.createTopic(topicName);
//6,。创建生产者
MessageProducer mp = session.createProducer(destination);
for (int i = 0;i<100;i++){
    //7.创建消息
    TextMessage textMessage = session.createTextMessage("TOPIC"+i);
    //8.发送消息
    mp.send(textMessage);
    System.out.println("消息发送成功:"+textMessage.getText());
}
//关闭连接
connection.close();
```	

## 主题模式的消费者
>   主题模式下,消费者无法接收到订阅之前生产者发布的消息，只有先开消费者，再开生产者才能接受消息。

>   队列模式不论先后queue( 将createTopic改成createQueue即为队列模式)

```
ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(url);
//2.创建Connenction
Connection connection = connectionFactory.createConnection();
//3.启动连接
connection.start();
//4.创建会话
Session session = connection.createSession(false,Session.AUTO_ACKNOWLEDGE);
//5.创建一个目标
Destination destination = session.createTopic(topicName);
//6,。创建消费者
MessageConsumer mp = session.createConsumer(destination);
//7.创建一个监听器
mp.setMessageListener(new MessageListener() {
    public void onMessage(Message message) {
        TextMessage textMessage =(TextMessage)message;
        try {
            System.out.println("接收消息："+textMessage.getText());
        } catch (JMSException e) {
            e.printStackTrace();
        }
    }
});	
```


## Spring集成JMS连接ActiveMQ 

>ConnectionFactory 用于管理连接的连接工厂

>>  一个Spring为我们提供的连接池,Spring中提供了SingleConnectionFactory 和 CachingConnectionFactory

>JmsTemplate 用于发送和接受消息的模板类
	
>>  注入即可使用,线程安全,JmsTemplate 每次发送消息都会重新创建连接，会话和productor

>MessageListerner 消息监听器

>>  实现一个onMessage方法，该方法只接受一个Message参数

### common.xml
```
<!--使用注解-->
<context:annotation-config />
<!--配置activeMQ连接工厂-->	
<bean id="activeMQConnectionFactory" class="org.apache.activemq.ActiveMQConnectionFactory">
    <property name="brokerURL" value="tcp://localhost:61616"/>
</bean>
<!--配置spring连接工厂-->
<bean id="connectionFactory" class="org.springframework.jms.connection.SingleConnectionFactory">
    <property name="targetConnectionFactory" ref="activeMQConnectionFactory"/>
</bean>
<!--配置目标地址：使用队列-->
<bean id="queueDestination" class="org.apache.activemq.command.ActiveMQQueue">
   <constructor-arg value="queue"/>
</bean>	
<!--配置目标地址：使用主题模式-->
<bean id="topicDestination" class="org.apache.activemq.command.ActiveMQTopic">
   <constructor-arg value="topic"/>
    </bean>	
```
### consumer.xml
```
<import resource="common.xml"/>
<bean id="consumerContainerListener" class="com.imooc.jms.consumer.ConsumerContainerListener"/>	
<bean id="jmsContainer" class="org.springframework.jms.listener.DefaultMessageListenerContainer">
    <property name="connectionFactory" ref="connectionFactory"/>
    <property name="destination" ref="queueDestination"/>
    <property name="messageListener" ref="consumerContainerListener"/>
</bean>
``` 
### producer.xml
```
<import resource="common.xml"/>
<bean id="jmsTemplate" class="org.springframework.jms.core.JmsTemplate">
    <property name="connectionFactory" ref="connectionFactory"/>
</bean>
<bean class="com.imooc.jms.producer.impl.ProducerServiceImpl"/>
```
		    
    

				











