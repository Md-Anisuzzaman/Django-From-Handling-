from django.urls import path
from .views import work_app, about, contact, form,validationForm

urlpatterns = [
    path("home/", work_app, name="homepage"),
    path("about/", about, name="aboutpage"),
    path("contact/", contact, name="contactpage"),
    path("form/", form, name="formpage"),
    path("valid/", validationForm, name="validationpage"),
]
