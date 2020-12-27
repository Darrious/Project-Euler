
// Darrious Barger

// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143?

public class large_prime_fact
{
	public static void main(String[] args)
	{
		long num = 6000;
		long largest = 0;
		for (long i = 2; i < num; i++)
		{
			if (i % 2 != 0 )
			{
				for (long j = 2; j < i; j++)
				{
					if (i%j != 0 && num % i==0)
					{
						largest = i;
					}
				}
			}
		}

		System.out.println(largest);
	}
}