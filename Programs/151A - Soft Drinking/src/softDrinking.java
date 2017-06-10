// Description of the problem can be found at http://codeforces.com/problemset/problem/151/A

import java.util.Scanner;

public class softDrinking {

	public static void main(String[] args) {
		Scanner sysIn = new Scanner(System.in);
		int n = sysIn.nextInt();
		int k = sysIn.nextInt();
		int l = sysIn.nextInt();
		int c = sysIn.nextInt();
		int d = sysIn.nextInt();
		int p = sysIn.nextInt();
		int nl = sysIn.nextInt();
		int np = sysIn.nextInt();
		
		int l_u = (c * d) / n;
		int p_u = p / (np * n);
		int d_u = l*k / (nl * n);
		
		int min = Math.min(l_u, p_u);
		min = Math.min(min, d_u);
		System.out.println(min);
		
		sysIn.close();
	}

}
