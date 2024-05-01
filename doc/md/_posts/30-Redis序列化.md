title: Redis序列化

date: 2021-06-03 15:20:36

tags: Redis

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/30.jpg)

</span>

<!--more-->

# RedisConfig

    ```
    import com.fasterxml.jackson.annotation.JsonAutoDetect;
    import com.fasterxml.jackson.annotation.PropertyAccessor;
    import com.fasterxml.jackson.databind.ObjectMapper;
    import com.fasterxml.jackson.databind.module.SimpleModule;
    import org.joda.time.DateTime;
    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.Configuration;
    import org.springframework.data.redis.connection.RedisConnectionFactory;
    import org.springframework.data.redis.core.RedisTemplate;
    import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
    import org.springframework.data.redis.serializer.RedisSerializer;
    import org.springframework.data.redis.serializer.StringRedisSerializer;
    @Configuration
    public class RedisConfig {
        @Bean
        public RedisTemplate<String, Object> redisTemplate(RedisConnectionFactory factory) {
            RedisTemplate<String, Object> redisTemplate = new RedisTemplate<>();
            redisTemplate.setConnectionFactory(factory);
    
            RedisSerializer<String> redisSerializer = new StringRedisSerializer();
            //key序列化方式
            redisTemplate.setKeySerializer(redisSerializer);
    
            Jackson2JsonRedisSerializer jackson2JsonRedisSerializer = new Jackson2JsonRedisSerializer(Object.class);
            ObjectMapper objectMapper = new ObjectMapper();
            //属性
            objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
            objectMapper.enableDefaultTyping(ObjectMapper.DefaultTyping.NON_FINAL);
            //处理时间
            SimpleModule simpleModule = new SimpleModule();
            simpleModule.addSerializer(DateTime.class, new JodaDateTimeJsonSerializer());
            simpleModule.addDeserializer(DateTime.class, new JodaDateTimeJsonDeSerializer());
            objectMapper.registerModule(simpleModule);
            //注册objectMapper
            jackson2JsonRedisSerializer.setObjectMapper(objectMapper);
            //value序列化
            redisTemplate.setValueSerializer(jackson2JsonRedisSerializer);
            //value hashmap序列化
            redisTemplate.setHashValueSerializer(jackson2JsonRedisSerializer);
            return redisTemplate;
        }
    }
    ```

# JodaDateTimeJsonSerializer

    ```
    import com.fasterxml.jackson.core.JsonGenerator;
    import com.fasterxml.jackson.databind.JsonSerializer;
    import com.fasterxml.jackson.databind.SerializerProvider;
    import org.joda.time.DateTime;
    
    import java.io.IOException;
    
    public class JodaDateTimeJsonSerializer extends JsonSerializer<DateTime> {
        @Override
        public void serialize(DateTime date, JsonGenerator jsonGenerator, SerializerProvider serializerProvider) throws IOException {
            jsonGenerator.writeString(date.toString("yyyy-MM-dd HH:mm:ss"));
        }
    }
    ```

# JodaDateTimeJsonDeSerializer

    ```
    import com.fasterxml.jackson.core.JsonParser;
    import com.fasterxml.jackson.core.JsonProcessingException;
    import com.fasterxml.jackson.databind.DeserializationContext;
    import com.fasterxml.jackson.databind.JsonDeserializer;
    import org.joda.time.DateTime;
    import org.joda.time.format.DateTimeFormat;
    import org.joda.time.format.DateTimeFormatter;
    
    import java.io.IOException;
    
    public class JodaDateTimeJsonDeSerializer extends JsonDeserializer<DateTime> {
    
        @Override
        public DateTime deserialize(JsonParser jsonParser, DeserializationContext deserializationContext) throws IOException, JsonProcessingException {
            String s = jsonParser.readValueAs(String.class);
            DateTimeFormatter dateTimeFormatter = DateTimeFormat.forPattern("yyyy-MM-dd HH:mm:ss");
            return DateTime.parse(s,dateTimeFormatter);
        }
    }
    ```