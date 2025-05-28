import urllib.request, json
import sys

def display_brewery_details(brewery):

    print("\n--- Brewery Details ---")
    print("Name: " + str(brewery.get('name', 'N/A')))
    print("Type: " + str(brewery.get('brewery_type', 'N/A')))

    address = str(brewery.get('address_1', 'N/A'))
    if brewery.get('address_2'):
        address += ", " + str(brewery.get('address_2'))
    if brewery.get('address_3'):
        address += ", " + str(brewery.get('address_3'))
    print("Address: " + address)

    print("City: " + str(brewery.get('city', 'N/A')))
    print("State: " + str(brewery.get('state', 'N/A')))
    print("Postal Code: " + str(brewery.get('postal_code', 'N/A')))
    print("Country: " + str(brewery.get('country', 'N/A')))
    print("Phone: " + str(brewery.get('phone', 'N/A')))
    print("Website: " + str(brewery.get('website_url', 'N/A')))
    print("Updated At: " + str(brewery.get('updated_at', 'N/A')))
    print("Latitude: " + str(brewery.get('latitude', 'N/A')))
    print("Longitude: " + str(brewery.get('longitude', 'N/A')))
    print("-" * 30)

def show_breweries(country_name):

    url_breweries = "https://api.openbrewerydb.org/v1/breweries?by_country=" + str(country_name.replace(' ', '%20')) + "&per_page=25"

    breweries_list = []

    request = urllib.request.Request(url_breweries, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'})

    with urllib.request.urlopen(request) as data:
        parsed = json.load(data)

    if parsed:
        print("\n--- Breweries in " + str(country_name) + " ---")
        for i, brewery in enumerate(parsed):
            breweries_list.append(brewery)
            name = brewery.get('name', 'Name not available.')
            city = brewery.get('city', 'City not available.')
            state = brewery.get('state', 'State not available.')
            print(str(i + 1) + ". " + str(name) + " (Ciudad: " + str(city) + ", Estado: " + str(state) + ")")

        selection_menu = -1
        while selection_menu != 0:
            print("\n--- Select Brewery Options ---")
            print("Enter the number of the brewery to see more details.")
            print("0. Go Back.")

            selection_menu = input("Choose an option (0-" + str(len(breweries_list)) + "): ")

            if selection_menu.isdigit():
                selection_menu = int(selection_menu)
                if selection_menu == 0:
                    break
                elif selection_menu >= 1 and selection_menu <= len(breweries_list):
                    selected_index = selection_menu - 1
                    display_brewery_details(breweries_list[selected_index])
                    detail_option = -1
                    while detail_option != 0:
                        print("\n--- Details Options ---")
                        print("1. Continue browse breweries in this country.")
                        print("0. Go back.")

                        detail_option = input("Choose an option (0-1): ")

                        if detail_option.isdigit():
                            detail_option = int(detail_option)
                            if detail_option == 0:
                                selection_menu = 0
                                break
                            elif detail_option == 1:
                                break
                            else:
                                print("Invalid option. Please enter a 0 or 1.")
                        else:
                            print("Error: You must enter a valid number.") 
                else:
                    print("Invalid number. Please enter a number between 0 and " + str(len(breweries_list)) + ".")
            else:
                print("Error: You must enter a valid number.")

    else:
        print("No breweries were found for " + str(country_name) + ".")

def show_breweries_menu():

    option_menu = -1
    while option_menu != 0:
        print("""
        ______                                     ___               
        | ___ \                                   / _ \              
        | |_/ /_ __ _____      _____ _ __ _   _  / /_\ \_ __  _ __   
        | ___ \ '__/ _ \ \ /\ / / _ \ '__| | | | |  _  | '_ \| '_ \  
        | |_/ / | |  __/\ V  V /  __/ |  | |_| | | | | | |_) | |_) | 
        \____/|_|  \___| \_/\_/ \___|_|   \__, | \_| |_/ .__/| .__/  
                                           __/ |       | |   | |     
                                          |___/        |_|   |_|
                            by Hector Puch       
        """)
        print("--- Menu ---")
        print("1. Austria.")
        print("2. England.")
        print("3. France.")
        print("4. Isle of Man.")
        print("5. Ireland.")
        print("6. Poland.")
        print("7. Portugal.")
        print("8. Scotland.")
        print("9. Singapore.")
        print("10. South Korea.")
        print("11. United States.")
        print("0. Exit.")

        option_menu = input("Choose an option (0-11): ")

        if option_menu.isdigit():
            option_menu = int(option_menu)
            match option_menu:
                case 0:
                    print("Goodbye.")
                case 1:
                    show_breweries("Austria")
                case 2:
                    show_breweries("England")
                case 3:
                    show_breweries("France")
                case 4:
                    show_breweries("Isle of Man")
                case 5:
                    show_breweries("Ireland")
                case 6:
                    show_breweries("Poland")
                case 7:
                    show_breweries("Portugal")
                case 8:
                    show_breweries("Scotland")
                case 9:
                    show_breweries("Singapore")
                case 10:
                    show_breweries("South Korea")
                case 11:
                    show_breweries("United States")
                case _:
                    print("Please, enter a number between 0 and 11.")
        else:
            print("Error: You must enter a valid number.")

show_breweries_menu()