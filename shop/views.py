from django.views import generic

from conftest import product
from shop.models import Product, Category


class HomeView(generic.ListView):
    model = Product
    template_name = 'home.html'
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['selected_categories'] = self.request.GET.getlist('filter')
        context['selected_sort'] = self.request.GET.get('sort', 'new')
        query = self.request.GET.copy()
        query.pop('page', None)
        context['query_string'] = query.urlencode()
        return context

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.GET.get('filter'):
            filter_param = self.request.GET.getlist('filter')
            print(filter_param)
            queryset = queryset.filter(category__name__in=filter_param)
        if self.request.GET.get('search'):
            search_param = self.request.GET.get('search')
            queryset = queryset.filter(name__icontains=search_param)
        if self.request.GET.get('sort'):
            sort_param = self.request.GET.get('sort', 'new')
            if sort_param == 'new':
                queryset = queryset.order_by('created_at')
            elif sort_param == 'price_asc':
                queryset = queryset.order_by('price')
            elif sort_param == 'price_desc':
                queryset = queryset.order_by('-price')
            elif sort_param == 'rating':
                queryset = queryset.order_by('created_at')

        return queryset

# Products



class ProductDetailView(generic.DetailView):
    model = Product
    slug_field = "slug"
    slug_url_kwarg = "product_slug"
    template_name = "products/product-detail.html"



class ProductReviewAddView(generic.TemplateView):
    pass

class ProductReviewListView(generic.TemplateView):
    pass


# Orders
class OrderListView(generic.TemplateView):
    pass

class OrderAddView(generic.TemplateView):
    pass

class OrderRemoveView(generic.TemplateView):
    pass

class OrderUpdateView(generic.TemplateView):
    pass

class OrderCheckoutView(generic.TemplateView):
    pass

class OrderDetailView(generic.TemplateView):
    pass

class OrderHistoryView(generic.TemplateView):
    pass


# Payments
class PaymentProcessView(generic.TemplateView):
    pass

class PaymentConfirmView(generic.TemplateView):
    pass

class PaymentCancelView(generic.TemplateView):
    pass


# Reviews
class ReviewAddView(generic.TemplateView):
    pass

class ReviewUpdateView(generic.TemplateView):
    pass

class ReviewDeleteView(generic.TemplateView):
    pass
