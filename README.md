# 📧 Envío automático de correos con Lotus Notes usando Python

Este script permite enviar correos electrónicos automáticamente a través de **Lotus Notes** utilizando la librería `win32com.client` de Windows. Está pensado para entornos corporativos que siguen utilizando IBM Notes/Domino como gestor de correo.

## 🚀 Requisitos

- Windows OS
- Lotus Notes instalado y configurado
- Python 3.x
- `pywin32` instalado

Puedes instalar `pywin32` con:

```bash
pip install pywin32
```

## 🛠️ Configuración
Edita los siguientes valores en el script para adaptarlo a tu entorno:

```python
notes.Initialize("TU_CONTRASEÑA")  # Contraseña de tu sesión de Lotus Notes
notes.GetDatabase("", "mail\\TU_USUARIO.nsf")  # Ruta a tu archivo NSF
mail_doc.ReplaceItemValue("SendTo", "DESTINATARIO@tuempresa.com")
```
## 📩 Ejemplo de uso
```bash
python send_lotus_email.py
```
El correo se enviará automáticamente sin necesidad de abrir el cliente Lotus Notes.

## ⚠️ Seguridad
Advertencia: Este script contiene contraseñas en texto plano. No lo subas a repositorios públicos sin eliminarlas o usar variables de entorno.

## 📄 Licencia
Este proyecto está licenciado bajo la MIT License.

## ✉️ Contacto
Marco Fernandez Callejon
marco.fernandezcallejon@hotmail.com
