import java.io.*;

public class CopyFile {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: CopyFile <source-file> <destination-file>");
            System.exit(1);
        }
        
        try {
            // create a new file to copy the contents into
            File sourceFile = new File(args[0]);
            File destFile = new File(args[1]);
            if (!sourceFile.exists()) {
                System.out.println("Source file does not exist.");
                System.exit(1);
            }
            
            // copy the contents of the source file to the destination file
            FileInputStream inputStream = new FileInputStream(sourceFile);
            FileOutputStream outputStream = new FileOutputStream(destFile);
            byte[] buffer = new byte[1024];
            int length;
            while ((length = inputStream.read(buffer)) > 0) {
                outputStream.write(buffer, 0, length);
            }
            inputStream.close();
            outputStream.close();
            
            // display contents of the destination file on the screen
            inputStream = new FileInputStream(destFile);
            byte[] data = new byte[(int) destFile.length()];
            inputStream.read(data);
            inputStream.close();
            String content = new String(data, "UTF-8");
            System.out.println(content);
            
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
