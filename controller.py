import view
import add_to_db
import extract




def phone_book():
    menu = 0
    while menu != 4:
        menu = view.main_menu()

        if menu == 1:
            phone_data = view.write_data()
            add_to_db.add_to_txt(phone_data)
            add_to_db.add_to_csv(phone_data)
        elif menu == 2:
            extract.full_output()
        elif menu == 3:
            lastname = view.search_data()
            extract.find_data(lastname)



