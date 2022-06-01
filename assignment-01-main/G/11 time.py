# By entering seconds we find how many hours, minutes and seconds.

seconds = int(input("enter seconds: "))
hour = seconds // 3600
seconds %= 3600
minute = seconds // 60
seconds %= 60
# second = seconds
print(hour, "hours,", minute, "minutes,", seconds, "seconds.")


'''public static void main(String[] args)
		Scanner sc=new Scanner(System.in);
		System.out.print("Give a number of seconds:");
		int seconds=sc.nextInt();
		int h=seconds/3600;
		int m=(seconds%3600)/60;
		int s=seconds%60;
		System.out.println("This corresponds to: " + h + " hours, "+ m +" minutes and "+ s +" seconds.");
		sc.close();'''

