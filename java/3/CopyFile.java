import java.io.*;

public class CopyFile{
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
            FileReader reader = new FileReader(sourceFile);
            FileWriter writer = new FileWriter(destFile);
            int character;
            while ((character = reader.read()) != -1) {
                writer.write(character);
            }
            reader.close();
            writer.close();
            
            // display contents of the destination file on the screen
            reader = new FileReader(destFile);
            BufferedReader bufferedReader = new BufferedReader(reader);
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
            bufferedReader.close();
            
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
