from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail  # Importa la función para enviar correos

def index(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Construye el contenido del correo
        subject = f"Nuevo mensaje de {name}"
        message_body = f"Nombre: {name}\nCorreo: {email}\n\nMensaje:\n{message}"

        # Envía el correo
        send_mail(
            subject,  # Asunto del correo
            message_body,  # Cuerpo del mensaje
            'tu_correo@hotmail.com',  # Desde (tu correo)
            ['coria.gabriel@hotmail.com'],  # A (tu correo de destino)
            fail_silently=False,
        )

        # Muestra un mensaje de éxito
        return HttpResponse("Gracias por tu mensaje, " + name + "! Tu correo ha sido enviado.")

    return render(request, 'index.html')