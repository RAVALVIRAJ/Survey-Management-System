import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random as r
def MAIN_MENU():
    print()
    print("_______________________________________________________")
    print("|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|")
    print("|* ->[ I N F O R M A T I C S ]<- *-*-*-*-*-*-*-*-*-*-*|")
    print("|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|")
    print("|*-*-*-*-*-*-*-*-*-*-*-*-* ->[ P R A C T I C E S ]<- *|")
    print("|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|")
    print("|*|=================================================|*|")
    print("|-|                                                 |-|")
    print("|*|                    [ START ]                    |*|")
    print("|-|                                                 |-|")
    print("|*|=================================================|*|")
    print("|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|")
    print("|*|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|*|")
    print("|-|                                                 |-|")
    print("|*|             -> { DATA READINGS } <-             |*|")
    print("|-|                                                 |-|")
    print("|*|-------------------------------------------------|*|")
    print("|-| 1.) Reading A CSV File .                        |-|")
    print("|*| 2.) Reading A CSV File Without Index .          |*|")
    print("|-|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|-|")
    print("|*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*|")
    print("|-|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|-|")
    print("|*|                                                 |*|")
    print("|-|         -> { VISUALIZATION OF DATA } <-         |-|")
    print("|*|                                                 |*|")
    print("|-|-------------------------------------------------|-|")
    print("|*| 3.) Line Chart Representation .                 |*|")
    print("|-| 4.) Bar Plot Representation .                   |-|")
    print("|*| 5.) Histogram Respresentation .                 |*|")
    print("|-|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|-|")
    print("|*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*|")
    print("|-|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|-|")
    print("|*|                                                 |*|")
    print("|-|           -> { DATA MANIPULATION } <-           |-|")
    print("|*|-------------------------------------------------|*|")
    print("|-| 6.) Data Sorting .                              |-|")
    print("|*| 7.) Highest or Lowest .                         |*|")
    print("|-| 8.) Tops or Bottoms .                           |-|")
    print("|*|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|*|")
    print("|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|")
    print("|*|=================================================|*|")
    print("|-|                                                 |-|")
    print("|*|                     [ END ]                     |*|")
    print("|-|                                                 |-|")
    print("|*|=================================================|*|")
    print("|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|")
    print("|=====================================================|")
    print()
    print()
    print("-------------------------------------------------------")
    print("                       OPERATIONS                      ")
    print("-------------------------------------------------------")
    print("          [ Cumulative Operations Begins Here ]        ")
def CHOICE():
    print()
    print("=> CHOOSE OPERATIONS TO PERFORM FROM :- ")
    print()
    print("[ Data Reading Based Operations ]")
    print(" ---> Press 1 to read CSV file .")
    print(" ---> Press 2 to read CSV file without index .")
    print()
    print("[ Data Visualization Based Operations ]")
    print(" ---> Press 3 to represent the data in LINE CHART .")
    print(" ---> Press 4 to represent the data in BAR PLOT .")
    print(" ---> Press 5 to represent the data in HISTOGRAM .")
    print()
    print("[ Data Manipulation Based Operations ]")
    print(" ---> Press 6 to SORT DATA ACCORDING TO YOUR PREFERENCES .")
    print(" ---> Press 7 to VIEW THE HIGHEST OR THE LOWEST VALUES .")
    print(" ---> Press 8 to VIEW MULTIPLE TOP OR BOTTOM VALUES .")
    print()
    print("[ Press 0 To Exit Cummulative Operations ]")    
def OPERATIONS(x):
    print()    
    def DATA_READING(x):   
        print("=> [ Data Reading Based Operations ] ")
        print()
        if x==1:            
            print("Reading CSV file :- ")
            print()
            dataframe=pd.read_csv(r"E:\Education\Computer Development\Python Project\Informatics Practices Project.csv")           
            print(dataframe)
        else:           
            print("Reading CSV File Without Index :- ")
            print()
            dataframe=pd.read_csv(r"E:\Education\Computer Development\Python Project\Informatics Practices Project.csv",index_col=0)           
            print(dataframe)
    def DATA_VISUALIZATION(x):
        print("=> [ Data Visualization Based Operations ] ")
        print()
        DF=pd.read_csv(r"E:\Education\Computer Development\Python Project\Informatics Practices Project.csv")
        State=DF["State"]
        #Capital=DF["Capital"]
        Population=DF["Population ( 2011 )"]
        HDI=DF["Human Development Index ( 2018 )"]
        Literacy=DF["Literacy Rate ( 2011 )"]
        Poverty=DF["Poverty Rate ( 2011 )"]
        Sex_Ratio=DF["Sex Ratio ( 2011 )"]
        Unemployment=DF["Unemployment Rate ( 2018 )"]       
        plt.xticks(rotation='vertical')        
        if x==3:
            l=plt.style.available            
            plt.grid(True)
            print("Line Chart Representation")
            print()
            print("Select Specific Line Chart Format :- ")
            print()            
            print("Press a to print the data of State wise Population ( 2011 ) .")
            print("Press b to print the data of State wise Human Development Index ( 2018 ) .")
            print("Press c to print the data of State wise Literacy Rate ( 2011 ) .")
            print("Press d to print the data of State wise Poverty Rate ( 2011 ).")
            print("Press e to print the data of State wise Sex Ratio ( 2011 ).")
            print("Press f to print the data of State wise Unemployment Rate ( 2018 ) .")            
            print()
            print("Press 1 to print the data of State wise All Attribute in Combined Line Chart .")
            userinput=input("Enter Your Choice : ")            
            if userinput=='a':
                plt.style.use(r.choice(l))
                plt.ylabel("Population ( 2011 )")
                plt.title("State wise Population ( 2011 )")                
                plt.plot(State,Population,'.-',color="navy")
                plt.show()            
            elif userinput=='b':                
                plt.style.use(r.choice(l))
                plt.ylabel("Human Development Index ( 2018 )")
                plt.title("State wise Human Development Index ( 2018 )")               
                plt.plot(State,HDI,'.-',color="lime")
                plt.show()            
            elif userinput=='c':
                plt.style.use(r.choice(l))
                plt.ylabel("Literacy Rate ( 2011 )")
                plt.title("State wise Literacy Rate ( 2011 )")                
                plt.plot(State,Literacy,'.-',color="tomato")
                plt.show()           
            elif userinput=='d':                
                plt.style.use(r.choice(l))
                plt.ylabel("Poverty Rate ( 2011 )")
                plt.title("State wise Poverty Rate ( 2011 )")                
                plt.plot(State,Poverty,'.-',color="hotpink")
                plt.show()            
            elif userinput=='e':               
                plt.style.use(r.choice(l))
                plt.ylabel("Sex Ratio ( 2011 )")
                plt.title("State wise Sex Ratio ( 2011 )")                
                plt.plot(State,Sex_Ratio,'.-',color="cyan")
                plt.show()           
            elif userinput=='f':                
                plt.style.use(r.choice(l))
                plt.ylabel("Unemployment Rate ( 2018 )")
                plt.title("State wise Unemployment Rate ( 2018 )")                
                plt.plot(State,Unemployment,'.-',color="grey")
                plt.show()            
            elif userinput=='1':                
                plt.style.use(r.choice(l))
                plt.ylabel("DATA")
                plt.title("State wise All Attribute")
                plt.plot(State,Population,'.-',color="navy",label="State wise Population")
                plt.plot(State,HDI,'.-',color="lime",label="State wise Human Development Index")
                plt.plot(State,Literacy,'.-',color="tomato",label="State wise Literacy Rate")
                plt.plot(State,Poverty,'.-',color="hotpink",label="State wise Poverty Rate")
                plt.plot(State,Sex_Ratio,'.-',color="cyan",label="State wise Sex Ratio")
                plt.plot(State,Unemployment,'.-',color="grey",label="State wise Unemployment Rate")
                plt.legend(loc="upper right")
                plt.show()
            else:
                print("Invalid Input")        
        elif x==4:
            l=plt.style.available
            plt.grid(True)
            print("Bar Plot Representation")
            print()            
            print("Select Specific Bar Plot Format :- ") 
            print()
            print("Press a to print the data of State wise Population ( 2011 ) .")
            print("Press b to print the data of State wise Human Development Index ( 2018 ) .")
            print("Press c to print the data of State wise Literacy Rate ( 2011 ) .")
            print("Press d to print the data of State wise Poverty Rate ( 2011 ).")
            print("Press e to print the data of State wise Sex Ratio ( 2011 ).")
            print("Press f to print the data of State wise Unemployment Rate ( 2018 ) .")
            print()            
            print("Press 1 to print the data of State wise All Attribute in Stack Bar Plot .")
            print("Press 2 to print the data of State wise All Attribute in Multiple Bar Plot .")            
            userinput=input("Enter Your Choice : ")            
            if userinput=='a':                
                plt.style.use(r.choice(l))
                plt.ylabel("Population ( 2011 )")
                plt.title("State wise Population ( 2011 )")                
                plt.bar(State,Population,color="navy")
                plt.show()            
            elif userinput=='b':                
                plt.style.use(r.choice(l))
                plt.ylabel("Human Development Index ( 2018 )")
                plt.title("State wise Human Development Index ( 2018 )")                
                plt.bar(State,HDI,color="lime")                
                plt.show()            
            elif userinput=='c':                
                plt.style.use(r.choice(l))
                plt.ylabel("Literacy Rate ( 2011 )")
                plt.title("State wise Literacy Rate ( 2011 )")                
                plt.bar(State,Literacy,color="tomato")                
                plt.show()            
            elif userinput=='d':                
                plt.style.use('seaborn-whitegrid')
                plt.ylabel("Poverty Rate ( 2011 )")
                plt.title("State wise Poverty Rate ( 2011 )")                
                plt.bar(State,Poverty,color="grey")               
                plt.show()            
            elif userinput=='e':                
                plt.style.use(r.choice(l))
                plt.ylabel("Sex Ratio ( 2011 )")
                plt.title("State wise Sex Ratio ( 2011 )")                
                plt.bar(State,Sex_Ratio,color="cyan")                
                plt.show()            
            elif userinput=='f':                
                plt.style.use('seaborn-whitegrid')
                plt.ylabel("Unemployment Rate ( 2018 )")
                plt.title("State wise Unemployment Rate ( 2018 )")                
                plt.bar(State,Unemployment,color="grey")                
                plt.show()            
            elif userinput=='1':                
                plt.style.use(r.choice(l))
                plt.ylabel("DATA")
                plt.title("State wise All Attribute")
                plt.bar(State,Population,color="navy",label="State wise Population ( 2011 )")
                plt.bar(State,Unemployment,bottom=Population,color="grey",label="State wise Unemployment Rate ( 2018 )")
                plt.bar(State,Poverty,bottom=Unemployment,color="hotpink",label="State wise Poverty Rate ( 2011 )")
                plt.bar(State,HDI,bottom=Poverty,color="lime",label="State wise Human Development Index ( 2018 )")
                plt.bar(State,Literacy,bottom=HDI,color="tomato",label="State wise Literacy Rate ( 2011 )")
                plt.bar(State,Sex_Ratio,bottom=Literacy,color="cyan",label="State wise Sex Ratio ( 2011 )")
                plt.legend()
                plt.show()
            elif userinput=='2':
                plt.style.use(r.choice(l))
                Index=np.arange(len(State)*6,step=6)
                Width=1
                plt.xlabel=("States")
                plt.ylabel("DATA")
                plt.title("State wise All Attribute")
                plt.bar(Index,Population,Width,color="navy",label="State wise Population ( 2011 )")
                plt.bar(Index+1,HDI,Width,color="lime",label="State wise Human Development Index ( 2018 )")
                plt.bar(Index+2,Literacy,Width,color="tomato",label="State wise Literacy Rate ( 2011 )")
                plt.bar(Index+3,Poverty,Width,color="hotpink",label="State wise Poverty Rate ( 2011 )")
                plt.bar(Index+4,Sex_Ratio,Width,color="cyan",label="State wise Sex Ratio ( 2011 )")
                plt.bar(Index+5,Unemployment,Width,color="grey",label="State wise Unemployment Rate ( 2018 )")
                plt.xticks(Index,State)
                plt.legend()
                plt.show()
            else:
                print("Invalid Input")
        else:
            l=plt.style.available
            plt.grid(True)
            plt.xticks(rotation='horizontal')
            print("Histogram Representation")
            print()
            print("Select Specific Histogram Format :- ") 
            print()
            print("Press a to print the statistical data of Population ( 2011 ).")
            print("Press b to print the statistical data of Human Development Index ( 2018 ).")
            print("Press c to print the statistical data of Literacy Rate ( 2011 ).")
            print("Press d to print the statistical data of Poverty Rate ( 2011 ).")
            print("Press e to print the statistical data of Sex Ratio ( 2011 ).")
            print("Press f to print the statistical data of Unemployment Rate ( 2018 ).")
            print()            
            print("Press 1 to print the statistical data of Combined Histograms.")
            Total=[]
            nos=int(round(len(State))/2)
            for j in range(0,nos,2):
                    Total+=[j]
            userinput=input("Enter Your Choice : ") 
            if userinput=='a':
                plt.style.use(r.choice(l))
                population_upper_limit=round(max(Population))
                population_lower_limit=round(min(Population))
                Limits=[]
                for i in range(population_lower_limit,population_upper_limit,2):
                    Limits+=[i]    
                plt.hist(Population,bins=Limits,color="navy",ec="black")
                plt.ylabel("Number of States")
                plt.xticks(Limits)
                plt.yticks(Total)
                plt.title("Population ( 2011 )")
                plt.show()
            elif userinput=='b':
                plt.style.use(r.choice(l))
                hdi_upper_limit=round(max(HDI))
                hdi_lower_limit=round(min(HDI))
                Limits=[]
                for i in range(hdi_lower_limit,hdi_upper_limit,2):
                    Limits+=[i]   
                plt.hist(HDI,bins=Limits,color="lime",ec="black")
                plt.ylabel("Number of States")
                plt.xticks(Limits)
                plt.yticks(Total)
                plt.title("Human Devalopment Index ( 2018 )")
                plt.show()
            elif userinput=='c':
                plt.style.use(r.choice(l))
                literacy_upper_limit=round(max(Literacy))
                literacy_lower_limit=round(min(Literacy))               
                Limits=[]
                for i in range(literacy_lower_limit,literacy_upper_limit,2):
                    Limits+=[i]   
                plt.hist(Literacy,bins=Limits,color="tomato",ec="black")
                plt.ylabel("Number of States")
                plt.xticks(Limits)
                plt.yticks(Total)
                plt.title("Literacy Rate ( 2011 )")
                plt.show()
            elif userinput=='d':
                plt.style.use(r.choice(l))
                poverty_upper_limit=round(max(Poverty))
                poverty_lower_limit=round(min(Poverty))               
                Limits=[]
                for i in range(poverty_lower_limit,poverty_upper_limit,2):
                    Limits+=[i]   
                plt.hist(Poverty,bins=Limits,color="hotpink",ec="black")
                plt.ylabel("Number of States")
                plt.xticks(Limits)
                plt.yticks(Total)
                plt.title("Poverty Rate ( 2011 )")
                plt.show()
            elif userinput=='e':
                plt.style.use(r.choice(l))
                sex_ratio_upper_limit=round(max(Sex_Ratio))
                sex_ratio_lower_limit=round(min(Sex_Ratio))              
                Limits=[]
                for i in range(sex_ratio_lower_limit,sex_ratio_upper_limit,2):
                    Limits+=[i]   
                plt.hist(Sex_Ratio,bins=Limits,color="cyan",ec="black")
                plt.ylabel("Number of States")
                plt.xticks(Limits)
                plt.yticks(Total)
                plt.title("Sex Ratio ( 2011 )")
                plt.show()
            elif userinput=='f':
                plt.style.use(r.choice(l))
                unemployment_upper_limit=round(max(Unemployment))
                unemployment_lower_limit=round(min(Unemployment))               
                Limits=[]
                for i in range(unemployment_lower_limit,unemployment_upper_limit,2):
                    Limits+=[i]   
                plt.hist(Unemployment,bins=Limits,color="grey",ec="black")
                plt.ylabel("Number of States")
                plt.xticks(Limits)
                plt.yticks(Total)
                plt.title("Unemployment Rate ( 2018 )")
                plt.show()
            elif userinput=='1':
                plt.style.use(r.choice(l))
                Limits=nos
                plt.hist(Population,bins=Limits,color="navy",alpha=0.75,histtype="stepfilled",label="Population ( 2011 )")
                plt.hist(HDI,bins=Limits,color="lime",alpha=0.75,histtype="stepfilled",label="Human Development Index ( 2018 )")
                plt.hist(Literacy,bins=Limits,color="tomato",alpha=0.75,histtype="stepfilled",label="Human Development Index ( 2018 )")
                plt.hist(Poverty,bins=Limits,color="hotpink",alpha=0.75,histtype="stepfilled",label="Poverty Rate ( 2011 )")
                plt.hist(Sex_Ratio,bins=Limits,color="cyan",alpha=0.75,histtype="stepfilled",label="Sex Ratio ( 2011 )")
                plt.hist(Unemployment,bins=Limits,color="grey",alpha=0.75,histtype="stepfilled",label="Unemployment Rate ( 2018 )")
                plt.yticks(Total)
                plt.ylabel("Number of States")
                plt.title("Combined Histogram")
                plt.legend()
                plt.show()
            else:
                print("Invalid Input")
    def DATA_MANIPULATION(x):
        print("=> [ Data Manipulation Based Operations ] ")
        print()
        DF=pd.read_csv(r"E:\Education\Computer Development\Python Project\Informatics Practices Project.csv",index_col=0)
        if x==6:
            print("Data Sorting")
            print()
            print("Select The Specific Order For Sorting :- ")
            print()
            print("Press 1 to sort data in Ascending Order.")
            print("Press 2 to sort data in Desending Order.")
            order=int(input("Enter Your Choice : "))
            if order==1:
                print()
                print("Select Specific Attribute to Sort Data :- ")
                print()
                print("Press a to sort the data according to State.")
                print("Press b to sort the data according to Capital.")
                print("Press c to sort the data according to Population ( 2011 ).")
                print("Press d to sort the data according to Human Development Index ( 2018 ).")
                print("Press e to sort the data according to Literacy Rate ( 2011 ).")
                print("Press f to sort the data according to Poverty Rate ( 2011 ).")
                print("Press g to sort the data according to Sex Ratio ( 2011 ).")
                print("Press h to sort the data according to Unemployment Rate ( 2018 ).")
                userinput=input("Enter Your Choice : ")
                print()
                if userinput=='a':
                    print(DF["Unemployment Rate ( 2018 )"])
                elif userinput=='b':
                    DF.sort_values(["Capital"],inplace=True)
                    print(DF)
                elif userinput=='c':
                    DF.sort_values(["Population ( 2011 )"],inplace=True)
                    print(DF)
                elif userinput=='d':
                    DF.sort_values(["Human Development Index ( 2018 )"],inplace=True)
                    print(DF)
                elif userinput=='e':
                    DF.sort_values(["Literacy Rate ( 2011 )"],inplace=True)
                    print(DF)
                elif userinput=='f':
                    DF.sort_values(["Poverty Rate ( 2011 )"],inplace=True)
                    print(DF)
                elif userinput=='g':
                    DF.sort_values(["Sex Ratio ( 2011 )"],inplace=True)
                    print(DF)
                elif userinput=='h':
                    DF.sort_values(["Unemployment Rate ( 2018 )"],inplace=True)
                    print(DF)
                else:
                    print("Invalid Input")
            elif order==2:
                print()
                print("Select Specific Attribute to Sort Data :- ")
                print()
                print("Press a to sort the data according to State.")
                print("Press b to sort the data according to Capital.")
                print("Press c to sort the data according to Population ( 2011 ).")
                print("Press d to sort the data according to Human Development Index ( 2018 ).")
                print("Press e to sort the data according to Literacy Rate ( 2011 ).")
                print("Press f to sort the data according to Poverty Rate ( 2011 ).")
                print("Press g to sort the data according to Sex Ratio ( 2011 ).")
                print("Press h to sort the data according to Unemployment Rate ( 2018 ).")
                userinput=input("Enter Your Choice : ")
                print()
                if userinput=='a':
                    DF.sort_values(["State"],inplace=True,ascending=False)
                    print(DF)
                elif userinput=='b':
                    DF.sort_values(["Capital"],inplace=True,ascending=False)
                    print(DF)
                elif userinput=='c':
                    DF.sort_values(["Population ( 2011 )"],inplace=True,ascending=False)
                    print(DF)
                elif userinput=='d':
                    DF.sort_values(["Human Development Index ( 2018 )"],inplace=True,ascending=False)
                    print(DF)
                elif userinput=='e':
                    DF.sort_values(["Literacy Rate ( 2011 )"],inplace=True,ascending=False)
                    print(DF)
                elif userinput=='f':
                    DF.sort_values(["Poverty Rate ( 2011 )"],inplace=True,ascending=False)
                    print(DF)
                elif userinput=='g':
                    DF.sort_values(["Sex Ratio ( 2011 )"],inplace=True,ascending=False)
                    print(DF)
                elif userinput=='h':
                    DF.sort_values(["Unemployment Rate ( 2018 )"],inplace=True,ascending=False)
                    print(DF)
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        elif x==7:
            print("Highest and Lowest")
            print()
            print("Select Between Highest and Lowest :- ")
            print()
            print("Press 1 for Highest.")
            print("Press 2 for Lowest.")
            choice=int(input("Enter Your Choice : "))
            print()
            if choice==1:
                print("Select Specific Format :- ")
                print()
                print("Press a to get the Highest row according to Population ( 2011 ).")
                print("Press b to get the Highest row according to Human Development Index ( 2018 ).")
                print("Press c to get the Highest row according to Literacy Rate ( 2011 ).")
                print("Press d to get the Highest row according to Poverty Rate ( 2011 ).")
                print("Press e to get the Highest row according to Sex Ratio ( 2011 ).")
                print("Press f to get the Highest row according to Unemployment Rate ( 2018 ).")
                userinput=input("Enter Your Choice : ")
                print()
                if userinput=='a':
                    print(DF[DF["Population ( 2011 )"]==DF["Population ( 2011 )"].max()])
                elif userinput=='b':
                    print(DF[DF["Human Development Index ( 2018 )"]==DF["Human Development Index ( 2018 )"].max()])
                elif userinput=='c':
                    print(DF[DF["Literacy Rate ( 2011 )"]==DF["Literacy Rate ( 2011 )"].max()])
                elif userinput=='d':
                    print(DF[DF["Poverty Rate ( 2011 )"]==DF["Poverty Rate ( 2011 )"].max()])
                elif userinput=='e':
                    print(DF[DF["Sex Ratio ( 2011 )"]==DF["Sex Ratio ( 2011 )"].max()])
                elif userinput=='f':
                    print(DF[DF["Unemployment Rate ( 2018 )"]==DF["Unemployment Rate ( 2018 )"].max()])
                else:
                    print("Invalid Input")
            elif choice==2:
                print("Select Specific Format :- ")
                print()
                print("Press a to get the lowest row according to Population ( 2011 ).")
                print("Press b to get the lowest row according to Human Development Index ( 2018 ).")
                print("Press c to get the lowest row according to Literacy Rate ( 2011 ).")
                print("Press d to get the lowest row according to Poverty Rate ( 2011 ).")
                print("Press e to get the lowest row according to Sex Ratio ( 2011 ).")
                print("Press f to get the lowest row according to Unemployment Rate ( 2018 ).")
                userinput=input("Enter Your Choice : ")
                print()
                if userinput=='a':
                    print(DF[DF["Population ( 2011 )"]==DF["Population ( 2011 )"].min()])
                elif userinput=='b':
                    print(DF[DF["Human Development Index ( 2018 )"]==DF["Human Development Index ( 2018 )"].min()])
                elif userinput=='c':
                    print(DF[DF["Literacy Rate ( 2011 )"]==DF["Literacy Rate ( 2011 )"].min()])
                elif userinput=='d':
                    print(DF[DF["Poverty Rate ( 2011 )"]==DF["Poverty Rate ( 2011 )"].min()])
                elif userinput=='e':
                    print(DF[DF["Sex Ratio ( 2011 )"]==DF["Sex Ratio ( 2011 )"].min()])
                elif userinput=='f':
                    print(DF[DF["Unemployment Rate ( 2018 )"]==DF["Unemployment Rate ( 2018 )"].min()])
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        else:
            print("Tops and Bottoms")
            print()
            print("Select Between Tops and Bottoms :- ")
            print()
            print("Press 1 for Tops.")
            print("Press 2 for Bottoms.")
            choice=int(input("Enter Your Choice : "))
            if choice==1:
                tops=int(input("Enter Number of Values : "))
                print()
                print(DF.head(tops))
            elif choice==2:
                bottoms=int(input("Enter Number of Values : "))
                print()
                print(DF.tail(bottoms))
            else:
                print("Invalid Input")
    if x==1 or x==2: 
        DATA_READING(x)    
    elif x in [3,4,5]:
        DATA_VISUALIZATION(x)
    elif x in [6,7,8]:
        DATA_MANIPULATION(x)
    else:
        print("Invalid Input")
def CUMULATIVE_OPERATION():
    REPLY=1
    while(REPLY!=0):        
        CHOICE()        
        x=int(input("ENTER YOUR CHOICE : "))        
        if x==0:
            REPLY=0
            print()
            print("          [ Cumulative Operations Ends Here . ]          ")
        else:
            OPERATIONS(x)        
def REPRESENTATION():    
    MAIN_MENU()    
    CUMULATIVE_OPERATION()      
REPRESENTATION()