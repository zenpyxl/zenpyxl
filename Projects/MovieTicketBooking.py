import pickle
import time
import random
from datetime import datetime

def search(path):
    movie_name = input("Enter Movie name to search: ")
    
    try:
        with open("E:\\Projects\\moviedata.dat", "rb") as file:
            loaded_movies = pickle.load(file)
        
        found = False
        for movie in loaded_movies:
            if movie_name.lower() in movie["name"].lower():
                found = True
                print(f"---------- {movie['name']} ----------\n")
                print(movie["screen"])
                print(movie["language"])
                print(movie["duration"])
                print(movie["genre"])
                print(movie["film certification"])
                print(movie["release"])
                print(movie["about"], '\n')
                print("----------------------------------------------------------------------------------------------")
                print(f"Home > {path} > {movie['language']} > {movie['name']}")
                print("----------------------------------------------------------------------------------------------")
        
        if not found:
            print("No such movie found.\n")
            print("----------------------------------------------------------------------------------------------")
            print(f"Home > {path} > Error")
            print("----------------------------------------------------------------------------------------------")
    
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return ()
    
def movies():
    print("\n-=-=-=-=-=-=-=-=-=-=- Filters -=-=-=-=-=-=-=-=-=-=-\n")
    print("1. English")
    print("2. Hindi हिंदी")
    print("3. Tamil தமிழ்")
    print("4. Kannada ಕನ್ನಡ")
    print("5. Malayalam മലയാളം")
    print("6. Telugu తెలుగు")
    print("7. Back\n")
    print("----------------------------------------------------------------------------------------------")
    print("Home > Movies")
    print("----------------------------------------------------------------------------------------------")
    opt_movies1=int(input("Enter your option(1..7):"))
    if(opt_movies1==1):
        movies_english()
    elif(opt_movies1==2):
        movies_hindi()
    elif(opt_movies1==3):
        movies_tamil()
    elif(opt_movies1==4):
        movies_kannada()
    elif(opt_movies1==5):
        movies_malayalam()
    elif(opt_movies1==6):
        movies_telugu()

def movies_english():
    print("\n-=-=-=-=-=-=-=-=-=-=- English -=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Killers of the Flower Moon")
    print("A\nEnglish\n")
    print("2. Top Gun: Maverick")
    print("UA\nEnglish\n")
    print("3. Five Nights at Freddy`s")
    print("A\nEnglish\n")
    print("4. The Exorcist: Believer")
    print("A\nEnglish\n")
    print("5. The Nun II")
    print("A\nEnglish\n")
    print("6. Interstellar")
    print("13+\nEnglish\n")
    print("7. Back\n")
    print("----------------------------------------------------------------------------------------------")
    print("Home > Movies > English")
    print("----------------------------------------------------------------------------------------------")
    opt_movie_english1=int(input("Enter your option(1..7):"))
    if(opt_movie_english1==1):
        moviename="Killers of the Flower Moon"
        movielook(moviename)        
    elif(opt_movie_english1==2):
        moviename="Top Gun: Maverick"
        movielook(moviename)    
    elif(opt_movie_english1==3):
        moviename="Five Nights at Freddy`s"
        movielook(moviename)    
    elif(opt_movie_english1==4):
        moviename="The Exorcist: Believer"
        movielook(moviename)    
    elif(opt_movie_english1==5):
        moviename="The Nun II"
        movielook(moviename)    
    elif(opt_movie_english1==6):
        moviename="Interstellar"
        movielook(moviename) 
    elif(opt_movie_english1==7):
        movies()
            
def movies_hindi():
    print("\n-=-=-=-=-=-=-=-=-=-=- Hindi हिंदी -=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Jawan")
    print("UA\nHindi\n")
    print("2. Pathaan")
    print("UA\nHindi\n")
    print("3. War")
    print("UA\nHindi\n")
    print("4. Tiger Zinda Hai")
    print("UA\nHindi\n")
    print("5. Back\n")
    print("----------------------------------------------------------------------------------------------")
    print("Home > Movies > Hindi")
    print("----------------------------------------------------------------------------------------------")
    opt_movie_hindi1=int(input("Enter your option(1..5):"))
    if(opt_movie_hindi1==1):
        moviename="Jawan"
        movielook(moviename)
    elif(opt_movie_hindi1==2):
        moviename="Pathaan"
        movielook(moviename)
    elif(opt_movie_hindi1==3):
        moviename="War"
        movielook(moviename)
    elif(opt_movie_hindi1==4):
        moviename="Tiger Zinda Hai"
        movielook(moviename)
    elif(opt_movie_hindi1==5):
        movies()

def movies_tamil():
    print("\n-=-=-=-=-=-=-=-=-=-=- Tamil தமிழ் -=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Leo")
    print("UA\nTamil\n")
    print("2. Back")
    print("----------------------------------------------------------------------------------------------")
    print("Home > Movies > Tamil")
    print("----------------------------------------------------------------------------------------------")
    opt_movies_tamil1=int(input("Enter your option(1..2):"))
    if(opt_movies_tamil1==1):
        moviename="Leo"
        movielook(moviename)
    elif(opt_movies_tamil1==2):
        movies()

def movies_kannada():
    print("\n-=-=-=-=-=-=-=-=-=-=- Kannada ಕನ್ನಡ -=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Martin")
    print("Not yet rated\nKannada\n")
    print("2. Back")
    print("----------------------------------------------------------------------------------------------")
    print("Home > Movies > Kannada")
    print("----------------------------------------------------------------------------------------------")
    opt_movies_kannada1=int(input("Enter your option(1..2):"))
    if(opt_movies_kannada1==1):
        moviename="Martin"
        movielook(moviename)
    elif(opt_movies_kannada1==2):
        movies()

def movies_malayalam():
    print("\n-=-=-=-=-=-=-=-=-=-=- Malayalam മലയാളം -=-=-=-=-=-=-=-=-=-=-\n")
    print("1. RDX")
    print("UA\nMalayalam\n")
    print("2. Kannur Squad")
    print("UA\nMalayalam\n")
    print("3. Back")
    print("----------------------------------------------------------------------------------------------")
    print("Home > Movies > Malayalam")
    print("----------------------------------------------------------------------------------------------")
    opt_movies_malayalam1=int(input("Enter your option(1..3):"))
    if(opt_movies_malayalam1==1):
        moviename="RDX"
        movielook(moviename)
    elif(opt_movies_malayalam1==2):
        moviename="Kannur Squad"
        movielook(moviename)
    elif(opt_movies_malayalam1==3):
        movies()

def movies_telugu():
    print("\n-=-=-=-=-=-=-=-=-=-=- Kannada ಕನ್ನಡ -=-=-=-=-=-=-=-=-=-=-\n")
    print("1. Salaar: Cease Fire - Part 1")
    print("Not yet rated\nTelugu\n")
    print("2. Back")
    print("----------------------------------------------------------------------------------------------")
    print("Home > Movies > Telegu")
    print("----------------------------------------------------------------------------------------------")
    opt_movies_telugu1=int(input("Enter your option(1..2):"))
    if(opt_movies_telugu1==1):
        moviename="Salaar: Cease Fire - Part 1"
        movielook(moviename)
    elif(opt_movies_telugu1==2):
        movies()

def movielook(movie_name):
    loaded_movies = pickle.load(open("E:\\Projects\\moviedata.dat", "rb"))
    found=False
    for movie in loaded_movies:
        if movie["name"] == movie_name:
            found=True
            print("----------", movie["name"], "----------", '\n')
            print(movie["screen"])
            print(movie["language"])
            print(movie["duration"])
            print(movie["genre"])
            print(movie["film certification"])
            print(movie["release"])
            print(movie["about"], '\n')
            if movie["film certification"]=="Not yet rated":
                print("Booking not available.")
            elif movie["film certification"]=="A":
                print("CONTENT WARNING\nThis movie is rated `A` and its only for viewers above\n18. Please carry a valid ID/Age Proof to the theatre.\n")
                book=input("Book Tickets (Y/N): ")
                if book=='y' or booking=='Y':
                    booking(movie)    
                else:
                    print()               
            else:
                book=input("Book Tickets (Y/N): ")
                print("----------------------------------------------------------------------------------------------")
                print("Home > Movies >",movie["language"],">",movie["name"])
                print("----------------------------------------------------------------------------------------------")
                if book=='y' or booking=='Y':
                    booking(movie,movie_name)    
                else:
                    print()    
    if found==False:
            print("Error")
            print("----------------------------------------------------------------------------------------------")
            print("Home > Movies > Error404")
            print("----------------------------------------------------------------------------------------------")
    open("E:\\Projects\\moviedata.dat", "rb").close() 
    return()

def adminpanel():
    print("-=-=-=-=-=-=-=-=-=-=- ADMINPANEL -=-=-=-=-=-=-=-=-=-=-")
    print("1. Add movies")
    print("2. Delete movies")
    print("3. Show movies")
    print("4. Modify movie")
    print("5. Exit")
    opt_adminpanel_input=int(input("Enter your option(1..5):"))
    if opt_adminpanel_input==1:
        admin_add_movies()
    elif opt_adminpanel_input==2:
        admin_del_movies()
    elif opt_adminpanel_input==3:
        admin_show_movies()
    elif opt_adminpanel_input==4:
        admin_modify_movie()
    
def admin_add_movies():
    opt='Y'
    while opt=='Y'or opt=='y':
        start_time = time.time()
        try:
            file = open("E:\\Projects\\moviedata.dat", "rb")
            existing_movies = pickle.load(file)
            file.close()
        except FileNotFoundError:
            existing_movies = []
        list_of_movies = []
        no_of_movies = int(input("Enter the number of movies you want to add:"))
        for i in range(no_of_movies):
            movie_data = {}
            movie_data["name"] = input("Enter movie name:")
            movie_data["screen"] = input("Enter screen type:")
            movie_data["language"] = input("Enter language:")
            movie_data["duration"] = input("Enter duration:")
            movie_data["genre"] = input("Enter movie genre:")
            movie_data["film certification"] = input("Enter film certification rating:")
            movie_data["release"] = input("Enter movie release date:")
            movie_data["about"] = input("Enter description:")
            list_of_movies.append(movie_data)
        all_movies = existing_movies + list_of_movies

        file = open("E:\\Projects\\moviedata.dat", "wb")
        pickle.dump(all_movies, file)
        print(no_of_movies,"successfully added.")
        file.close()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: ",float(elapsed_time)," seconds")
        opt=input("Do you want to continue(Y or N):")

def admin_del_movies():
    no_movies_del=int(input("Enter the no of movies to be deleted:"))
    for i in range(no_movies_del):
        start_time = time.time()
        try:
            with open("E:\\Projects\\moviedata.dat", "rb") as file:
                existing_movies = pickle.load(file)
        except FileNotFoundError:
            print("No movies found.")
            return

        movie_name_to_delete = input("Enter the name of the movie to delete:")

        movie_found = False
        for movie in existing_movies:
            if movie["name"] == movie_name_to_delete:
                existing_movies.remove(movie)
                movie_found = True
                break

        if not movie_found:
            print("Movie not found.")
        else:
            with open("E:\\Projects\\moviedata.dat", "wb") as file:
                pickle.dump(existing_movies, file)
            print("Movie deleted successfully.")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")

def admin_show_movies():
    file = open("E:\\Projects\\moviedata.dat", "rb")
    loaded_movies = pickle.load(file)
    file.close()
    for movie in loaded_movies:
        print("\n----------", movie["name"], "----------")
        print("Screen:", movie["screen"])
        print("Language:", movie["language"])
        print("Duration:", movie["duration"])
        print("Genre:", movie["genre"])
        print("Film Certification:", movie["film certification"])
        print("Release Date:", movie["release"])
        print("Description:", movie["about"])

def admin_modify_movie():
    start_time = time.time()
    try:
        with open("E:\\Projects\\moviedata.dat", "rb") as file:
            existing_movies = pickle.load(file)
    except FileNotFoundError:
        print("No movies found.")
        return

    movie_name_to_modify = input("Enter the name of the movie to modify:")

    movie_found = False
    for movie in existing_movies:
        if movie["name"] == movie_name_to_modify:
            movie["duration"] = input("Enter the new duration:")
            movie["film certification"] = input("Enter the new film certification rating:")
            movie["about"] = input("Enter the new description:")
            movie_found = True
            break

    if not movie_found:
        print("Movie not found.")
    else:
        with open("E:\\Projects\\moviedata.dat", "wb") as file:
            pickle.dump(existing_movies, file)
        print("Movie details modified successfully.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time} seconds")

def booking(movie,movie_name):
    seat_data={}
    print("----------","Booking Panel","----------",'\n')
    print(movie["name"],'-',movie["language"],'\n')
    current_datetime = datetime.now()
    date = current_datetime.strftime("%d/%m/%Y")
    print(f"{date}"," ",end='')
    time = current_datetime.strftime("%H:%M:%S")
    print(f"{time}\n")
    print("1. PVR: Lulu, Trivandrum\nFood & Beverage\n")
    print("2. Ariesplex SL Cinemas\nFood & Beverage\n")
    print("3. Greenfield Moviemax Cinemas: Trivandrum\nFood & Beverage\n")
    print("4. New Theater: Trivandrum\n")
    print("5. PVR: Kripa, Thampanoor Trivandrum\nFood & Beverage\n")
    print("6. Back\n")
    opt_booking1=int(input("Enter your option(1..6):"))
    if(opt_booking1==1):
        theatrename = "PVR: Lulu, Trivandrum"
        print("---------- Choose Seat class ----------\n")
        print("1. CLASSIC  - Rs. 480")
        print("2. PRIME    - Rs. 530")
        print("3. RECLINER - Rs. 830")
        print("4. Back\n")
        opt_booking_type1=int(input("Enter your option(1..4):"))
        print("----------------------------------------------------------------------------------------------")
        print("Home > Movies >",movie["language"],">",movie["name"],"> Booking")
        print("----------------------------------------------------------------------------------------------")
        if(opt_booking_type1==1):
            seat_type = "CLASSIC"
            seats_available = random.randint(0, 60)
            seat_cost=480
            seat_data={}
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

        elif(opt_booking_type1==2):
            seat_type = "PRIME"
            seats_available = random.randint(0, 39)
            seat_cost=530
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

        elif(opt_booking_type1==3):
            seat_type = "RECLINER"
            seats_available = random.randint(0, 8)
            seat_cost=830
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

    elif(opt_booking1==2):   
        theatrename = "Ariesplex SL Cinemas"
        print("---------- Choose Seat class ----------\n")
        print("1. EXECUTIVE - Rs. 160")
        print("2. GOLD      - Rs. 180")
        print("3. PLATINUM  - Rs. 480")
        print("4. Back\n") 
        opt_booking_type1=int(input("Enter your option(1..4):"))
        if(opt_booking_type1==1):
            seat_type = "EXECUTIVE"
            seats_available = random.randint(0, 41)
            seat_cost=160
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

        elif(opt_booking_type1==2):
            seat_type = "GOLD"
            seats_available = random.randint(0, 41)
            seat_cost=180
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

        elif(opt_booking_type1==3):
            seat_type = "PLATINUM"
            seats_available = random.randint(0, 24)
            seat_cost=480
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

    elif(opt_booking1==3):   
        theatrename = "Greenfield Moviemax Cinemas: Trivandrum"
        print("---------- Choose Seat class ----------\n")
        print("1. EXECUTIVE - Rs. 150")
        print("2. Back\n") 
        opt_booking_type1=int(input("Enter your option(1..2):"))
        if(opt_booking_type1==1):
            seat_type = "EXECUTIVE"
            seats_available = random.randint(0, 132)
            seat_cost=150
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)
        else:
            print()
            
    elif(opt_booking1==4):
        theatrename = "New Theater: Trivandrum"
        print("---------- Choose Seat class ----------\n")
        print("1. FAMILY CIRCLE - Rs. 150.00")
        print("2. ROYAL CIRCLE  - Rs. 250.00")
        print("3. Back\n") 
        opt_booking_type1=int(input("Enter your option(1..3):"))
        if(opt_booking_type1==1):
            seat_type = "FAMILY CIRCLE"
            seats_available = random.randint(0, 200)
            seat_cost=150
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

        elif(opt_booking_type1==2):
            seat_type = "ROYAL CIRCLE"
            seats_available = random.randint(0, 316)
            seat_cost=250
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)
        
    elif(opt_booking1==5):   
        theatrename = "PVR: Kripa, Thampanoor Trivandrum"
        print("---------- Choose Seat class ----------\n")
        print("1. CLASSIC - Rs. 140")
        print("2. PRIME   - Rs. 160")
        print("3. Back\n") 
        opt_booking_type1=int(input("Enter your option(1..3):"))
        if(opt_booking_type1==1):
            seat_type = "CLASSIC"
            seats_available = random.randint(0, 240)
            seat_cost=140
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

        elif(opt_booking_type1==2):
            seat_type ="PRIME"
            seats_available = random.randint(0, 16)
            seat_cost=160
            seat_data["type"] = seat_type
            seat_data["available"] = seats_available
            seat_data["cost"] = seat_cost
            seat_selection(seat_data,theatrename)

    else:
        movielook(movie_name)

def seat_selection(seat_data,theatrename):
            print("\nNo of seats available: ", seat_data["available"])
            seatnos=int(input("Enter Number of Seats: "))
            if seatnos>seat_data["available"]:
                print("\nRequired amount of seats not available.")
            else:
                cost=seat_data["cost"]*seatnos
                print("\nPay -",cost,'\n')
                food(cost,seatnos,theatrename,seat_data)

def food(cost,seatnos,theatrename,seat_data):
    cart=[]
    opt='Y'
    while opt=='Y'or opt=='y':
        print("----------","Add Meal","----------",)
        print("1. Cheese Popcorn    - Rs. 140 ~ Rs. 260")
        print("2. Classic Popcorn   - Rs. 110 ~ Rs. 220")
        print("3. Chicken Popcorn   - Rs. 160")
        print("4. Pepsi             - Rs. 110 ~ Rs. 160")
        print("5. French Fries      - Rs. 160")
        print("6. Chicken Nuggets   - Rs. 160")
        print("7. Nachos            - Rs. 130")
        print("8. Cold Coffee       - Rs. 120")
        print("9. Chocolate Coffee  - Rs. 140")
        print("10. Skip")
        opt_food1=int(input("Enter your option(1..10):"))
        if(opt_food1==1):
            print('\n',"----------","Choose Type","----------",)
            print("1. Cheese Popcorn (Regular) - Rs. 140")
            print("2. Cheese Popcorn (Medium)  - Rs. 190")
            print("3. Cheese Popcorn (Large)   - Rs. 260")
            print("4. Back")
            opt_food_size1=int(input("Enter your option(1..4):"))
            if opt_food_size1==1:
                menu_item = "Cheese Popcorn (Regular)"
                price = 140
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})
                    
            elif opt_food_size1==2:
                menu_item = "Cheese Popcorn (Medium)"
                price = 190
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})
                
            elif opt_food_size1==3:
                menu_item = "Cheese Popcorn (Large)"
                price = 260
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})

        elif(opt_food1==2):
            print('\n',"----------","Choose Type","----------",)
            print("1. Classic Popcorn (Regular) - Rs. 110")
            print("2. Classic Popcorn (medium)  - Rs. 160")
            print("3. Classic Popcorn (Large)   - Rs. 220")
            print("4. Back")
            opt_food_size1=int(input("Enter your option(1..4):"))
            if opt_food_size1==1:
                menu_item = "Classic Popcorn (Regular)"
                price = 110
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})

            elif opt_food_size1==2:
                menu_item = "Classic Popcorn (Medium)"
                price = 160
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})

            elif opt_food_size1==3:
                menu_item = "Classic Popcorn (Large)"
                price = 220
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})

        elif(opt_food1==3):
            menu_item = "Chicken Popcorn"
            price = 160
            qtn=int(input("Enter quantity: "))
            qtn1='x'+str(qtn)
            price1=str(price*qtn)
            cart.append({'name': menu_item+qtn1, 'price': int(price1)})

        elif(opt_food1==4):
            print('\n',"----------","Choose Type","----------",)
            print("1. Pepsi (Regular) - Rs. 110")
            print("2. Pepsi (medium)  - Rs. 140")
            print("3. Pepsi (Large)   - Rs. 160")
            print("4. Back")
            opt_food_size1=int(input("Enter your option(1..4):"))
            if opt_food_size1==1:
                menu_item = "Pepsi (Regular)"
                price = 110
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)}) 

            elif opt_food_size1==2:
                menu_item = "Pepsi (Medium)"
                price = 140
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})

            elif opt_food_size1==3:
                menu_item = "Pepsi (large)"
                price = 160
                qtn=int(input("Enter quantity: "))
                qtn1='x'+str(qtn)
                price1=str(price*qtn)
                cart.append({'name': menu_item+qtn1, 'price': int(price1)})                 

        elif(opt_food1==5):
            menu_item = "French Fries"
            price = 160
            qtn=int(input("Enter quantity: "))
            qtn1='x'+str(qtn)
            price1=str(price*qtn)
            cart.append({'name': menu_item+qtn1, 'price': int(price1)})  

        elif(opt_food1==6):
            menu_item = "Chicken Nuggets"
            price = 160
            qtn=int(input("Enter quantity: "))
            qtn1='x'+str(qtn)
            price1=str(price*qtn)
            cart.append({'name': menu_item+qtn1, 'price': int(price1)})              

        elif(opt_food1==7):
            menu_item = "Nachos"
            price = 130
            qtn=int(input("Enter quantity: "))
            qtn1='x'+str(qtn)
            price1=str(price*qtn)
            cart.append({'name': menu_item+qtn1, 'price': int(price1)})          

        elif(opt_food1==8):
            menu_item = "Cold Coffee"
            price = 120
            qtn=int(input("Enter quantity: "))
            qtn1='x'+str(qtn)
            price1=str(price*qtn)
            cart.append({'name': menu_item+qtn1, 'price': int(price1)})          

        elif(opt_food1==9):
            menu_item = "Chocolate Coffee"
            price = 140
            qtn=int(input("Enter quantity: "))
            qtn1='x'+str(qtn)
            price1=str(price*qtn)
            cart.append({'name': menu_item+qtn1, 'price': int(price1)})          
                
        elif(opt_food1==10):
            print()
        opt=input("Do you want to continue to add more meal(s)? (Y or N):")
    food_cost = sum(item['price'] for item in cart)
    book_summary(cost,seat_data,seatnos,theatrename,food_cost,cart)

def book_summary(cost,seat_data,seatnos,theatrename,food_cost,cart):
        amount_data={}
        amount_data["food_cost"]=food_cost
        amount_data["cost"]=cost
        amount_data["base_amount"] = cost*18.75/100
        amount_data["gst"] = amount_data["base_amount"]*18/100
        amount_data["convenience_fees"] = amount_data["gst"]+amount_data["base_amount"]
        amount_data["totcost"] = int(food_cost+amount_data["convenience_fees"]+cost)
        print("----------","Booking Summary","----------","\n")
        print(seat_data["type"],"-",seatnos,"Tickets")
        print(theatrename)
        print("                               ","Rs.",cost,'\n')
        print("Convenience fees               ","Rs.",amount_data["convenience_fees"])
        print("Base Amount                    ","Rs.",amount_data["base_amount"])
        print("Integrated GST (IGST) @ 18%    ","Rs.",amount_data["gst"],"\n")
        print("Food & Beverage                ","Rs.",food_cost)
        print("---------- Cart Contents ----------")
        for item in cart:
            print(f"{item['name']}: Rs. {item['price']}")
            print("-----------------------------------")
        print("Sub Total                      ","Rs.",amount_data["totcost"])
        opt=input("\nDo you want to continue(Y or N):")
        if opt=='Y' or opt=='y':
            print("\n-=-=-=-=-=-=-=-=-=-=- LOG-IN -=-=-=-=-=-=-=-=-=-=-\n")
            username=input("USERNAME:")
            password=input("PASSWORD:")
            loaded_userdata = pickle.load(open("E:\\Projects\\userdata.dat", "rb"))
            found=False
            for userdata in loaded_userdata:
                if userdata["name"] == username and userdata["password"] == password:
                    payment(amount_data,seat_data,theatrename,seatnos,cart,username)
                elif username=="admin1" and password=="xyz":
                    adminpanel()
                else:
                    print("Wrong username or password.")
        else:
            print()

def payment(amount_data,seat_data,theatrename,seatnos,cart,username):
    print("\n----------","Payment Panel","----------\n")
    print("1. Debit/Credit Card")
    print("2. Net Banking")
    print("3. Mobile Wallets")
    print("4. Exit\n")
    opt_payment1=int(input("Enter your option(1..4):"))
    if(opt_payment1==1):
        print("\nEnter your Card details\n")
        cardno=int(input("Card Number: "))
        name=input("Name on the card: ")
        print("Expiry")
        mm=int(input("MM: "))
        yy=int(input("YY: "))
        cvv=int(input("CVV"))
        print("\nBy clicking `Make Payment` you agree to the terms and conditions\n")
        opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
        if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
            pay=int(input("Enter the amount to be paid: "))
            str1=''
            if pay==amount_data['totcost']:
                print("Payment in process",end='')
                for i in range(4):
                    time.sleep(0.5)
                    print(str1,end='')
                    str1=''+'.'
                print("Payment successful!")
                receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
        else:
            print()

    elif(opt_payment1==2):
        print("\n---------- Pay using Net Banking ----------\n")
        print("1. State Bank of India")
        print("2. HDFC Bank")
        print("3. ICICI Bank")
        print("4. Axis Bank")
        print("5. Back")
        str1=''
        opt_payment_choice1=int(input("Enter your option(1..5):"))

        if(opt_payment_choice1==1):
            print("Redirecting",end='')
            for i in range(4):
                time.sleep(0.5)
                print(str1,end='')
                str1=''+'.'
            print("\n-=-=-=-=-=-=-=-=-=-=- State Bank of India -=-=-=-=-=-=-=-=-=-=-\n")
            phno=input("Enter phone number: ")
            if len(phno)==10:
                opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
                if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
                    pay=int(input("Enter the amount to be paid: "))
                    str1=''
                    if pay==amount_data["totcost"]:
                        print("Payment in process",end='')
                        for i in range(4):
                            time.sleep(0.5)
                            print(str1,end='')
                            str1=''+'.'
                        print("Payment successful!")
                        receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
            else:
                print("Invalid Phone number.")

        elif(opt_payment_choice1==2):
            print("Redirecting",end='')
            for i in range(4):
                time.sleep(0.5)
                print(str1,end='')
                str1=''+'.'
            print("\n-=-=-=-=-=-=-=-=-=-=- HDFC Bank -=-=-=-=-=-=-=-=-=-=-\n")   
            phno=input("Enter phone number: ")
            if len(phno)==10:
                opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
                if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
                    pay=int(input("Enter the amount to be paid: "))
                    str1=''
                    if pay==amount_data["totcost"]:
                        print("Payment in process",end='')
                        for i in range(4):
                            time.sleep(0.5)
                            print(str1,end='')
                            str1=''+'.'
                        print("Payment successful!")
                        receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
            else:
                print("Invalid Phone number.")
        
        elif(opt_payment_choice1==3):
            print("Redirecting",end='')
            for i in range(4):
                time.sleep(0.5)
                print(str1,end='')
                str1=''+'.'
            print("\n-=-=-=-=-=-=-=-=-=-=- ICICI Bank -=-=-=-=-=-=-=-=-=-=-\n")
            phno=input("Enter phone number: ")
            if len(phno)==10:
                opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
                if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
                    pay=int(input("Enter the amount to be paid: "))
                    str1=''
                    if pay==amount_data["totcost"]:
                        print("Payment in process",end='')
                        for i in range(4):
                            time.sleep(0.5)
                            print(str1,end='')
                            str1=''+'.'
                        print("Payment successful!")
                        receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
            else:
                print("Invalid Phone number.")

        elif(opt_payment_choice1==4):
            print("Redirecting",end='')
            for i in range(4):
                time.sleep(0.5)
                print(str1,end='')
                str1=''+'.'
            print("\n-=-=-=-=-=-=-=-=-=-=- Axis Bank -=-=-=-=-=-=-=-=-=-=-\n")
            phno=input("Enter phone number: ")
            if len(phno)==10:
                opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
                if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
                    pay=int(input("Enter the amount to be paid: "))
                    str1=''
                    if pay==amount_data["totcost"]:
                        print("Payment in process",end='')
                        for i in range(4):
                            time.sleep(0.5)
                            print(str1,end='')
                            str1=''+'.'
                        print("Payment successful!")
                        receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
            else:
                print("Invalid Phone number.")                      

        else:
            print()

    elif(opt_payment1==3):
        print("\n---------- Pay Using Wallets ----------\n")
        print("1. PAYTM")
        print("2. AMAZONPAY")
        print("3. GOOGLEPAY")
        print("4. Back")
        opt_payment_choice1=int(input("Enter your option(1..4):"))
        if(opt_payment_choice1==1):
            print("\n-=-=-=-=-=-=-=-=-=-=- PAYTM -=-=-=-=-=-=-=-=-=-=-\n")
            phno=input("Enter phone number: ")
            if len(phno)==10:
                opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
                if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
                    pay=int(input("Enter the amount to be paid: "))
                    str1=''
                    if pay==amount_data["totcost"]:
                        print("Payment in process",end='')
                        for i in range(4):
                            time.sleep(0.5)
                            print(str1,end='')
                            str1=''+'.'
                        print("Payment successful!")
                        receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
        
        elif(opt_payment_choice1==2):
            print("\n-=-=-=-=-=-=-=-=-=-=- AMAZONPAY -=-=-=-=-=-=-=-=-=-=-\n")
            phno=input("Enter phone number: ")
            if len(phno)==10:
                opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
                if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
                    pay=int(input("Enter the amount to be paid: "))
                    str1=''
                    if pay==amount_data["totcost"]:
                        print("Payment in process",end='')
                        for i in range(4):
                            time.sleep(0.5)
                            print(str1,end='')
                            str1=''+'.'
                        print("Payment successful!")
                        receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
        
        elif(opt_payment_choice1==3):
            print("\n-=-=-=-=-=-=-=-=-=-=- GOOGLEPAY -=-=-=-=-=-=-=-=-=-=-\n")
            phno=input("Enter phone number: ")
            if len(phno)==10:
                opt_payment_choice1=input("MAKE PAYMENT (Y/N):")
                if(opt_payment_choice1=='y' or opt_payment_choice1=='Y'):
                    pay=int(input("Enter the amount to be paid: "))
                    str1=''
                    if pay==amount_data["totcost"]:
                        print("Payment in process",end='')
                        for i in range(4):
                            time.sleep(0.5)
                            print(str1,end='')
                            str1=''+'.'
                        print("Payment successful!")
                        receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username)
    
    else:
        print()       
def receipt_input(amount_data,seat_data,theatrename,seatnos,cart,username):
    with open('E:\\Projects\\booking_summary_'+username+'.txt', 'w') as file:
        file.write("---------- Booking Summary ----------\n")
        inp = str(seat_data["type"]) + '-' + str(seatnos) + " Tickets"
        file.write(inp)
        file.write(theatrename)
        file.write(f"                               Rs. {amount_data['cost']}\n")
        file.write(f"Convenience fees               Rs. {amount_data['convenience_fees']}\n")
        file.write(f"Base Amount                    Rs. {amount_data['base_amount']}\n")
        file.write(f"Integrated GST (IGST) @ 18%    Rs. {amount_data['gst']}\n")
        file.write(f"Food & Beverage                Rs. {amount_data['food_cost']}\n")
        file.write("---------- Cart Contents ----------\n")
        for item in cart:
            file.write(f"{item['name']}: Rs. {item['price']}\n")
            file.write("-----------------------------------\n")
        file.write(f"Sub Total                      Rs. {amount_data['totcost']}\n")

def receipt(username):
    file_path = f'E:\\Projects\\booking_summary_{username}.txt'
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("\nNo current booking(s)")
    except FileNotFoundError:
        print("\nNo current booking(s)")

#MAIN PROGRAM
print("-=-=-=-=-=-=-=-=-=-=- Welcome to BlockBusterCinemas -=-=-=-=-=-=-=-=-=-=-\n")
print("`````````````````````````")
print("1. Search")
print("2. Movies")
print("3. Sign-in/Log-in")
print("4. Exit")
print("`````````````````````````")
opt_main1=int(input("Enter your option(1..4):"))
if(opt_main1==1):
    path="Search"
    search(path)
elif(opt_main1==2):
    movies()
elif(opt_main1==3):
    print("\n`````````````````````````")
    print("1. Log-in")
    print("2. Sign-in")
    print("3. Back")
    print("``````````````````````````")
    opt_main_auth1=int(input("Enter your option(1..3):"))
    if(opt_main_auth1==1):
        print("\n-=-=-=-=-=-=-=-=-=-=- LOG-IN -=-=-=-=-=-=-=-=-=-=-\n")
        username=input("USERNAME:")
        password=input("PASSWORD:")
        loaded_userdata = pickle.load(open("E:\\Projects\\userdata.dat", "rb"))
        found=False
        for userdata in loaded_userdata:
            if userdata["name"] == username and userdata["password"] == password:
                print("\n`````````````````````````")
                print("Welcome",username,'!')
                print("`````````````````````````\n")
                print("1. Review Booking")
                print("2. Back")
                opt_main_auth_choice=int(input("Enter your option(1..2):"))
                if(opt_main_auth_choice==1):
                    receipt(username)
                else:
                    print()

            elif username=="admin1" and password=="xyz":
                adminpanel()

            else:
                print("Wrong username or password.")
            
        
    elif(opt_main_auth1==2):
        print("\n-=-=-=-=-=-=-=-=-=-=- SIGN-IN -=-=-=-=-=-=-=-=-=-=-\n")
        print("Create New Account\n")
        print("``````````````````````````")
        username=input("USERNAME:")
        password=input("PASSWORD:")
        print("``````````````````````````")
        try:
            file = open("E:\\Projects\\userdata.dat", "rb")
            existing_users = pickle.load(file)
            file.close()
        except FileNotFoundError:
            existing_users = []
        list_of_users = []
        user_data = {}
        user_data["name"] = username
        user_data["password"] = password
        list_of_users.append(user_data)
        all_users = existing_users + list_of_users 

        file = open("E:\\Projects\\userdata.dat", "wb")
        pickle.dump(all_users, file)
        print("Account successfully created.")
        file.close()

elif(opt_main1==4):
    print()


