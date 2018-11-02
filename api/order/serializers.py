from rest_framework import serializers
from produk.models import Order, Order_Detail
from api.produk.serializers import ProdukSerializer


class OrderGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id','no_hape', 'alamat', 'ongkosKirim','status',) 

class OrderPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id',)

    def create(self, validated_data):
        # digunakan agar ketika order, otomatis mengisi user berdasarkan
        # siapa yang sedang login
        user = self.context['request'].user 
        validated_data['user'] = user
        ordernyaUser = user.user_order.filter(status='cart').first()

        if ordernyaUser:
            return ordernyaUser
        return super(OrderSerializer, self).create(validated_data)


class OrderBarangGETSerializer(serializers.ModelSerializer):
    # ProdukSerializer() ini digunakan untuk menampilkan detail data produk
    produk = ProdukSerializer()

    class Meta:
        model = Order_Detail
        fields = ('id', 'produk', 'harga', 'qty','subtotal')


class OrderBarangPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_Detail
        fields = ('id', 'produk', 'qty')

    def create(self, validated_data):
        # digunakan agar ketika order kosong, otomatis menggunakan
        # order id yang sedang dipakai
        order_id = self.context['order_id']
        order = Order.objects.get(id=order_id)
        semuaOrderBarang = order.barang_order.all()

        produk = validated_data['produk']
        validated_data['order'] = order
        validated_data['harga'] = produk.harga
        # print(validated_data['harga'])

        # kode untuk ngecek apakah produk sudah ada di orderan apa belum
        # kalau sudah ada, maka tinggal tambahkan jumlah/qty nya
        for sob in semuaOrderBarang:
            if produk.id == sob.produk.id:
                sob.qty += validated_data['qty']
                sob.save()
                return sob
                # harus di return dalam bentuk instance nya

        return super(OrderBarangPOSTSerializer, self).create(validated_data)
