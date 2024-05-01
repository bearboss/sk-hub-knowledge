import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.io.UnsupportedEncodingException;
import java.util.Base64;

public class Doris {
    public static void main(String[] args) throws Exception {
    
       String filePath = "C:\\Users\\MX\\Desktop\\doris-template-admin.sh";
       FileInputStream fileInputStream = new FileInputStream(filePath);
       List<String> lines = getLine(fileInputStream);

       String dorisHost = "10.51.34.149";
       String dorisPort = "9030";
       String dorisUser = "root";
       String dorisPwd = "Xhwl.@2023";

       String user = "admin";
       String domain = "%";
       String pwd = "{bcrypt}$2a$10$fADSOoOytpgFd1hB2PT/3OK2Z7bofYc4TibP4O7vXtlgoVJzUZQ1G";
       String database = "admin_database";
       String table = "admin_database_table";
       String replicationNum = "1";

       String copyFilePath = "C:\\Users\\MX\\Desktop\\doris.sh";
       File file = new File(copyFilePath);
       if (file.exists()) {
          file.delete();
       }
       file.createNewFile();
       FileOutputStream fileOutputStream = new FileOutputStream(file);
       for (String line : lines) {
          String replace = line.replace("${dorisHost}", dorisHost)
                .replace("${dorisPort}", dorisPort)
                .replace("${dorisUser}", dorisUser)
                .replace("${dorisPwd}", dorisPwd)
                .replace("${user}", user)
                .replace("${domain}", domain)
                .replace("${pwd}", encoder(pwd))
                .replace("${database}", database)
                .replace("${table}", table)
                .replace("${replicationNum}", replicationNum)
                + "\n";
          fileOutputStream.write(replace.getBytes(StandardCharsets.UTF_8));
       }
       fileOutputStream.close();

       String command = "sh " + copyFilePath;
       Process process = Runtime.getRuntime().exec(command);
       int exitCode = process.waitFor();
       if (exitCode != 0) {
          System.out.println("doris fail!!" + Arrays.toString(getLine(process.getErrorStream()).toArray()));
       } else {
          file.delete();
       }
       System.out.println("doris success!!");
    }

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

      /**
    * 加密
    */
   public static String encoder(String text) {
      Base64.Encoder encoder = Base64.getEncoder();
      String encodedText = "";
      try {
         byte[] textByte = text.getBytes("UTF-8");
         encodedText = encoder.encodeToString(textByte);
         encodedText = encodedText.replaceAll("\r\n", "").replaceAll("=", "");
      } catch (UnsupportedEncodingException e) {
         e.printStackTrace();
      }
      return encodedText;
   }
}