package advent;

import java.util.ArrayList;
import java.util.List;

public class Claims {

	private List<String> input;
	private List<Claim> claims;

	
	public Claims(List<String> input)
	{
		
		this.input = input;
		this.claims = buildClaims();
		
	}
	
	public List<Claim> getClaims()
	{
		return claims;
	}
	
	private List<Claim> buildClaims()
	{
		List<Claim> claimList = new ArrayList<>();
		
		for(String s : this.input)
			claimList.add(new Claim(s));
		
		return claimList;
		
	}
	
}
