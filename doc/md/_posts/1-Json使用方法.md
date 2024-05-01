title: Json使用规范

date: 2021-05-25 15:20:36

tags: [Json,Java]

categories: Json

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/1.jpg)

</span>

<!--more-->

<h1 id="json-lib-2.4-jdk15">json-lib-2.4-jdk15使用</h1>

    import java.util.ArrayList;
    import java.util.HashMap;
    import net.sf.json.JSONArray;
    import net.sf.json.JSONObject;
    public class JsonCombine {
    	public static void main(String[] args) {
    		JSONObject jsonOne = new JSONObject();
    		jsonOne.put("name", "kewen");
    		jsonOne.put("age", "24");
    		JSONObject jsonTwo = new JSONObject();
    		jsonTwo.put("hobbit", "Doto");
    		jsonTwo.put("hobbit2", "wow");
    		JSONObject jsonThree = new JSONObject();
    		jsonThree.putAll(jsonOne);
    		jsonThree.putAll(jsonTwo);
    		System.out.println(jsonThree.toString());
    	
    		// JsonObject和JsonArray区别就是JsonObject是对象形式，JsonArray是数组形式
    		// 创建JsonObject第一种方法
    		JSONObject jsonObject = new JSONObject();
    		jsonObject.put("UserName", "ZHULI");
    		jsonObject.put("age", "30");
    		jsonObject.put("workIn", "ALI");
    		System.out.println("jsonObject1：" + jsonObject);
    	
    		// 创建JsonObject第二种方法
    		HashMap<String, String> hashMap = new HashMap<String, String>();
    		hashMap.put("UserName", "ZHULI");
    		hashMap.put("age", "30");
    		hashMap.put("workIn", "ALI");
    		System.out.println("jsonObject2：" + JSONObject.fromObject(hashMap));
    	
    		// 创建一个JsonArray方法1
    		JSONArray jsonArray = new JSONArray();
    		jsonArray.add(0, "ZHULI");
    		jsonArray.add(1, "30");
    		jsonArray.add(2, "ALI");
    		System.out.println("jsonArray1：" + jsonArray);
    	
    		// 创建JsonArray方法2
    		ArrayList<String> arrayList = new ArrayList<String>();
    		arrayList.add("ZHULI");
    		arrayList.add("30");
    		arrayList.add("ALI");
    		System.out.println("jsonArray2：" + JSONArray.fromObject(arrayList));
    		// 如果JSONArray解析一个HashMap
    		System.out.println("jsonArray FROM HASHMAP：" + JSONArray.fromObject(hashMap));
    		// 组装一个复杂的JSONArray
    		JSONObject jsonObject2 = new JSONObject();
    		jsonObject2.put("UserName", "ZHULI");
    		jsonObject2.put("age", "30");
    		jsonObject2.put("workIn", "ALI");
    		jsonObject2.element("Array", arrayList);
    		jsonObject2.element("Map", hashMap);
    		System.out.println("jsonObject2：" + jsonObject2);
    	
    		// 将Json字符串转为java对象
    		String jsonString = "{\"UserName\":\"ZHULI\",\"age\":\"30\",\"workIn\":\"ALI\",\"Array\":[\"ZHULI\",\"30\",\"ALI\"]}";
    		JSONObject obj = JSONObject.fromObject(jsonString);
    		if (obj.has("UserName")) {
    			System.out.println("UserName:" + obj.getString("UserName"));
    		}
    		if (obj.has("Array")) {
    			JSONArray transitListArray = obj.getJSONArray("Array");
    			for (int i = 0; i < transitListArray.size(); i++) {
    				System.out.println("Array:" + transitListArray.getString(i) + " ");
    	
    			}
    		}
    	}
    }



<h1 id="org.json">org.json使用</h1>

	<dependency>
	  <groupId>org.json</groupId>
	  <artifactId>json</artifactId>
	  <version>20180130</version>
	</dependency>
	(1)使用普通设置
	JSONObject jsonObject = new JSONObject();
	jsonObject.put("name","张三");
	jsonObject.put("sex",false);
	jsonObject.put("sex",new String[]{"dsd","富士达","fdsfd"});
	String s = jsonObject.toString();
	System.out.println(s);
	（2）使用map或者实体
	Page u = new Page();
	new JSONObject(u).toString()
	#读json文件
	<dependency>
	   <groupId>commons-io</groupId>
	   <artifactId>commons-io</artifactId>
	   <version> 2.6 </version>
   	</dependency>

   	File file = new File(xx.class.getResource("/json.json").getFile());
   	String s = fileUtil.readFileToString(file);
   	JSONObject jsonobject = new JSONObject(s);
   	System.out.println(jsonobject.getInt("id"));

<h1 id="gson">gson使用</h1>

	<dependency>
	  <groupId>com.google.code.gson</groupId>
	  <artifactId>gson</artifactId>
	  <version>2.8.5</version>
	</dependency>
	Page u = new Page();
	new Gson().toJson(u)
	#读json文件-对应java实体been
	<dependency>
	   <groupId>commons-io</groupId>
	   <artifactId>commons-io</artifactId>
	   <version> 2.6 </version>
	</dependency>
	
	File file = new File(xx.class.getResource("/json.json").getFile());
	String s = fileUtil.readFileToString(file);
	Gson gson= new Gson();
	Page page = gson.fromJson(s,Page.class);
	System.out.println(page);   


<h1 id="fastJson">fastJson</h1>

    #JSON类型
        JSON.toJavaObject((JSON) json.getResult(), clazz);
    #jSONObject
        String jsonString = JSON.toJSONString(jsonObject);
        MatterVO vo = JSON.parseObject(jsonString, MatterVO.class);






