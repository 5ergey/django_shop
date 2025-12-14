from django.urls import path
from . import views as shop_views


urlpatterns = [
    # Home Page
    path("home", shop_views.HomeView.as_view(), name="home"),

    # Products,
    path("shop_products", shop_views.ProductListView.as_view(), name="shop_products"),
    path("shop_products_search", shop_views.ProductSearchView.as_view(), name="shop_products_search"),
    path("shop_product_detail", shop_views.ProductDetailView.as_view(), name="shop_product_detail"),
    path("shop_product_review_add", shop_views.ProductReviewAddView.as_view(), name="shop_product_review_add"),
    path("shop_product_reviews", shop_views.ProductReviewListView.as_view(), name="shop_product_reviews"),

    # Orders
    path("shop_order", shop_views.OrderListView.as_view(), name="shop_order"),
    path("shop_order_add", shop_views.OrderAddView.as_view(),name="shop_order_add"),
    path("shop_order_remove", shop_views.OrderRemoveView.as_view(), name="shop_order_remove"),
    path("shop_order_update", shop_views.OrderUpdateView.as_view(), name="shop_order_update"),
    path("shop_order_checkout", shop_views.OrderCheckoutView.as_view(),name="shop_order_checkout"),
    path("shop_order_detail", shop_views.OrderDetailView.as_view(),name="shop_order_detail"),
    path("shop_orders", shop_views.OrderHistoryView.as_view(),name="shop_orders"),

    # Payments
    path("shop_payment_process", shop_views.PaymentProcessView.as_view(), name="shop_payment_process"),
    path("shop_payment_confirm", shop_views.PaymentConfirmView.as_view(), name="shop_payment_confirm"),
    path("shop_payment_cancel", shop_views.PaymentCancelView.as_view(), name="shop_payment_cancel"),

    # Reviews
    path("shop_review_add", shop_views.ReviewAddView.as_view(), name="shop_review_add"),
    path("shop_review_update", shop_views.ReviewUpdateView.as_view(), name="shop_review_update"),
    path("shop_review_delete", shop_views.ReviewDeleteView.as_view(), name="shop_review_delete"),
]