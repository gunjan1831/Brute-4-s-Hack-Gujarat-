#!/usr/bin/env python
# coding: utf-8

# In[2]:


symp = ["fever","cough","cold","sneezing","fatigue","weakness","lack of appetite","headache","lack of thirst","runny nose","itching","muscle weakness","weight gain","dry skin","depression","bodyache","seizures","skin rash","chills","nausea","sinus pain"]
choice = 0
listOfsym=[]
while(1):
    print("Select the symptoms according to the S.No:")
    print("1. fever")
    print("2. cough")
    print("3. cold")
    print("4. sneezing")
    print("5. fatigue")
    print("6. weakness")
    print("7. lack of appetite")
    print("8. headache")
    print("9. lack of thirst")
    print("10. runny nose")
    print("11. itching")
    print("12. muscle weakness")
    print("13. weight gain")
    print("14. dry skin")
    print("15. depression")
    print("16. bodyache")
    print("17. seizures")
    print("18. skin rash")
    print("19. chills")
    print("20. nausea")
    print("21. sinus pain")
    print("22. exit")
    
    
    choice=int(input("enter choice: "))
    if(choice == 22):
        break
    elif(choice <1 or choice>21):
        print("Wrong input")
        continue
    else:
        dup=listOfsym.count(symp[choice-1])
        if dup>0:
            print("Already added")
            continue
        else:
            listOfsym.append(symp[choice-1])
            print("symptom added: ",symp[choice-1])
print("")
print("The final list of symptoms are: ",listOfsym)

swineFlu=['fever','cough','headache','fatigu','bodyache','chills','swineFlu']
pneumococcalMeningitis=['fever','skin rash','headache','lack of apitite','lack of thirst','seizures','pneumococcalMeningitis']
influenzaFlu=['fever','cough','headache','sinus pain','runny nose','sneezing','influenzaFlu']
acuteKidneyFailure=['fatigue','seizuers','lack of apitite','itching','muscle weakness','nausea','acuteKidneyFailure']
hypothuroidism=['weakness','cold','dry skin','fatigu','weight gain','depression','hypothuroidism']
diseasesn=[swineFlu,pneumococcalMeningitis,influenzaFlu,acuteKidneyFailure,hypothuroidism]

def getPercentage(disease,symptoms):    #to find number of symptoms matching a particular disease
    x=len(symptoms)
    flag=0
    for i in range(0,x):
        if symptoms[i] in disease:
            flag=flag+1              
    
    print(str(disease[len(disease)-1])+' = '+str(flag*100/(len(disease)-1))[:5]+'%')
    #print(disease[len(disease)-1])
    
    
for i in range(0,5):
    getPercentage(diseasesn[i],listOfsym)
            


# In[ ]:




