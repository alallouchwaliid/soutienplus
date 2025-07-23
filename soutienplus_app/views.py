from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect 
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

def send_custom_email(text,name):
    subject = f'{name} want to subscribe'
    message = text
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['soutienplus.ma@gmail.com']
    send_mail(subject, message, from_email, recipient_list)



def home(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        niveau = request.POST.get('niveau')
        message = request.POST.get('message')
        # Send email
        
        messages.success(request, 'form submited succesfuly!')
        return render(request,'home.html')
    else:
        # Show your form template
        return render(request, 'home.html')







def send_custom_email(nom, email, telephone, niveau, message):
    subject = f"Nouvelle demande d'inscription de {nom}"
    from_email = settings.EMAIL_HOST_USER
    to = ['soutienplus.ma@gmail.com']

    # Version texte brut
    text_content = f"""
    Une nouvelle personne souhaite s'inscrire !

    Nom complet : {nom}
    Email : {email}
    Téléphone : {telephone}
    Niveau scolaire : {niveau}

    Message :
    {message}

    ---
    Ce message a été généré automatiquement par le site.
    """

    # Version HTML
    html_content = f"""
    <html>
<body style="margin: 0; padding: 0; background-color: #f0f2f5; font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background-color: #f0f2f5; padding: 40px 0;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="background-color: #ffffff; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); overflow: hidden;">
          <tr>
            <td style="background-color: #2d89ef; padding: 30px; color: #ffffff;">
              <h1 style="margin: 0; font-size: 24px;">📨 Nouvelle Demande d'Inscription</h1>
              <p style="margin-top: 5px; font-size: 14px;">Vous avez reçu une nouvelle demande via le site.</p>
            </td>
          </tr>
          <tr>
            <td style="padding: 30px;">
              <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td style="padding: 10px 0;"><strong>🔹 Nom complet :</strong></td>
                  <td style="padding: 10px 0;">{nom}</td>
                </tr>
                <tr>
                  <td style="padding: 10px 0;"><strong>📧 Email :</strong></td>
                  <td style="padding: 10px 0;">{email}</td>
                </tr>
                <tr>
                  <td style="padding: 10px 0;"><strong>📞 Téléphone :</strong></td>
                  <td style="padding: 10px 0;">{telephone}</td>
                </tr>
                <tr>
                  <td style="padding: 10px 0;"><strong>🎓 Niveau scolaire :</strong></td>
                  <td style="padding: 10px 0;">{niveau}</td>
                </tr>
              </table>

              <hr style="border: none; border-top: 1px solid #e0e0e0; margin: 30px 0;">

              <p style="margin: 0 0 10px 0;"><strong>📝 Message :</strong></p>
              <div style="background-color: #f9fafb; border-left: 5px solid #2d89ef; padding: 15px; font-style: italic; color: #333;">
                {message}
              </div>
            </td>
          </tr>
          <tr>
            <td style="background-color: #f7f7f7; text-align: center; padding: 20px; font-size: 12px; color: #777;">
              Ce message a été généré automatiquement par le site. <br>
              © 2025 Soutien+
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
    </html>
    """

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
