import win32com.client

def send_email():
    try:
        notes = win32com.client.Dispatch("Lotus.NotesSession")
        notes.Initialize("Contraseña")  #contraseña

        mail_db = notes.GetDatabase("", "mail\\archivo.nsf")  # Usamos archivo.nsf

        # Abrir base de datos si no está abierta
        if not mail_db.IsOpen:
            mail_db.Open()

        # Crear un nuevo documento de correo
        mail_doc = mail_db.CreateDocument()

        # Configurar los detalles del correo
        mail_doc.ReplaceItemValue("Subject", "Este es un correo de prueba automatizado") 
        mail_doc.ReplaceItemValue("SendTo", "prueba@correo.com")
        mail_doc.ReplaceItemValue("Body", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed justo risus, tempor at eros nec, hendrerit viverra dolor. Integer condimentum ipsum eget dignissim rutrum. Vivamus vitae sagittis nisl. Integer ut consectetur nisi. Morbi eget felis sed nulla vulputate ullamcorper eget in diam. Donec placerat, erat ultricies rhoncus rhoncus, lorem libero rutrum arcu, id tincidunt ex velit eget diam. Quisque eget nunc ut dui placerat laoreet in non ligula. Nunc sed interdum nunc. Ut porta, magna vitae rhoncus vestibulum, justo nibh tincidunt nisi, non suscipit ex sapien dapibus nibh. Aliquam ultrices consequat arcu, at rutrum massa sodales nec. Nunc sit amet lacus lectus.")  # Cuerpo del correo

        # Enviar el correo
        mail_doc.Send(False)  # No pedirá confirmación antes de enviar
        print("Correo enviado correctamente.")
    
    except Exception as e:
        print(f"Error: {e}")

send_email()
