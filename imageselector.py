import flet as ft

def main(page:ft.Page):

    def handle_loaded_file(e:ft.FilePickerResultEvent):
        print(e.files)
    file_picker = ft.FilePicker(on_result=handle_loaded_file)
    page.overlay.append(file_picker)

    page.add(ft.Text("Read Image"))
    page.add(ft.ElevatedButton(text="Image",on_click=lambda _:file_picker.pick_files(allow_multiple=False,allowed_extensions=['jpg','png','jpeg'])))


ft.app(target=main)
