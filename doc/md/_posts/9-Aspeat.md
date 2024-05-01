title: Aspeat

date: 2021-05-28 15:20:36

tags: Aop

categories: Aop

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/9.jpg)

</span>

<!--more-->

# Aspeat介绍

- 匹配类包
- - within
- 匹配对象 拦截对象里面的方法 
- - this target bean
- 匹配参数	
- - execution arg
- 匹配注解 
- - annotation
- execution表达式 
    ``` 
    execution( modifier-pattern? ret-type-pattern
      declarin-type-pattern? name-pattern(param-pattern) throw-pattern? )
    
    @Aspect 
    @Component
    public class ExecutionAspectConfig{
        #匹配public方法 service包（service.*）和service子包（service..*）
        #下面的所有service 参数为任意
        @Pointcut("execution(public * com.imooc.service..*Service.*(..))")
        public void matchCondition(){}
    
    
        @Before ("matchCondition()")
        public void before(){
    
        }
    }
    ```	
- AOP实现原理(接口那种) 
    ```
    JDK 代理
        类:java.lang.reflect.Proxy
        实现接口:InvocationHandler
        只能基于接口进行动态代理
    cglib动态代理
        实现MethodInterceptor接口
        使用invokeSuper方法
    对比：
        JDK只能针对有接口的类的接口方法进行动态代理
        Cglib基于继承来实现代理，无法对static,final类进行代理
        无法对private,static进行代理
    ```
- Spring aop
    ```
    如果目标对象实现了接口，则默认采用JDK动态代理,反之用Cglib
    如果实现接口，强制使用cglib代理，则用cglib（proxy-target-class="true"）
    ```

				











