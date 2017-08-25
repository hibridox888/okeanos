from django.views.generic.dates import (
    ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView,
    YearArchiveView,
)

from .models import Post


class BlogViewMixin(object):
    date_field = 'pub_date'
    paginate_by = 10

    def get_allow_future(self):
        return self.request.user.is_staff

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        else:
            return Post.objects.published()


class BlogArchiveIndexView(BlogViewMixin, ArchiveIndexView):
    pass


class BlogYearArchiveView(BlogViewMixin, YearArchiveView):
    make_object_list = True


class BlogMonthArchiveView(BlogViewMixin, MonthArchiveView):
    pass


class BlogDayArchiveView(BlogViewMixin, DayArchiveView):
    pass


class BlogDateDetailView(BlogViewMixin, DateDetailView):
    pass
