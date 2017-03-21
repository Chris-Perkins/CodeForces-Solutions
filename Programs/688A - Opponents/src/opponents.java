// Description of the problem can be found at http://codeforces.com/problemset/problem/688/A

import java.util.Scanner;

public class opponents {

	public static void main(String[] args) {
		Scanner sysIn = new Scanner(System.in);

		int n = sysIn.nextInt();
		int d = sysIn.nextInt();
		
		int m_c = 0;
		int c_c = 0;
		
		for(int i = 0 ; i < d ; i++)
		{
			String s = sysIn.next();
			if(s.contains("0"))
			{
				c_c += 1;
				m_c = Math.max(m_c, c_c);
			}
			else
			{
				c_c = 0;
			}
		}
		
		System.out.printf("%d", m_c);
		
		sysIn.close();
	}

}
