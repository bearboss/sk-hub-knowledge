title: springMvc参数绑定

date: 2021-05-28 15:20:36

tags: SpringBoot

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/18.jpg)

</span>

<!--more-->
# 简介
## 多实体含有同属性

>  比如都含有name

	http://localhost:8080/springmvc/object.do?user.name=Tom&admin.name=Lucy&age=10 
	@InitBinder("user")
	public void initUser(WebDataBinder binder){
		binder.setFieldDefaultPrefix("user.");
	}
	@InitBinder("admin")
	public void initAdmin(WebDataBinder binder){
		binder.setFieldDefaultPrefix("admin.");
	}
	
## List绑定

	不能直接使用
	public void xx(List<User> user){

	}
	应该建一个数据收集类
    public class UserListFrom(){
        private List<User> users
        get set 方法
    }
    #mvc绑定list
    public void xx(UserListFrom user){

    }
    
## Set 绑定

	类需要定义Set的大小		
    public class UserSetForm(){
        private Set<User> users
        private UserSetForm(){ //有几个就定义几个Set
            users = new LinkedHashSet();
            users.add(new User);
            users.add(new User);
        }
        get set 方法
    }
    
    #mvc绑定Set
    public void xx(UserSetForm user){

    }
    
## Map 绑定  

- 同上

## json绑定
 
- @RequestBody

## xml绑定   

- 需要spring-oxm依赖
- 控制器 @RequestBody   
- 实体类   
- - 根节点 @XmlRootElement(name="user")
- - 子节点 @XmlElement(name="name")	
- - 子节点 @XmlElement(name="age")	

# 示例

* resf风格@ - /hello/100/say 

```
@RequestMapping(value = "/{id}/say",method = RequestMethod.GET)
public String say(@PathVariable("id") int id ){
    return String.valueOf(id);
}
```

* 普通传参 -	/hello/say?id=100

```
@RequestMapping(value = "/say",method = RequestMethod.GET)
public String say(@RequestParam(value = "id",required = false ,defaultValue = "0") int id ){
    return String.valueOf(id);
}
```


* 请求body
	
```
@PostMapping("/create")
public ResultJson create(@RequestBody @Validated dto dto) {
   
}
``` 

* 请求RequestPart

```
@PostMapping("/create")
public ResultJson create(@RequestPart @Validated dto dto) {
   
}
```

# 返回参数绑定


## 作用域

> 只实例化一个bean对象（即每次请求都使用同一个bean对象），默认是singleton

    @Scope(value="singleton") 

## 通过ModelAndView返回用户信息数据到页面
	
	/**
	 * 方式一，通过ModelAndView返回用户信息数据到页面
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/ModelAndView", method=RequestMethod.GET)
	private ModelAndView getUserInfo(@PathVariable("userId") Integer userId){
		User user = userService.getUserById(userId);
		return new ModelAndView("userinfo", "user", user);
	}
	/**
	 * 方式二，通过Model返回用户信息数据到页面
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/Model", method=RequestMethod.GET)
	private String getUserInfo(@PathVariable("userId") Integer userId, Model model){
		User user = userService.getUserById(userId);
		model.addAttribute("user", user);
		return "userinfo";
	}
	/**
	 * 方式三，通过ModelMap返回用户信息数据到页面
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/ModelMap", method=RequestMethod.GET)
	private String getUserInfo(@PathVariable("userId") Integer userId, ModelMap model){
		User user = userService.getUserById(userId);
		model.addAttribute("user", user);
		return "userinfo";
	}
	
	/**
	 * 方式四，通过Map返回用户信息数据到页面
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/Map", method=RequestMethod.GET)
	private String getUserInfo(@PathVariable("userId") Integer userId, Map<String,Object> model){
		User user = userService.getUserById(userId);
		model.put("user", user);
		return "userinfo";
	}
	/**
	 * 方式五，通过@SessionAttributes将指定key的模型数据存到HttpSession，让页面可以获取
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/SessionAttributes", method=RequestMethod.GET)
	private ModelAndView getUserInfo(@PathVariable("userId") Integer userId){
		User user = userService.getUserById(userId);
		return new ModelAndView("userinfo", "user", user);
	}
    /**
	 * 方式六，通过@SessionAttributes将指定key的模型数据存到HttpSession，让页面可以获取
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/ModelAttribute", method=RequestMethod.GET)
	private String getUserInfo(@PathVariable("userId") Integer userId){
		return "userinfo";
	}
	/**
	 * 方式七，直接将数据存到HttpSession，让页面可以获取
	 * @param userId
	 * @param session
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/HttpSession", method=RequestMethod.GET)
	private String getUserInfo(@PathVariable("userId") Integer userId, HttpSession session){
		User user = userService.getUserById(userId);
		session.setAttribute("user", user);
		return "userinfo";
	}
	/**
	 * 方式八，直接将数据存到HttpServletRequest，让页面可以获取
	 * @param userId
	 * @param session
	 * @return
	 */
	@RequestMapping(value="/view/{userId}/use/HttpServletRequest", method=RequestMethod.GET)
	private String getUserInfo(@PathVariable("userId") Integer userId, HttpServletRequest request){
		User user = userService.getUserById(userId);
		request.setAttribute("user", user);
		return "userinfo";
    }



