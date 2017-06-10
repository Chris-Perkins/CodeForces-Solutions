// Description of the problem can be found at http://codeforces.com/problemset/problem/454/A

import java.util.Scanner;

public class littlePonyAndCrystalMine {

	public static void main(String[] args) {
		Scanner sysIn = new Scanner(System.in);
		
		int n = sysIn.nextInt();
		int r = 1;
		int s = 1;
		
		for(int i = 0 ; i < n; i++)
		{
			for(int j = 0 ; j < (n - (s * 2 - 1)) / 2 ; j++)
			{
				System.out.print("*");
			}
			for(int j = 0 ; j < s * 2 - 1 ; j ++)
			{
				System.out.print("D");
			}
			for(int j = 0 ; j < (n - (s * 2 - 1)) / 2 ; j++)
			{
				System.out.print("*");
			}
			
			System.out.println();
			
			if(i == n / 2)
			{
				r = -1;
			}
			s += r;
		}
		
		sysIn.close();
	}

}
