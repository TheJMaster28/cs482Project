import java.lang.Math;
import java.util.Random;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
public class PlayersBulkCreation {
	public static void main (String [] args) throws IOException {
		
		int Players = 1000000;   // <<<<< ENTER NUMBER OF PLAYERS HERE  <<<<<
      File directory = new File("D:\\");
      FileWriter file = new FileWriter(new File(directory, "Players1000000.txt"));  // <<<<< CHANGE 
      String firstName[] = new String[] {"Billy", "Bob", "Mike", "Dave", "Jimmy"};                       
      String lastName[] = new String[] {"Jones", "Smith", "Jameson", "Perez", "Nunez"};
      String position[] = new String[] {"WR", "RB", "QB"};
      
      int playerID   = 1000000;  // <<<<<  MUST MATCH PLAYERS COUNT   <<<<<
      int firstNameRange  = 5;
      int lastNameRange   = 5;
      int teamID     = 3000000;  // <<<<<  MUST BE TRIPLE PLAYERS COUNT <<<<<
      int positionRange   = 3;
      int touchdowns = (1000 - 1) + 1;
      int totalYards = (1000 - 1) + 1;
      int salary     = (70000 - 10000) + 1;
      int tempPlayerID, tempFirstName, tempLastName, tempTeamID, tempPosition, tempTouchdowns, tempTotalYards, tempSalary;
      String insertLine = " ";
      for (int i = 0; i < Players; i++) {
         tempPlayerID = playerID++;
         tempFirstName = (int)(Math.random() * firstNameRange);
         tempLastName = (int)(Math.random() * lastNameRange);
         tempTeamID = teamID++;
         tempPosition = (int)(Math.random() * positionRange);
         tempTouchdowns = (int)(Math.random() * touchdowns) + 1;
         tempTotalYards = (int)(Math.random() * totalYards) + 1;
         tempSalary = (int)(Math.random() * salary) + 10000;
        
         insertLine = ("\"" + tempPlayerID + "\", \"" + firstName[tempFirstName] + "\", \"" + lastName[tempLastName] + "\", \"" + tempTeamID + "\", \"" + position[tempPosition] + "\", \"" + tempTouchdowns + "\", \"" + tempTotalYards + "\", \"" + tempSalary + "\"\n");
         file.write(insertLine);
      }  	
      file.close();	
	}
}
