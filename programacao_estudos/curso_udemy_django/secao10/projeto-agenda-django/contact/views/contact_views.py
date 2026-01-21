from django.shortcuts import render, get_object_or_404


from contact.models import Contact

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10] 

    context = {
        'contacts': contacts, 
        'site_title': 'Contatos - '
    }
    
    return render(
        request,
        'contact/index.html', context
    )
    
    
def contact(request, contact_id):
    single_contacts = get_object_or_404(
        Contact.objects.filter(pk=contact_id, show=True)
    )
    
    site_title = f'{single_contacts.first_name} {single_contacts.last_name} - '
    
    context = {
        'contact': single_contacts, 
        'site_title': site_title
    }
    
    return render(
        request,
        'contact/contact.html', context
    )