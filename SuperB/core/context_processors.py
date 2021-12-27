from core.forms import SubscriberForm


def get_subscriber_form(request):
    if request.method == "POST" and 'subscriber' in request.POST:
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SubscriberForm()

    return {'subscriber_form': form}
