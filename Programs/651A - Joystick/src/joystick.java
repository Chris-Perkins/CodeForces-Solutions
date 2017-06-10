// Description of the problem can be found at http://codeforces.com/problemset/problem/651/A

import java.util.Scanner;

public class joystick {

	public static void main(String[] args) {
		Scanner sysIn = new Scanner(System.in);
		
		int a1 = sysIn.nextInt();
		int a2 = sysIn.nextInt();
		int t = 0;
		
		while(a1 > 0 && a2 > 0)
		{
			if (a1 > a2)
			{
				a1 -= 2;
				a2 += 1;
			}
			else
			{
				a1 += 1;
				a2 -= 2;
			}
			
			if (a1 >= 0 && a2 >= 0)
			{
				t += 1;
			}
		}
		
		System.out.printf("%d", t);
		
		sysIn.close();
	}

}
