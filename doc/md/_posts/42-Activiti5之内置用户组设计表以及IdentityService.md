title: Activiti5之内置用户组设计表以及IdentityService

date: 2021-06-04 21:38:36

tags: Activti5

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/42.jpg)

</span>

<!--more-->

# Activiti之内置用户组设计表


* Activiti给我们提供了一套内置的用户和组设计表；
* 用户和组(或者叫做角色)，多对多关联，通过关联表实现；
* 我们来看下，
![](/images/activiti/activiti5/user/8.png)

* 四个表，
    ```
    act_id_group 用户组表；
    act_id_user 用户表；
    act_id_membership 用户与组的关联表，用来实现多对多；
    act_id_info 用户信息表；
    ```
* 首先来看下用户表：
![](/images/activiti/activiti5/user/9.jpg)
* 这里的设计可能和我们想象的不一样，比如_ID，字符串类型 我们直接可以把他当作用户名 
* FIRST_ LAST_ 是英文命名习惯  EMAIL_ PWD 邮箱 密码 字段 等等。
* 接下来看下组表：
![](/images/activiti/activiti5/user/10.jpg)
* ID_  依然是字符串类型 还有NAME_ TYPE_字段
* 再看下重要的关联表：
![](/images/activiti/activiti5/user/11.jpg)
* 只有两个字段 USER_ID_ 和 GROUP_ID_ 分别关联用户表的主键和组表的主键；
* 我们看下架构设计：
![](/images/activiti/activiti5/user/12.jpg)
* 最后一个是用户信息表，主要是用来扩展用户信息，以及可以实现组织机构层次关系，比如雇员领导用户设计；
![](/images/activiti/activiti5/user/13.jpg)
* 这里USE_ID_ 可以关联用户表的主键 KEY_ VALUE_可以扩展用户信息（虽然这个是一种冗余设计），PARENT_ID可以实现层次设计；
* 这个是activiti给我们内置的一个用户组设计，
* 这里说明下：正常的企业级项目都有自己的组织机构用户权限设置表，所以一般不会用到内置的；
* 但是假如一个很小的系统，例如 学生请假系统 就那么几十个用户，两三中角色，那我们就可以用内置的，用内置的更加方便；
* Activiti提供了一个Service来专门操作用户组表，那就是 IdentityService 身份信息Service
* 我们可以用过IdentityService来添加修改用户信息，组信息，也可以删除用户信息，组信息，以及维护他们的关联关系；
    
    ```
    import org.activiti.engine.IdentityService;
    import org.activiti.engine.ProcessEngine;
    import org.activiti.engine.ProcessEngines;
    import org.activiti.engine.identity.Group;
    import org.activiti.engine.identity.User;
    import org.activiti.engine.impl.persistence.entity.GroupEntity;
    import org.activiti.engine.impl.persistence.entity.UserEntity;
    import org.junit.Test;
     
    public class IdentityTest {
     
        /**
         * 获取默认流程引擎实例，会自动读取activiti.cfg.xml文件
         */
        private ProcessEngine processEngine=ProcessEngines.getDefaultProcessEngine();
         
        /**
         * 添加用户测试
         */
        @Test
        public void testSaveUser(){
            IdentityService identityService=processEngine.getIdentityService();
            User user1=new UserEntity(); // 实例化用户实体
            user1.setId("lisi");
            user1.setEmail("234@qq.com");
            user1.setPassword("123456");
            identityService.saveUser(user1); // 添加用户
        }
         
        /**
         * 测试删除用户
         */
        @Test
        public void testDeleteUser(){
            IdentityService identityService=processEngine.getIdentityService();
            identityService.deleteUser("zhangsan"); 
        }
         
        /**
         * 测试添加组
         */
        @Test
        public void testSaveGroup(){
            IdentityService identityService=processEngine.getIdentityService();
            Group group=new GroupEntity(); // 实例化组实体
            group.setId("test");
            identityService.saveGroup(group);
        }
         
        /**
         * 测试删除组
         */
        @Test
        public void testDeleteGroup(){
            IdentityService identityService=processEngine.getIdentityService();
            identityService.deleteGroup("test");
        }
         
        /**
         * 测试添加用户和组关联关系
         */
        @Test
        public void testSaveMembership(){
            IdentityService identityService=processEngine.getIdentityService();
            identityService.createMembership("lisi", "test");
        }
         
        /**
         * 测试删除用户和组关联关系
         */
        @Test
        public void testDeleteMembership(){
            IdentityService identityService=processEngine.getIdentityService();
            identityService.deleteMembership("lisi", "test");
        }
     
    }
    ```

# 来源地址

> [java1234.com](http://blog.java1234.com/blog/articles/84.html)