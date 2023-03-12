import flet as ft
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


class EntryField(ft.UserControl):
    def __init__(self, tname1, tname2, tname3, pname, tnamec1, tnamec2, cbxname1 , cbxname2, bname):
        super().__init__()
        self.tname1 = tname1
        self.tname2 = tname2
        self.tname3 = tname3
        self.tnamec1 = tnamec1
        self.tnamec2 = tnamec2
        self.cbxname1 = cbxname1
        self.cbxname2 = cbxname2
        self.bname = bname

        self.pname = pname





    def build(self):



        def change_click1(e):
            tfc1.disabled = not cb1.value;  
            tfc1.value = "" if cb1.value != True else tfc1.focus()
            self.update() 

        def change_click2(e):
            tfc2.disabled = not cb2.value;  
            tfc2.value = "" if cb2.value != True else tfc2.focus()
            self.update() 



        def get_input_data(e):
            data = {
                'data1' : tf1.value,
                'data2' : tf2.value,
                'data3' : tf3.value,
                'data4' : ptf.value,
                'data5' : tfc1.value,
                'data6' : cb1.value,
                'data7' : tfc2.value,
                'data8' : cb2.value,
            }


            print(data['data1'])
            print(data['data2'])
            print(data['data3'])
            print(data['data4'])
            print(data['data5'])
            print(data['data6'])
            print(data['data7'])
            print(data['data8'])

            #send_show_command(tf1.value, tf3.value, ptf.value)


            #show_banner




        tf1 = ft.TextField(label= self.tname1)
        tf2 = ft.TextField(label= self.tname2)
        tf3 = ft.TextField(label= self.tname3)
        ptf = ft.TextField(label= self.pname, password=True, can_reveal_password=True)
        
        tfc1 = ft.TextField(label= self.tnamec1,width=100, height=44, disabled = True)
        cb1 = ft.Checkbox(label = self.cbxname1, on_change=change_click1)

        tfc2 = ft.TextField(label= self.tnamec2,width=100, height=44, disabled = True)
        cb2 = ft.Checkbox(label = self.cbxname2, on_change=change_click2)
        
        
        btn= ft.ElevatedButton(text=self.bname, on_click=get_input_data)
        btn2= ft.ElevatedButton(text=self.bname, on_click=show_banner)




        return ft.Column(
                [
                    tf1, 
                    tf2, 
                    tf3, 
                    ptf, 
                    ft.Row(
                        controls=[
                            cb1, 
                            tfc1, 
                        ]
                    ),
                    ft.Row(
                        controls=[
                            cb2, 
                            tfc2, 
                        ]
                    ),
                    
                    btn,btn2
                ]
            )


#===========================================================
# then use the control
def main(page: ft.Page):

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


    def yes_close(e):
        page.window_destroy()

    def close_banner(e):
        page.banner.open = False
        tb1.value = ""
        tb2.value = ""
        tb3.value = ""
        page.update()
    
    page.banner = ft.Banner(
        bgcolor=ft.colors.RED_500,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        actions=[
            ft.ElevatedButton(text="Retry New Value", on_click=close_banner),
            ft.ElevatedButton(text="Cancel", on_click=yes_close),
        ],
    )
          
    def show_banner(err):
        page.banner.content = ft.Text(f"{err}")
        page.banner.open = True
        page.update() 

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

