package advent;

public class Claim {

	private String claim;
	private Integer claimID;
	private int[] rectangle;
	private int[] position;
	
	

	public Claim(String claim) {
		this.claim = claim;
		
		createClaim();
		
	}
	
	private void createClaim() {
		String[] claimAr = getClaim().split("\\s+");
		
		
		createClaimID(claimAr[0]);
		createClaimPosition(claimAr[2]);
		createClaimRec(claimAr[3]);
		
		
	}
	private void createClaimID(String claimIDString)
	{
		setClaimID(Integer.parseInt(claimIDString.substring(1)));
	}
	private void createClaimRec(String claimRecString)
	{
		String[] recS = claimRecString.split("x");
		int[] rec = new int[2];
		for(int i = 0; i < recS.length; i++)
		{
			rec[i] =Integer.parseInt(recS[i]);
		}
		
		setRectangle(rec);
	}
	private void createClaimPosition(String claimPosString)
	{
		String[] posS = claimPosString.split(",");
		int[] pos = new int[2];
			pos[0] = Integer.parseInt(posS[0]);
			pos[1] = Integer.parseInt(posS[1].substring(0, posS[1].length()-1));
		setPosition(pos);
	}

	public String getClaim() {
		return claim;
	}

	public void setClaim(String claim) {
		this.claim = claim;
	}

	public Integer getClaimID() {
		return claimID;
	}

	public void setClaimID(Integer claimID) {
		this.claimID = claimID;
	}

	public int[] getRectangle() {
		return rectangle;
	}

	public void setRectangle(int[] rectangle) {
		this.rectangle = rectangle;
	}

	public int[] getPosition() {
		return position;
	}

	public void setPosition(int[] location) {
		this.position = location;
	}
	
	@Override
	public String toString()
	{
		String str = String.format("id: %d, pos: %d-%d, rec: %dx%d", claimID, position, rectangle);
		
		return str;
	}
	
	

}
