from django import forms
from .models import Pemesanan, CheckOut

class PemesananForm(forms.ModelForm):
    class Meta:
        model = Pemesanan
        fields = (
        	'file',
        	'print_id',
        	'waktu_pengambilan',
        	'pengambilan_id',
            'copy',
        	# 'harga_bayar',
        	'status_id',
        	)

class PemesananUpdateForm(forms.ModelForm):
    class Meta:
        model = Pemesanan
        fields = (
            'bukti',
            )
    


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CheckOut
        fields = (
            # 'pemesanan_id',
            'bukti',
            )
    