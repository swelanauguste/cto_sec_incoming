from django.db.models import Q
from django.shortcuts import get_object_or_404, render, reverse
from django.utils import timezone
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models


class IncomingCreateView(CreateView):
    model = models.Incoming
    form_class = forms.IncomingForm


class IncomingUpdateView(UpdateView):
    model = models.Incoming
    form_class = forms.IncomingForm


class IncomingListView(ListView):
    model = models.Incoming
    paginate_by = 25

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get("q", "")
        date_from = self.request.GET.get("date_from", "")
        date_to = self.request.GET.get("date_to", "")

        if search_query:
            queryset = queryset.filter(
                Q(ref__icontains=search_query)
                | Q(received_from__icontains=search_query)
                | Q(contact__icontains=search_query)
                | Q(phone__icontains=search_query)
                | Q(email__icontains=search_query)
                | Q(subject__icontains=search_query)
                | Q(note__icontains=search_query)
            )

        # Filter based on date range
        if date_from:
            queryset = queryset.filter(received_on__gte=date_from)
        if date_to:
            queryset = queryset.filter(received_on__lte=date_to)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_query"] = self.request.GET.get("search", "")
        context["date_from"] = self.request.GET.get("date_from", "")
        context["date_to"] = self.request.GET.get("date_to", "")
        return context


class IncomingDetailView(DetailView):
    model = models.Incoming


class ChangeStatusCreateView(CreateView):
    model = models.ChangeStatus
    form_class = forms.ChangeStatusForm

    def get_initial(self):
        # Retrieve the `Incoming` instance based on the slug
        incoming = get_object_or_404(models.Incoming, slug=self.kwargs.get("slug"))

        # Set initial values
        initial = super().get_initial()
        initial.update(
            {
                "status": "received",
                "date": timezone.now(),
                "incoming": incoming,
            }
        )
        return initial

    def form_valid(self, form):
        # Assign the `incoming` field before saving
        form.instance.incoming = get_object_or_404(
            models.Incoming, slug=self.kwargs.get("slug")
        )
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the Incoming detail view after a successful form submission
        return reverse("detail", kwargs={"slug": self.kwargs.get("slug")})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the Incoming instance to the context
        context["incoming"] = get_object_or_404(
            models.Incoming, slug=self.kwargs.get("slug")
        )
        return context
