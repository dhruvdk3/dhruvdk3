import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Student {
    public static void main(String[] args) {
        // Open the file for writing
        File file = new File("students.txt");
        try {
            FileWriter writer = new FileWriter(file);

            Scanner scanner = new Scanner(System.in);
            for (int i = 1; i <= 5; i++) {
                System.out.print("Enter name and marks of student " + i + ": ");
                String line = scanner.nextLine();
                writer.write(line + "\n");
            }

            writer.close();
            scanner.close();

        } catch (IOException e) {
            System.out.println("Error writing to file: " + e.getMessage());
        }

        try {
            Scanner scanner = new Scanner(file);

            int count = 0;
            double sum = 0;

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] parts = line.split(" ");
                double marks = Double.parseDouble(parts[1]);

                sum += marks;
                count++;
            }

            double average = sum / count;
            System.out.println("Average marks: " + average);

            scanner.close();

        } catch (Exception e) {
            System.out.println("File not found: " + e.getMessage());
        }
    }
}
