# from rest_framework.generics import CreateAPIView
# from rest_framework import permissions, parsers
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
# from django.views.generic.edit import CreateView
# from .serializers import FeedbackSerializer
from .forms import FeedbackForm
# from .models import Feedback


@login_required
@permission_required('feedback.add_choice', raise_exception=True)
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_read = False
            form.user = request.user
            form.save()
            return render(request, 'form/ok.html')
        return render(request, 'form/feedback_form.html', {'form': form})
    form = FeedbackForm()
    return render(request, 'form/feedback_form.html', {'form': form})



# class FeedbackView(CreateView):
    # queryset = Feedback.objects.all()
    # parser_classes = (parsers.MultiPartParser,)
    # serializer_class = FeedbackSerializer
    # throttle_scope = 'low_request'
    # permission_classes = [permissions.IsAuthenticated]

    # def perform_create(self, serializer):
        # serializer.save(user=self.request.user)


