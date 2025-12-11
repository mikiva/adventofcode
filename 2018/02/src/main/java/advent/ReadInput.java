package advent;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ReadInput {
	
	private static List<String> input = readInput();
	
	public static List<String> readInput()
	{
		List<String> in = new ArrayList<>();
		ClassLoader classLoader = ReadInput.class.getClassLoader();
		
		File file = new File(classLoader.getResource("input.txt").getFile());
		
		try (Scanner scanner = new Scanner(file) ){
			while(scanner.hasNextLine()) {
				String line = scanner.nextLine();
				in.add(line);
			}
		}
		catch(FileNotFoundException e)
		{
			e.printStackTrace();
		}
		
		return in;
		
	}
	

	public static List<String> getInput()
	{
		return input;
	}
	
}
