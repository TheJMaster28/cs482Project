import java.lang.Math;
import java.util.Random;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
public class PlayersBulkCreation {
	public static void main (String [] args) throws IOException {
      
      int size[] = {100, 10000, 100000, 1000000};

      String fileNames[] = new String[size.length];

      for ( int i =0; i < size.length; i++ ) {
         fileNames[i] = "Players" + size[i] + ".txt";
      }
            
      for ( int k=0; k < size.length; k++) {

         int Players = size[k];   // <<<<< ENTER NUMBER OF PLAYERS HERE  <<<<<
      File directory = new File("D:\\"); // << might want to change this to if you want it some where else
      FileWriter file = new FileWriter(new File(directory, fileNames[k]));  // <<<<< CHANGE 
      String firstName[] = new String[] {"Billy", "Bob", "Mike", "Dave", "Jimmy"};                       
      String lastName[] = new String[] {"Jones", "Smith", "Jameson", "Perez", "Nunez"};
      String position[] = new String[] {"WR", "RB", "QB"};
      String teams[] = new String[] {"110011", "220022", "330033", "440044", "550055"};
      
      int playerID   = size[k];  // <<<<<  MUST MATCH PLAYERS COUNT   <<<<<
      int firstNameRange  = 5;
      int lastNameRange   = 5;
      int teamIDRange     = 5;  
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
         tempTeamID = (int)(Math.random() * teamIDRange);
         tempPosition = (int)(Math.random() * positionRange);
         tempTouchdowns = (int)(Math.random() * touchdowns) + 1;
         tempTotalYards = (int)(Math.random() * totalYards) + 1;
         tempSalary = (int)(Math.random() * salary) + 10000;
        
         insertLine = (tempPlayerID + "," + firstName[tempFirstName] + "," + lastName[tempLastName] + "," + teams[tempTeamID] + "," + position[tempPosition] + "," + tempTouchdowns + "," + tempTotalYards + "," + tempSalary + "\n");
         file.write(insertLine);
      }  	
      file.close();	
	}

      }

		
}
