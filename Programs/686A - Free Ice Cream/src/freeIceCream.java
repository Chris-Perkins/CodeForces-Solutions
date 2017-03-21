// Description of the problem can be found at http://codeforces.com/problemset/problem/686/A
import java.math.BigInteger;
import java.util.Scanner;

public class freeIceCream {

	public static void main(String[] args) {
		Scanner sysIn = new Scanner(System.in);
		
		int n = sysIn.nextInt();
		BigInteger x = BigInteger.valueOf(sysIn.nextLong());
		int d_t = 0;
				
		for(int i = 0 ; i < n ; i++)
		{
			if (sysIn.next().equals("+"))
			{
				x = x.add(BigInteger.valueOf(sysIn.nextLong()));
			}
			else
			{
				BigInteger w = BigInteger.valueOf(sysIn.nextLong());
				
				if (w.compareTo(x) <= 0)
				{
					x = x.subtract(w);
				}
				else
				{
					d_t += 1;
				}
			}
		}
		
		System.out.printf("%s %d", x.toString(), d_t);
	}

}
