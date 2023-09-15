from website.models import Reservation,OpeningHours,Info

def base_info(request):
    reservation = Reservation.objects.first()
    opening_hours = OpeningHours.objects.first()
    info = Info.objects.first()
    return {
        'reservation': reservation,
        'opening_hours': opening_hours,
        'info':info
    }
    