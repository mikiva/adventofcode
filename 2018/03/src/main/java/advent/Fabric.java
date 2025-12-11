package advent;

import java.util.ArrayList;
import java.util.List;

public class Fabric
{

	private Claimed[][] wholePiece;
	private Claims claims;

	public Fabric() {

		createPiece();
		// print();

	}

	private void createPiece()
	{
		this.wholePiece = new Claimed[1000][1000];
		for (Claimed[] cl : this.wholePiece)
		{
			for (int i = 0; i < cl.length; i++)
			{
				cl[i] = new Claimed();

			}

		}

	}

	public void setClaims(Claims claims)
	{
		this.claims = claims;
		for (Claim c : claims.getClaims())
		{
			addClaim(c);
		}
	}

	public void addClaim(Claim claim)
	{

		int posX = claim.getPosition()[0];
		int posY = claim.getPosition()[1];
		int width = claim.getRectangle()[0];
		int height = claim.getRectangle()[1];

		for (int i = posX; i < posX + width; i++)
		{
			for (int j = posY; j < posY + height; j++)
			{

				this.wholePiece[i][j].addClaim(claim.getClaimID());
			}
		}

	}

	public int checkOverlaps()
	{
		int overlaps = 0;

		for (int i = 0; i < wholePiece.length; i++)
		{
			for (int j = 0; j < wholePiece[i].length; j++)
			{
				if (wholePiece[i][j].getClaimCount() > 1)
				{
					overlaps++;
				}
			}
		}

		return overlaps;
	}

	public int findSingleClaim()
	{
		int id = 0;
		List<Integer> testedIDs = new ArrayList<>();
		boolean singleFound = false;

		while (!singleFound)
		{
			Claim tryClaim = findSinglePatch(testedIDs);
			id = tryClaim.getClaimID();
	
			testedIDs.add(tryClaim.getClaimID());

			singleFound = checkIfOnlyClaim(tryClaim);


		}

		return id;
	}

	private boolean checkIfOnlyClaim(Claim claim)
	{
		
		int posX = claim.getPosition()[0];
		int posY = claim.getPosition()[1];
		int width = claim.getRectangle()[0];
		int height = claim.getRectangle()[1];

		for (int i = posX; i < posX + width; i++)
		{
			for (int j = posY; j < posY + height; j++)
			{

				if(this.wholePiece[i][j].getClaimCount() > 1)
					return false;
			}
		}
		
		
		return true;
	}

	private Claim findSinglePatch(List<Integer> tested)
	{

		
		for (int i = 0; i < wholePiece.length; i++)
		{
			for (int j = 0; j < wholePiece[i].length; j++)
			{

				if (wholePiece[i][j].getClaimCount() == 1)
				{
					int single = (int) wholePiece[i][j].getClaimed().get(0);
					if (tested.contains(single))
					{
						continue;
					} else
					{
						for (Claim cl : claims.getClaims())
						{
							if(cl.getClaimID() == single)
								return cl;
						}
					}
				}
			}
		}

		return null;
	}

	public void print()
	{
		for (int i = 0; i < 10; i++)
		{
			for (int j = 0; j < 60; j++)
			{
				System.out.printf("[%d]", wholePiece[i][j].getClaimed().size());
			}
			System.out.println();
		}
	}

}
