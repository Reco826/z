import requests
import  hashlib
import time


#---------------------ctv_htv-------------------#	
url_token="https://services.orange.eg/GetToken.svc/GenerateToken"

hed_token={
    "net-msg-id":"e84d3c3b029904d16941165419001111",
    "x-microservice-name":"APMS",
    "Content-Type":"application/json; charset=UTF-8",
    "Content-Length":"78",
    "Host":"services.orange.eg",
    "Connection":"Keep-Alive",
    "Accept-Encoding":"gzip",
    "User-Agent":"okhttp/3.14.9",
    
    
    
    }

data_token={
  "channel": {
    "ChannelName": "MobinilAndMe",
    "Password": "ig3yh*mk5l42@oj7QAR8yF"
  }
}

r_ctv=requests.post(url_token, headers=hed_token, json=data_token).json()
#print(r_ctv)
ctv=r_ctv["GenerateTokenResult"]["Token"]
#print(ctv)
#----------------htv
extra_htv = ctv+",{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk"
htv = hashlib.sha256(extra_htv.encode('utf-8')).hexdigest().upper()
#print(htv)
#-------------------Input_user-------------------#
num=input("[+]Enter Your Number => : ")
print("-"*20+"(®)")
pas=input("[-]Enter Your Password => : ")
print("-"*20+"(®)")
num_famliy=input("[*]Enter Family Member Dial: ")
print()
#----------------addition _num-----------------#
while True:	
	url_add="https://backend.orange.eg/api/HybridFamily/ManageSharing"

	headers_add={
  "_ctv": ctv,
  "_htv": htv,
  "net-msg-id":"a1e19c56005529d16943850806221246",
  "x-microservice-name":"APMS",
  "Content-Type":"application/json; charset=UTF-8",
  "Content-Length":"254",
  "Host":"backend.orange.eg",
  "Connection":"Keep-Alive",
  "Accept-Encoding":"gzip",
  "User-Agent":"okhttp/3.14.9"
}
	data_add={
  "ActionType": "2",
  "channel": {
    "ChannelName": "MobinilAndMe",
    "Password": "ig3yh*mk5l42@oj7QAR8yF"
  },
  "FamilyMemberDial": num_famliy,
  "lang": "ar",
  "Sharing": [
    {
      "SharedAmount": "200",
      "SharingType": 5
    }
  ],
  "dial": num,
  "IsEasyLogin": False,
  "password": pas
}
#-------------------
	r_add = requests.post(url_add, headers=headers_add, json=data_add).json()
	Reply = r_add["ErrorDescription"]
	#print(Reply)
	if "تم إرسال طلبك بنجاح سوف تصلك رسالة بالتفاصيل" in Reply:
		print("#---Done 200MG---#")
		print("-"*20+"(@)")
	else:
		print("Try again")
		print("-"*20+"(@)")
#------------------wait_60_sec-------------------#
	sec= 60
	for x in range(sec,0,-1):
		print(f"[+]please wait {x} Second \r",end="")
		time.sleep(1)
#----------------delete_num-------------------#

	url_remove="https://backend.orange.eg/api/HybridFamily/ManageFamily"

	headers_remove={
     "_ctv": ctv,
     "_htv": htv,
     "net-msg-id":"a1e19c56005529d16943848403981092",
     "x-microservice-name":"APMS",
     "Content-Type":"application/json; charset=UTF-8",
     "Content-Length":"235",
     "Host":"backend.orange.eg",
     "Connection":"Keep-Alive",
     "Accept-Encoding":"gzip",
     "User-Agent":"okhttp/3.14.9"
     
     
     }
	data_remove={
  "ActionType": "3",
  "channel": {
    "ChannelName": "MobinilAndMe",
    "Password": "ig3yh*mk5l42@oj7QAR8yF"
  },
  "FamilyMemberDial": num_famliy,
  "FamilyOwnerDial": num,
  "lang": "ar",
  "dial": num,
  "IsEasyLogin": False,
  "password": pas
}
	r_remove=requests.post(url_remove, headers=headers_remove, json=data_remove).json()
	#print(r_remove)
	Reply2=r_remove["ErrorDescription"]
	#print(Reply2)
#---------------------if
	if "تم خروج " in Reply2:
		print(f"exit number: ({num_famliy})")
		print("-"*20+"(@)")
	else:
		print("exit error")
		print("-"*20+"(@)")	 	
