class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})

    def add(self, product_id, quantity=1):
        if str(product_id) not in self.cart:
            self.cart[str(product_id)] = quantity
        else:
            self.cart[str(product_id)] += quantity
        self.save()

    def remove(self, product_id):
        del self.cart[str(product_id)]
        self.save()

    def save(self):
        self.session['cart'] = self.cart