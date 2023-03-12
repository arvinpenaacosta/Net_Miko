import flet as ft
from entryField import EntryField

#===========================================================
# then use the control
def main(page):

    page.fonts = {
        "Prototype": "Prototype.ttf",
        "Candybean": "CandyBeans.otf",
    }

    #Page initialization

    page.window_height = 700
    page.window_width = 500
    page.title = "MyVersion"
    page.scroll = "auto"

    #page.on_connect = initialize_db()    
    
    #          EntryField("tname1", "tname2", "tname3", "pass", "tnamec1", "tnamec2", "cbxname1" , "cbxname2", "Submit")
    net_miko = EntryField("tname1", "tname2", "tname3", "pass", "tnamec1", "tnamec2", "VLAN" , "Voice", "Submit")

    page.add(
        ft.Column(
            expand=True,
            controls=[

                net_miko,
                ft.Divider(height=5, color="RED"),
 
                ft.Column(
                    #scroll ="hidden",
                    scroll ="auto",
                    expand=True,
                    controls=[
                        
                    ]



                )
            ],
        )
    )


ft.app(target=main, port=8886, assets_dir="assets")

