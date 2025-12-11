package advent;

import java.util.LinkedHashSet;
import java.util.Set;

public class ID {

	private String id;
	private boolean hasExactlyTwo;
	private boolean hasExactlyThree;
	
	public ID() {}
	public ID(String id) {
		this.id = id;
		this.hasExactlyThree = false;
		this.hasExactlyTwo = false;
		checkID();
		
	}
	
	public boolean isHasExactlyTwo() {
		return this.hasExactlyTwo;
	}

	public void setHasExactlyTwo(boolean hasExactlyTwo) {
		this.hasExactlyTwo = hasExactlyTwo;
	}

	public boolean isHasExactlyThree() {
		return this.hasExactlyThree;
	}

	public void setHasExactlyThree(boolean hasExactlyThree) {
		this.hasExactlyThree = hasExactlyThree;
	}

	
	
	public void checkID()
	{
		Set<Character> charID = getIdAsCharArray();
		
		setHasExactlyTwo(checkLetters(charID, 2));
		setHasExactlyThree(checkLetters(charID, 3));
		
	}
	
	private boolean checkLetters(Set<Character> id, int count)
	{
		
		for(char c : id) {
			int counter = 0;

			for (int i = 0; i < this.getId().length(); i++)
			{
				if(this.getId().charAt(i) == c)
				{
					counter++;
					
				}
			}
			if(counter == count)
			{
				return true;
			}
		}

		return false;
		
	}
	
	public Set<Character> getIdAsCharArray() {
		Set<Character> idSet = new LinkedHashSet<>();
		for(char c : this.id.toCharArray())
			idSet.add(c);
		
		return idSet;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}
	
	

	
	
	
	
	
}
