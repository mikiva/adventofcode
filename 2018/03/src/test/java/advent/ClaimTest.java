package advent;

import static org.junit.Assert.assertEquals;

import java.util.List;

import org.junit.Before;
import org.junit.Test;

public class ClaimTest {

	List<String> input;

	@Before
	public void initInput() {
		this.input = ReadInput.getInput();
	}

	@Test
	public void splitClaimToArrayTest() {
		String claim = input.get((int) Math.random() * input.size());

		String[] split = claim.split("\\s+");

		assertEquals("Inte rätt längd", 4, split.length);
		assertEquals("Inte rätt tecken", "@", split[1]);
	}

	@Test
	public void testClaimPositionParse() {
		int[] pos = new int[2];
		int random = (int)(Math.random()*input.size());
		
		String claim = input.get(random);

		String[] split = claim.split("\\s+");
		
		String[] posS = split[2].split(",");

		pos[0] = Integer.parseInt(posS[0]);
		pos[1] = Integer.parseInt(posS[1].substring(0, posS[1].length()-1));
		System.out.println(pos[0]);
		System.out.println(pos[1]);
	}

}
