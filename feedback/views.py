from rest_framework.generics import CreateAPIView
from rest_framework import permissions, parsers


from .serializers import FeedbackSerializer
from .models import Feedback


class FeedbackView(CreateAPIView):
    queryset = Feedback.objects.all()
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = FeedbackSerializer
    throttle_scope = 'low_request'
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


