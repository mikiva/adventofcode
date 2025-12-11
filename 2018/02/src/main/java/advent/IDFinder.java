package advent;

import java.util.Set;

public class IDFinder {

	public static String checkID(String id, Set<String> list)
	{
		String idFromList = null;
		for(String s : list)
		{
			int diff = 0;
			for(int i = 0; i < s.length(); i++)
			{
				
				if(!(id.charAt(i) == s.charAt(i)))
					diff++;

			}

			if(diff == 1)
			{
				idFromList = finalizeID(id, s);
				break;
			}
		}
		
		return idFromList;
	}
	
	private static String finalizeID(String id, String s)
	{
		StringBuilder finalID = new StringBuilder();
		
		for(int i = 0; i < id.length(); i++)
		{
			if(id.charAt(i) == s.charAt(i))
				finalID.append(id.charAt(i));
		}
		
		
		
		
		return finalID.toString();
	}
}
