title: Java文件重命名

date: 2021-05-25 15:20:36

tags: Java

categories: Java

copyright: true

sticky: 0

---

<span id="delete">

![](/images/banner/5.jpg)

</span>

<!--more-->

# 文件目录
## 文件重命名 

    public static void main(String[] args) {
        String d = "E:/images";
        File file = new File(d);
        File[] files = file.listFiles();
        int i = 1;
        for (File file1 : files) {
            reName(file1, i);
            i++;
        }
    }
    /**
    * 处理文件重命名
    */
    private static boolean reName(File file, int i) {//文件重命名
        if (file.exists()) {
    
            File newFile = new File(file.getParent() + File.separator + i + ".jpg");
            if (newFile.exists()) {
                return false;
            }
            if (file.renameTo(newFile)) {
                System.out.println("重命名成功！");
                return true;
            } else {
                System.out.println("重命名失败！新文件名已存在");
                return false;
            }
        } else {
            System.out.println("重命名文件不存在！");
            return false;
        }
    
    }
    
    #加载文件
    ClassLoader classLoader = getClass().getClassLoader();
    InputStream inputStream = classLoader.getResourceAsStream("relative/path/to/resource.file");
    
    InputStream is = ChinaPayUtil.class.getResourceAsStream("/security.properties");
    try {
    	properties.load(is);
    } catch (IOException e) {
    e.printStackTrace();
    }
    #第二种
    #windows下/data/app/cert是在当前项目的盘符下:c盘
    #linux是完整路径
    FileInputStream fis = new FileInputStream("/data/app/cert");
            
    
# doris导入
```

public static String getPhone() {
		String[] start = {"130", "131", "132", "133", "134", "150", "151", "155", "158", "166", "180", "181", "184", "185", "188"};
		return start[(int) (Math.random() * start.length)] + (10000000 + (int) (Math.random() * (99999999 - 10000000 + 1)));
	}


	@SneakyThrows
	public static void main(String[] args) {
		for (int i = 1; i <= 20; i++) {
			int number = i + 1500;
			System.out.println("number:" + number);
			loop(number);
		}
	}

	public static void loop(int number) throws Exception {
		File castFile = new File("C:\\Users\\MX\\Desktop\\cast10.txt");
		if (castFile.exists()) {
			castFile.delete();
		}
		castFile.createNewFile();
		FileWriter castFileWritter = new FileWriter(castFile, true);
		BufferedWriter castFilebufferWritter = new BufferedWriter(castFileWritter);


		File middleFile = new File("C:\\Users\\MX\\Desktop\\middle.txt");
		if (middleFile.exists()) {
			middleFile.delete();
		}
		middleFile.createNewFile();
		FileWriter middleFileWritter = new FileWriter(middleFile, true);
		BufferedWriter middleFileWritterbufferWritter = new BufferedWriter(middleFileWritter);

		for (int i = number; i <= (number + 1500); i++) {
			//输出到文件
			castFilebufferWritter.append("\n");
			middleFileWritterbufferWritter.append("\n");
			String phone = getPhone();
			String cast10 = i + "," + i + ",nc_cust_id," + i + ",cust_name,nick_name,cust_code,certificate_type,certificate_type_name,certificate_id," + phone + ",cust_address,password,2022-01-01,1,head_portrait,cust_channel,sex,sex_name,attr,attribute_type_name,home_phone,email,qq,2022-01-01,defadminarea,marr,marriage_name,employment,employee,employee_address,employee_phone,link_man,link_phone,label,label_name,label_note,note,1,2022-01-01,1,2022-01-01,9999,1,1,from_obj_id,2022-01-01,1,wx_app_openid,2022-01-01,mdm_code,1,cancel_account_reason,union_id,user_id_apple,1,2022-01-01,111111111";
			String middle = i + "," + phone + ",1,2023-10-18 11:20:24,2023-10-18 11:20:26,mx,mx,1,1,1,0,2023-10-18 11:20:41";
			castFilebufferWritter.append(cast10);
			middleFileWritterbufferWritter.append(middle);
		}

		castFilebufferWritter.close();
		castFileWritter.close();

		middleFileWritterbufferWritter.close();
		middleFileWritter.close();

		// 发送数据
		excmd();
	}

	public static void excmd() throws Exception {
		String label = String.valueOf(System.currentTimeMillis());

		String cmd1 = "curl --location-trusted -u root:Xhwl.@2023 -H \"label:" + label + "\" -H \"timeout:100000\" -H \"exec_mem_limit:200000000\" -H \"column_separator:,\" -T C:\\\\Users\\\\MX\\\\Desktop\\\\cast10.txt http://10.51.34.209:8040/api/ods_per/ods_per_customer_cust_10/_stream_load";
		Process exec = Runtime.getRuntime().exec(cmd1);
		getLine(exec.getInputStream());

		Thread.sleep(500);
		String cmd2 = "curl --location-trusted -u root:Xhwl.@2023 -H \"label:" + label + "\" -H \"timeout:100000\" -H \"exec_mem_limit:200000000\" -H \"column_separator:,\" -T C:\\\\Users\\\\MX\\\\Desktop\\\\middle.txt http://10.51.34.209:8040/api/ods_per/ods_per_customer_wecom_uni_cent_wechat_uni_we_customer_middle/_stream_load";
		Runtime.getRuntime().exec(cmd2);

		Thread.sleep(1500);
	}
	
	/**
	 * 打印
	 */
	private static List<String> getLine(InputStream inputStream) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(inputStream, StandardCharsets.UTF_8));
		List<String> lines = new LinkedList<>();
		String line;
		while ((line = br.readLine()) != null) {
			lines.add(line);
		}
		inputStream.close();
		return lines;
	}
```









