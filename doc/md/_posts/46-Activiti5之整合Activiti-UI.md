title: Activiti5之整合Activiti-UI

date: 2021-06-10 12:01:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/46.jpg)

</span>

<!--more-->

# Activiti5之整合Activiti-UI

> 在上一节整合了springboot之后

> pom.xml

    ```
    <!-- Activiti 流程图 -->
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-diagram-rest</artifactId>
            <version>${activiti.version}</version>
        </dependency>
        <!-- Activiti 在线设计 -->
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-modeler</artifactId>
            <version>${activiti.version}</version>
        </dependency>
    ```
 
> 拷贝Activiti-activiti-5.22.0\modules\activiti-webapp-explorer2\src\main\webapp,
> Activiti-activiti-5.22.0\modules\activiti-webapp-explorer2\src\main\resources\stencilset.json
> 到项目/resources/activiti-ui 

* diagram-viewer
* editor-app 
* modeler.html 
* stencilset.json

> Activiti-activiti-5.22.0\modules\activiti-modeler\src\main\java\org\activiti\rest\edit进行拷贝

* ModelEditorJsonRestResource #渲染页面查询模型id相关的数据;
* ModelSaveRestResource #保存模型(并不会部署);
* StencilsetRestResource #寻找页面汉化字体;

> 修改访问路径

    ```
    app-cfg.js
    
    ACTIVITI.CONFIG = {
        'contextRoot' : 'activiti-webapp-explorer2/service',
    };
     
    改为 
     
    ACTIVITI.CONFIG = {
        'contextRoot' : 'service',
    };
    ```
 
> 拷贝的文件统一增加访问前缀 @RequestMapping("/service")

> 增加入口访问 - 建一个控制器

    ```
    @RestController
    @RequestMapping("/activiti")
    public class ActivitiController {
        /**
         * 创建模型
         */
        @RequestMapping("/create")
        public void create(HttpServletRequest request, HttpServletResponse response) {
            try {
                ProcessEngine processEngine = ProcessEngines.getDefaultProcessEngine();
    
                RepositoryService repositoryService = processEngine.getRepositoryService();
    
                ObjectMapper objectMapper = new ObjectMapper();
                ObjectNode editorNode = objectMapper.createObjectNode();
                editorNode.put("id", "canvas");
                editorNode.put("resourceId", "canvas");
                ObjectNode stencilSetNode = objectMapper.createObjectNode();
                stencilSetNode.put("namespace", "http://b3mn.org/stencilset/bpmn2.0#");
                editorNode.put("stencilset", stencilSetNode);
                Model modelData = repositoryService.newModel();
                
                ObjectNode modelObjectNode = objectMapper.createObjectNode();
                modelObjectNode.put(ModelDataJsonConstants.MODEL_NAME, "创建模型");
                modelObjectNode.put(ModelDataJsonConstants.MODEL_REVISION, 1);
                String description = "创建模型";
                modelObjectNode.put(ModelDataJsonConstants.MODEL_DESCRIPTION, description);
                modelData.setMetaInfo(modelObjectNode.toString());
                modelData.setName("创建模型");
                modelData.setKey("创建模型");
    
                //跳转模型前端界面
                repositoryService.saveModel(modelData);
                repositoryService.addModelEditorSource(modelData.getId(), editorNode.toString().getBytes("utf-8"));
                response.sendRedirect(request.getContextPath() + "/activiti-ui/modeler.html?modelId=" + modelData.getId());
            } catch (Exception e) {
                System.out.println("创建模型失败：");
            }
        }
    }
    ```

> 如果不想用权限 

    ```
    @SpringBootApplication(exclude = {SecurityAutoConfiguration.class,
            org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration.class
    })
    ```

>增加内存用户权限

    ```
    @Configuration
    public class SpringSecuityConfiguration {
        private Logger logger = LoggerFactory.getLogger(SpringSecuityConfiguration.class);
        @Bean
        public UserDetailsService myUserDetailsService() {
            InMemoryUserDetailsManager inMemoryUserDetailsManager = new InMemoryUserDetailsManager();
            String[][] usersGroupsAndRoles = {
                    {"bob", "test", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
                    {"bajie", "test", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
                    {"wukong", "test", "ROLE_ACTIVITI_USER", "GROUP_activitiTeam"},
                    {"other", "test", "ROLE_ACTIVITI_USER", "GROUP_otherTeam"},
                    {"system", "test", "ROLE_ACTIVITI_USER"},
                    {"admin", "test", "ROLE_ACTIVITI_ADMIN"},
            };
    
            for (String[] user : usersGroupsAndRoles) {
                List<String> authoritiesStrings = asList(Arrays.copyOfRange(user, 2, user.length));
                logger.info("> Registering new user: " + user[0] + " with the following Authorities[" + authoritiesStrings + "]");
                inMemoryUserDetailsManager.createUser(new User(user[0], passwordEncoder().encode(user[1]),
                        authoritiesStrings.stream().map(s -> new SimpleGrantedAuthority(s)).collect(Collectors.toList())));
            }
            return inMemoryUserDetailsManager;
        }
        @Bean
        public PasswordEncoder passwordEncoder() {
            return new BCryptPasswordEncoder();
        }
    }
    ```
>增加数据库用户权限

    ```
    @Component
    public class MyUserDetailsService implements UserDetailsService {
        @Autowired
        UserInfoBeanMapper userInfoBeanMapper;
    
        @Override
        public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
    //      String password = passwordEncoder().encode("test");
    //      return new User(username, password,
    //      AuthorityUtils.commaSeparatedStringToAuthorityList("ROLE_ACTIVITI_USER"));
    
            //读取数据库判断用户
            UserInfoBean userInfoBean = userInfoBeanMapper.selectByUserName(username);
            if (Objects.isNull(userInfoBean)) {
                throw new UsernameNotFoundException("数据库中无此用户");
            }
            //如果用户是null抛出异常
            //返回异常
            return userInfoBean;
        }
    
        @Bean
        public PasswordEncoder passwordEncoder() {
            return new BCryptPasswordEncoder();
        }
    }
    ```
> 增加额外的功能 - 比如自动保存模型并发布

> > 在 ModelSaveRestResource 方法中进行改造,前端传来标识,只保存还是保存并发布

```
 if("true".equals(check)){
        //发布模型
        ObjectNode modelNode = (ObjectNode) new ObjectMapper()
                .readTree(repositoryService.getModelEditorSource(model.getId()));
        byte[] bpmnBytes = null;

        BpmnModel bpmnModel = new BpmnJsonConverter().convertToBpmnModel(modelNode);
        bpmnBytes = new BpmnXMLConverter().convertToXML(bpmnModel);
        String processName = model.getName() + ".bpmn";
        Deployment deployment = repositoryService.createDeployment()
                .name(model.getName()).addString(processName, new String(bpmnBytes,"UTF-8"))
                .deploy();
 }
```
> typeError: Cannot read property 'namespace' of undefined分析：可能是如下原因引起的

> >spring boot默认使用jackson作为解析json框架，如果配置使用阿里的fastjson的话，Activiti modoler会显示出问题

> > 解决方案：使用默认的jackson即可