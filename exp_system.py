import pandas as pd

df=pd.read_csv('cars.csv')
df.loc[df["doors"] == "04-May", "doors"] = 4
df.loc[df["doors"] == "02-Mar", "doors"] = 2
df['category'] = df['category'].str.lower()
df.loc[df['category'] == 'goods wagon', 'category'] = 'wagon'
df['leather_interior'] = df['leather_interior'].str.lower()
df['fuel_type'] = df['fuel_type'].str.lower()
df.loc[df["fuel_type"] == "plug-in hybrid", "fuel_type"] = 'plug-in'
df['gear_box_type'] = df['gear_box_type'].str.lower()
df['drive_wheels'] = df['drive_wheels'].str.lower()
df['color'] = df['color'].str.lower()

df = df.dropna()

new_df = df.copy()

#Inputs 

def get_budget():
    budget = input("Enter your budget: ")
    if(budget.isdigit() and int(budget) > 0):
        return budget
    else:
        print("Please enter a valid budget.")
        get_budget()

def get_year(years):
    year = input("Enter car make year that you wanted from the years between 2000 and 2019: ")
    if(year.isdigit() and (int(year) in years)):
        return year
    else:
        print("Please enter a valid year within the range of 2000 and 2019.")
        get_year(years)
    
def get_fueltype_input(fuel_list):
    fuel_type = input("Enter fuel type from the list available "+str(fuel_list)+": ")
    if(fuel_type.lower() in fuel_list):
        return fuel_type
    else:
        print("Please enter a valid fuel type.")
        get_fueltype_input(fuel_list)
    
def get_geartype_input(gear_list):
    gear_type = input("Enter gear type from the list available "+str(gear_list)+": ")
    if(gear_type.lower() in gear_list):
        return gear_type
    else:
        print("Please enter a valid gear type.")
        get_geartype_input(gear_list)
    
def get_color_input(color_list):
    color = input("Enter car color from the list available "+str(color_list)+": ")
    if(color.lower() in color_list):
        return color
    else:
        print("Please enter a valid color from the list.")
        get_color_input(color_list)

def get_car_category_input(cat_list):
    category = input("Enter car category from the list available "+str(cat_list)+": ")
    if(category.lower() in cat_list):
        return category
    else:
        print("Please enter a valid category from the list.")
        get_car_category_input(cat_list)


#List
def get_color(color_choice, data_list):
    if(color_choice == "green"):
        return data_list.query('color == "green"')
    elif(color_choice == "blue"):
        return data_list.query('color == "blue"')
    elif(color_choice == "red"):
        return data_list.query('color == "red"')
    elif(color_choice == "black"):
        return data_list.query('color == "black"')
    elif(color_choice == "white"):
        return data_list.query('color == "white"')
    elif(color_choice == "silver"):
        return data_list.query('color == "silver"')
    elif(color_choice == "yellow"):
        return data_list.query('color == "yellow"')
    elif(color_choice == "orange"):
        return data_list.query('color == "orange"')
    elif(color_choice == "purple"):
        return data_list.query('color == "purple"')
    elif(color_choice == "brown"):
        return data_list.query('color == "brown"')
    elif(color_choice == "grey"):
        return data_list.query('color == "grey"')
    elif(color_choice == "pink"):
        return data_list.query('color == "pink"')
    elif(color_choice == "beige"):
        return data_list.query('color == "beige"')
    elif(color_choice == "multi"):
        return data_list.query('color == "multi"')
    elif(color_choice == "sky blue"):
        return data_list.query('color == "sky blue"')
    elif(color_choice == "carnelian red "):
        return data_list.query('color == "carnelian red"')
    elif(color_choice == "golden"):
        return data_list.query('color == "golden"')

def get_wheels_type(wheels, data_list):
    if wheels == "front":
        return data_list.query('drive_wheels == "front"')
    elif wheels == "rear": 
        return data_list.query('drive_wheels == "rear"')
    elif wheels == "4X4":
        return data_list.query('drive_wheels == "4X4"')
    else:
        return 0

def price_range(choice):
    if choice <300:
        return new_df.query('price < 300')
    elif choice <=300 and choice < 600:
        return new_df.query('price >=300 and price <600')
    elif choice >=600 and choice < 1000:
        return new_df.query('price >= 600 and price < 1000')
    elif choice >=1000 and choice < 2000:
         return new_df.query('price >=1000 and price <2000')
    elif choice >=2000 and choice < 3000:
        return new_df.query('price >=2000 and price <3000')
    elif choice >=3000 and choice < 4000:
        return new_df.query('price >=3000 and price <4000')
    elif choice >=4000 and choice < 5000:
        return new_df.query('price >=4000 and price <5000')
    elif choice >=5000 and choice < 6000:
        return new_df.query('price >=5000 and price <6000')
    elif choice >=6000 and choice < 7000:
        return new_df.query('price >=6000 and price <7000')
    elif choice >=7000 and choice < 8000:
        return new_df.query('price >=7000 and price <8000')
    elif choice >=8000 and choice < 9000:
        return new_df.query('price >=8000 and price <9000')
    elif choice >=9000 and choice < 10000:
        return new_df.query('price >=9000 and price <10000')
    elif choice >=10000 and choice < 11000:
        return new_df.query('price >=10000 and price <11000')
    elif choice >=11000 and choice < 12000:
        return new_df.query('price >=11000 and price <12000')
    elif choice >=12000 and choice < 13000:
        return new_df.query('price >=12000 and price <13000')
    elif choice >=13000 and choice < 14000:
        return new_df.query('price >=13000 and price <14000')
    elif choice >=14000 and choice < 15000:
        return new_df.query('price >=14000 and price <15000')
    elif choice >=15000 and choice < 16000:
        return new_df.query('price >=15000 and price <16000')
    elif choice >=16000 and choice < 17000:
        return new_df.query('price >=16000 and price <17000')
    elif choice >=18000 and choice < 19000:
        return new_df.query('price >=18000 and price <19000')
    elif choice >=19000 and choice < 20000:
        return new_df.query('price >=19000 and price <20000')
    else:
        return new_df.query('price >20000')

def category(car_category, data_list):
    if car_category == "coupe":
        return data_list.query('category =="coupe"')
    elif car_category == "sedan":
        return data_list.query('category == "sedan"')
    elif car_category =="microbus":
        return data_list.query('category == "microbus"')
    elif car_category == "cabriolet":
        return data_list.query('category == "cabriolet"')
    elif car_category == "wagon":
        return data_list.query('category == "wagon"')
    elif car_category == "hatchback":
        return data_list.query('category == "hatchback"')
    elif car_category == "jeep":
        return data_list.query('category == "jeep"')
    elif car_category == "minivan":
        return data_list.query('category == "minivan"')
    elif car_category == "pickup":
        return data_list.query('category == "pickup"')
    elif car_category == 'universal':
        return data_list.query('category == "universal"')
    elif car_category == 'limousine':
        return data_list.query('category == "limousine"')

def get_fueltype(fuel, data_list):
    if fuel == "petrol":
        return data_list.query('fuel_type == "petrol"')
    elif fuel == "diesel":
        return data_list.query('fuel_type == "diesel"')
    elif fuel == "hybrid":
        return data_list.query('fuel_type == "hybrid"')
    elif fuel == "cng":
        return data_list.query('fuel_type == "cng"')
    elif fuel == "plug-in":
        return data_list.query('fuel_type == "plug-in"')
    elif fuel == "lpg":
        return data_list.query('fuel_type == "lpg"')
    elif fuel == "hydrogen":
        return data_list.query('fuel_type == "hydrogen"')

def get_geartype(gear, data_list):
    if gear == "automatic":
        return data_list.query('gear_box_type == "automatic"')
    elif gear == "manual":
        return data_list.query('gear_box_type == "manual"')
    elif gear == "tiptronic":
        return data_list.query('gear_box_type == "tiptronic"')
    elif gear == "variator":
        return data_list.query('gear_box_type == "variator"')

def year(value, data_list):
    return data_list.query("prod_year == @value")

def return_list(data):
    print("List of Car(s) with your selected Budget and features: ")
    for i in range(len(data)):
        print(str(i+1) +". "+str(data['manufacturer'].iloc[i])+" "+str(data['model'].iloc[i])+" - Cylinders: "+str(data['cylinders'].iloc[i])+" - Year:"+str(data['prod_year'].iloc[i]) +" - CAD: $"+str(data['price'].iloc[i]))

def rules_engine():
    budget = get_budget()
    df_price = price_range(int(budget))
    if(len(df_price) <= 3):
        return_list(df_price)
        return
    new_df = df_price.copy()

    year_num = get_year(new_df['prod_year'].unique())
    df_year = year(int(year_num), new_df)
    if(len(df_year) <= 3):
        return_list(df_year)
        return
    new_df = df_year.copy()

    car_category = get_car_category_input(new_df['category'].unique())
    df_car_category = category(car_category.lower(), new_df)
    if(len(df_car_category) <= 3):
        return_list(df_car_category)
        return
    new_df = df_car_category.copy()

    fuel_type = get_fueltype_input(new_df['fuel_type'].unique())
    df_fuel_type = get_fueltype(fuel_type.lower(), new_df)
    if(len(df_fuel_type) <= 3):
        return_list(df_fuel_type)
        return
    new_df = df_fuel_type.copy()

    type_of_gear = get_geartype_input(new_df['gear_box_type'].unique())
    df_type_of_gear = get_geartype(type_of_gear.lower(), new_df)
    if(len(df_type_of_gear) <= 3):
        return_list(df_type_of_gear)
        return
    new_df = df_type_of_gear.copy()

    color = get_color_input(new_df['color'].unique())
    df_color = get_color(color.lower(), new_df)
    if(len(df_color) <= 3):
        return_list(df_color)
        return
    new_df = df_color.copy()

    return return_list(new_df)

rules_engine()