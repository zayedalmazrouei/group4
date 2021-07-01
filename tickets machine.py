print("            ", "Welcome to Group4 Cinema")
Customer_First_Name = input("Enter Your First Name:")
Customer_Last_Name = input("Enter Your Last Name:")
print("Hello!", Customer_First_Name, Customer_Last_Name, "Which move would you like to book?")
print("please choise from 1 to 4")


def movies():
    print("[1] Cruella","PG13")
    print("[2] A Queit Place: Part II","PG16")
    print("[3] Fast and Furious 9","PG")
    print("[4] Exit/Quit")

movies()
while True:
    movies = input("Enter your option:")
    if movies.lower() not in ('1', '2', '3', '4'):
        print("wrong choice try again.")
    else:
        break
if movies=='4':
        import os
        import sys
        os.execl(sys.executable, sys.executable, *sys.argv)



# first move options
if movies=='1':
    print("Cruella")
    def age1():
        age=int(input("Please enter your age:"))
        if age >=13:
            print("You are allowed to see the film. Standard ticket price is 35AED")
            def menu1():
                print("[1] Book a seat")
                print("[2] Movie Description")
                print("[3] exit/quit")
            menu1()
            while True:
                menu1 = input("Enter your option3:")
                if menu1.lower() not in ('1', '2', '3'):
                    print("wrong choice try again.")
                elif menu1 == '3':
                    import os
                    import sys
                    os.execl(sys.executable, sys.executable, *sys.argv)
                elif menu1=='2':
                    print("Genre: Comedy","     ""A live-action prequel feature film following a young Cruella de Vil.")
                    print("Running Time: 135 min")
                    print("Release Date: 27 May 2021")
                    print("Starring: Emma Stone, Mark Strong, Emma Thompson")
                    print("Language: English")
                    print("Subtitle(s): Arabic")
                    import os
                    import sys
                    os.execl(sys.executable, sys.executable, *sys.argv)

                elif menu1=='1':
                    def timing_1():
                        print("[1] 10:00-13:00")
                        print("[2] 13:10-16:10")
                        print("[3] 16:20-19:20")
                        print("[4] exit/quit")
                    timing_1()
                    while True:
                            movies_time1 = input("Enter your option2:")
                            if movies_time1.lower() not in ('1', '2', '3', '4'):
                                print("wrong choice try again.")
                            if movies_time1 == '4':
                                import os
                                import sys
                                os.execl(sys.executable, sys.executable, *sys.argv)

                            if movies_time1 == '1':
                                tikets1_movie1 = int(input("how many person:"))
                                price1_movie1 = tikets1_movie1 * 35
                                print("total=", price1_movie1)
                                conform1=input("send y to conform to cancel send n{y/n}:")
                                if conform1.lower() not in ('y','n'):
                                    print("try again")
                                if conform1=='y':
                                    print("ticket")
                                    print("Creulla")
                                    print("screen:1")
                                    print("10:00-13:00")
                                    print("person:",tikets1_movie1)
                                    exit()
                            if movies_time1 == '2':
                                tikets2_movie1=int(input("how many person:"))
                                price2_movie1=tikets2_movie1 * 35
                                print("total=",price2_movie1)
                                conform1 = input("send y to conform to cancel send n{y/n}:")
                                if conform1.lower() not in ('y', 'n'):
                                    print("try again")
                                if conform1 == 'y':
                                    print("ticket")
                                    print("Creulla")
                                    print("screen:1")
                                    print("13:10-16:10")
                                    print("person:",tikets2_movie1)
                                    exit()
                            if movies_time1 == '3':
                                tikets3_movie1=int(input("how many person:"))
                                price3_movie1=tikets3_movie1 * 35
                                print("total=",price3_movie1)
                                conform1 = input("send y to conform to cancel send n{y/n}:")
                                if conform1.lower() not in ('y', 'n'):
                                    print("try again")
                                if conform1 == 'y':
                                    print("ticket")
                                    print("Creulla")
                                    print("screen:1")
                                    print("16:20-19:20")
                                    print("person:",tikets3_movie1)
                                    exit()
                            else:
                                exit()
                    else:
                        exit()


        if age <13:
            print("Sorry,You are not over 13 years old. You cannot watch this movie.")
            exit()
        else:
            exit()
    age1()


# second move options
if movies=='2':
    print("A Queit Place: Part II")
    def age2():
        age=int(input("Please enter your age:"))
        if age >=16:
            print("You are allowed to see the film. Standard ticket price is 40AED")
            def menu2():
                print("[1] Book a seat")
                print("[2] Movie Description")
                print("[3] exit/quit")
            menu2()
            while True:
                menu2 = input("Enter your option3:")
                if menu2.lower() not in ('1', '2', '3'):
                    print("wrong choice try again.")
                if menu2 == '3':
                    import os
                    import sys
                    os.execl(sys.executable, sys.executable, *sys.argv)
                if menu2=='2':
                    print("Genre: Horror","        Following the events at home","the Abbott family now face the terrors of the outside world.")
                    print("                      Forced to venture into the unknown, they realize that the creatures that hunt by sound are")
                    print("                      not the only threats that lurk beyond the sand path.")
                    print("Running Time: 100 min")
                    print("Release Date: 10 June 2021")
                    print("Starring: Emily Blunt, Noah Jupe, Djimon Hounsou, Cillian Murphy")
                    print("Language: English")
                    print("Subtitle(s): Arabic")
                    import os
                    import sys
                    os.execl(sys.executable, sys.executable, *sys.argv)

                if menu2=='1':
                    def timing_2():
                        print("[1] 10:00-13:00")
                        print("[2] 13:10-16:10")
                        print("[3] 16:20-19:20")
                        print("[4] exit/quit")
                    timing_2()
                    while True:
                            movies_time2 = input("Enter your option2:")
                            if movies_time2.lower() not in ('1', '2', '3', '4'):
                                print("wrong choice try again.")
                            if movies_time2 == '4':
                                import os
                                import sys
                                os.execl(sys.executable, sys.executable, *sys.argv)

                            if movies_time2 == '1':
                                tikets1_movie2 = int(input("how many person:"))
                                price1_movie2 = tikets1_movie2 * 40
                                print("total=", price1_movie2)
                                conform2=input("send y to conform to cancel send n{y/n}:")
                                if conform2.lower() not in ('y','n'):
                                    print("try again")
                                if conform2=='y':
                                    print("ticket")
                                    print("A Queit Place: Part II")
                                    print("screen:1")
                                    print("10:00-13:00")
                                    print("person:",tikets1_movie2)
                                    exit()
                            if movies_time2 == '2':
                                tikets2_movie2=int(input("how many person:"))
                                price2_movie2=tikets2_movie2 * 40
                                print("total=",price2_movie2)
                                conform2 = input("send y to conform to cancel send n{y/n}:")
                                if conform2.lower() not in ('y', 'n'):
                                    print("try again")
                                if conform2 == 'y':
                                    print("ticket")
                                    print("A Queit Place: Part II")
                                    print("screen:1")
                                    print("13:10-16:10")
                                    print("person:",tikets2_movie2)
                                    exit()
                            if movies_time2 == '3':
                                tikets3_movie2=int(input("how many person:"))
                                price3_movie2=tikets3_movie2 * 40
                                print("total=",price3_movie2)
                                conform2 = input("send y to conform to cancel send n{y/n}:")
                                if conform2.lower() not in ('y', 'n'):
                                    print("try again")
                                if conform2 == 'y':
                                    print("ticket")
                                    print("A Queit Place: Part II")
                                    print("screen:1")
                                    print("16:20-19:20")
                                    print("person:",tikets3_movie2)
                                    exit()
                            else:
                                exit()
                    else:
                        exit()


        if age <16:
            print("Sorry,You are not over 16 years old. You cannot watch this movie.")
            exit()
        else:
            exit()
    age2()

#movie 3
if movies=='3':
    print("Fast and Furious 9")
    def age3():
        age=int(input("Please enter your age:"))
        if age >=10:
            print("You are allowed to see the film. Standard ticket price is 40AED")
            def menu3():
                print("[1] Book a seat")
                print("[2] Movie Description")
                print("[3] exit/quit")
            menu3()
            while True:
                menu3 = input("Enter your option3:")
                if menu3.lower() not in ('1', '2', '3'):
                    print("wrong choice try again.")
                if menu3 == '3':
                    import os
                    import sys
                    os.execl(sys.executable, sys.executable, *sys.argv)
                if menu3=='2':
                    print("Genre: Action","      Cypher enlists the help of Jakob, Dom's younger brother to take revenge on Dom and his team.")
                    print("Running Time: 145 min")
                    print("Release Date: 20 May 2021")
                    print("Starring: John Cena, Charlize Theron, Nathalie Emmanuel, Vin Diesel")
                    print("Language: English")
                    print("Subtitle(s): Arabic")
                    import os
                    import sys
                    os.execl(sys.executable, sys.executable, *sys.argv)

                if menu3=='1':
                    def timing_3():
                        print("[1] 10:00-13:00")
                        print("[2] 13:10-16:10")
                        print("[3] 16:20-19:20")
                        print("[4] exit/quit")
                    timing_3()
                    while True:
                            movies_time3 = input("Enter your option2:")
                            if movies_time3.lower() not in ('1', '2', '3', '4'):
                                print("wrong choice try again.")
                            if movies_time3 == '4':
                                import os
                                import sys
                                os.execl(sys.executable, sys.executable, *sys.argv)

                            if movies_time3 == '1':
                                tikets1_movie3 = int(input("how many person:"))
                                price1_movie3 = tikets1_movie3 * 45
                                print("total=", price1_movie3)
                                conform3=input("send y to conform to cancel send n{y/n}:")
                                if conform3.lower() not in ('y','n'):
                                    print("try again")
                                if conform3=='y':
                                    print("ticket")
                                    print("Fast and Furious 9")
                                    print("screen:1")
                                    print("10:00-13:00")
                                    print("person:",tikets1_movie3)
                                    exit()
                            if movies_time3 == '2':
                                tikets2_movie3=int(input("how many person:"))
                                price2_movie3=tikets2_movie3 * 45
                                print("total=",price2_movie3)
                                conform3 = input("send y to conform to cancel send n{y/n}:")
                                if conform3.lower() not in ('y', 'n'):
                                    print("try again")
                                if conform3 == 'y':
                                    print("ticket")
                                    print("Fast and Furious 9")
                                    print("screen:1")
                                    print("13:10-16:10")
                                    print("person:",tikets2_movie3)
                                    exit()
                            if movies_time3 == '3':
                                tikets3_movie3=int(input("how many person:"))
                                price3_movie3=tikets3_movie3 * 45
                                print("total=",price3_movie3)
                                conform3 = input("send y to conform to cancel send n{y/n}:")
                                if conform3.lower() not in ('y', 'n'):
                                    print("try again")
                                if conform3 == 'y':
                                    print("ticket")
                                    print("Fast and Furious 9")
                                    print("screen:1")
                                    print("16:20-19:20")
                                    print("person:",tikets3_movie3)
                                    exit()
                            else:
                                exit()
                    else:
                        exit()


        if age <10:
            print("Sorry,You are not over 10 years old. You cannot watch this movie.")
            exit()
        else:
            exit()
    age3()

