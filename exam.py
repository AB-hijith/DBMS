import pymongo
url="mongodb://localhost:27017/"
client=pymongo.MongoClient(url)
db=client["Exam"]
co=db["Student"]

#co.insert_many([{"_id":2,"Name":"Anuradha","Place":"Varkala",
#"Phone":9992639562,"Vaccination_status":"Both vaccinated",
#"RTPCR":"negative","Lab_mark":{"Internal":40,"External":48},
#"Department":"Civil"},


#{"_id":3,"Name":"Bismiya","Place":"Kollam",
#"Phone":9446639562,"Vaccination_status":"not vaccinated",
#"RTPCR":"positive","Lab_mark":{"Internal":50,"External":39},
#"Department":"MCA"},


#{"_id":4,"Name":"Vimal","Place":"Ernakulam",
#"Phone":8582639568,"Vaccination_status":"First does only",
#"RTPCR":"positive","Lab_mark":{"Internal":40,"External":42},
#"Department":"Civil"},


#{"_id":5,"Name":"Vivek","Place":"Kollam",
#"Phone":8582639777,"Vaccination_status":"Both vaccinated",
#"RTPCR":"negative","Lab_mark":{"Internal":50,"External":50},
#"Department":"MCA"}])




#for s in co.find({"Vaccination_status":"not vaccinated"}):
	#print(s["Name"]+'\n'+str(s["Phone"]))


#for s in co.find({"Department":"MCA"}).sort("Lab_mark.External",-1).limit(2):
	#print(s["Name"]+"\n"+str(s["Phone"]))


#for s in co.find({"Name":{"$regex":"^A"}}):
	#print(str(s["_id"])+"\n"+s["Name"]+"\n"+s["Department"])


#myq={"_id":4}
#upd={"$set":{"Vaccination_status":"Both vaccinated"}}
#co.update_one(myq,upd)


#for s in co.find().sort("Lab_mark.External",-1):
	#print(s["Name"])
