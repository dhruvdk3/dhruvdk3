import java.io.*;

public class MergeFiles {
    public static void main(String[] args) {
        try {
            // take input from the user for two file names
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            System.out.print("Enter the name of the first file: ");
            String file1 = reader.readLine();
            System.out.print("Enter the name of the second file: ");
            String file2 = reader.readLine();
            
            // create a new file to store the merged content
            System.out.print("Enter the name of the merged file: ");
            String mergedFile = reader.readLine();
            FileWriter writer = new FileWriter(mergedFile);
            
            // read contents of first file and write to merged file
            FileReader fileReader = new FileReader(file1);
            int character;
            while ((character = fileReader.read()) != -1) {
                writer.write(character);
            }
            fileReader.close();
            
            // read contents of second file and write to merged file
            fileReader = new FileReader(file2);
            while ((character = fileReader.read()) != -1) {
                writer.write(character);
            }
            fileReader.close();
            
            // close writer
            writer.close();
            
            System.out.println("Merged content of " + file1 + " and " + file2 + " into " + mergedFile);
            
        } catch (IOException e) {
            System.out.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
