import flet
from flet import *
from controls import add_control_reference
from btn import return_form_button


class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        add_control_reference("AppForm",self)

    def app_form_input_field(self,name:str,expand:int):
        return Container(
            expand=expand,
            height=45,
            bgcolor='#ebebeb',
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=10,
                        color='black',
                        weight='bold',
                    ),
                    TextField(
                        border_color='transparent',
                        height=20,
                        text_size=13,
                        content_padding=0,
                        cursor_color='black',
                        cursor_width=1,
                        cursor_height=18,
                        color='black',
                    ),
                    
                ]
            )
        )
    
    
    def build(self):
        self.app_form_input_instance(),
        def handle_loaded_file( e:flet.FilePickerResultEvent):
            print(e.files)
        file_picker = flet.FilePicker(on_result=handle_loaded_file)
        
        
        return Container(
            expand=True,
            height=300,
            bgcolor='white10',
            border=border.all(1,'#ebebeb'),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            self.app_form_input_field('Enter Name FirstName-Surname',True),
                        ],
                        
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field('Enter MIS No.',1),
                            # self.app_form_input_field('Enter Score',1),
                            # self.app_form_input_field('Placed At',1),
                        ]
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field('Enter Score',1),
                        ]
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field('Placed At',1),
                        ]
                    ),
                    Divider(
                        height=1,
                        color='transparent',
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_form_button()
                        ]
                    ),
                    # Row(
                    #     alignment=MainAxisAlignment.START,
                    #     controls=[
                    #         return_form_button()
                    #     ]
                    # ),
                ],
            ),
        )