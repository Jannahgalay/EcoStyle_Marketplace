from models.seller import Seller

class SellerService:
    def __init__(self):
        self.sellers = []

    def add_seller(self, seller):
        self.sellers.append(seller)

    def get_all_sellers(self):
        return self.sellers
