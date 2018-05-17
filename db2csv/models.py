# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alis(models.Model):
    satisno = models.AutoField(db_column='SATISNO', primary_key=True)  # Field name made lowercase.
    toptancino = models.IntegerField(db_column='TOPTANCINO', blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    kdv = models.FloatField(db_column='KDV', blank=True, null=True)  # Field name made lowercase.
    iskonto = models.FloatField(db_column='ISKONTO', blank=True, null=True)  # Field name made lowercase.
    toplam = models.FloatField(db_column='TOPLAM', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tborcno = models.IntegerField(db_column='TBORCNO', blank=True, null=True)  # Field name made lowercase.
    kar = models.FloatField(db_column='KAR', blank=True, null=True)  # Field name made lowercase.
    depoadi = models.CharField(db_column='DEPOADI', max_length=35, blank=True, null=True)  # Field name made lowercase.
    tur = models.CharField(db_column='TUR', max_length=35, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    kartutar = models.FloatField(blank=True, null=True)
    uruncinsi = models.CharField(max_length=50, blank=True, null=True)
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=50, blank=True, null=True)
    toptanciad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'alis'


class Alistemp(models.Model):
    satisno = models.AutoField(db_column='SATISNO', primary_key=True)  # Field name made lowercase.
    toptancino = models.IntegerField(db_column='TOPTANCINO', blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    kdv = models.FloatField(db_column='KDV', blank=True, null=True)  # Field name made lowercase.
    iskonto = models.FloatField(db_column='ISKONTO', blank=True, null=True)  # Field name made lowercase.
    toplam = models.FloatField(db_column='TOPLAM', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tborcno = models.IntegerField(db_column='TBORCNO', blank=True, null=True)  # Field name made lowercase.
    kar = models.FloatField(db_column='KAR', blank=True, null=True)  # Field name made lowercase.
    depoadi = models.CharField(db_column='DEPOADI', max_length=35, blank=True, null=True)  # Field name made lowercase.
    tur = models.CharField(db_column='TUR', max_length=35, blank=True, null=True)  # Field name made lowercase.
    renk = models.CharField(db_column='RENK', max_length=20, blank=True, null=True)  # Field name made lowercase.
    uruncinsi = models.CharField(db_column='URUNCINSI', max_length=44, blank=True, null=True)  # Field name made lowercase.
    beden = models.CharField(db_column='BEDEN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    stokdurum = models.IntegerField(blank=True, null=True)
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'alistemp'


class Beden(models.Model):
    bedenno = models.AutoField(db_column='BEDENNO', primary_key=True)  # Field name made lowercase.
    beden = models.CharField(db_column='BEDEN', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'beden'


class Birim(models.Model):
    birimno = models.AutoField(db_column='BIRIMNO', primary_key=True)  # Field name made lowercase.
    birim = models.CharField(db_column='BIRIM', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'birim'


class Borc(models.Model):
    borcno = models.AutoField(db_column='BORCNO', primary_key=True)  # Field name made lowercase.
    musterino = models.IntegerField(db_column='MUSTERINO', blank=True, null=True)  # Field name made lowercase.
    adsoyad = models.CharField(db_column='ADSOYAD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    islemtur = models.CharField(db_column='ISLEMTUR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    aciklama = models.CharField(db_column='ACIKLAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    alinan = models.FloatField(db_column='ALINAN', blank=True, null=True)  # Field name made lowercase.
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    bakiye = models.FloatField(db_column='BAKIYE', blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    kasano = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'borc'


class Cekalis(models.Model):
    adsoyad = models.CharField(max_length=50, blank=True, null=True)
    bankaad = models.CharField(max_length=50, blank=True, null=True)
    serino = models.CharField(max_length=125, blank=True, null=True)
    odemetarihi = models.DateField(blank=True, null=True)
    tutar = models.FloatField(blank=True, null=True)
    ceknotu = models.CharField(max_length=250, blank=True, null=True)
    cekno = models.AutoField(primary_key=True)
    islemtur = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        
        db_table = 'cekalis'


class Cekislem(models.Model):
    adsoyad = models.CharField(max_length=50, blank=True, null=True)
    bankaad = models.CharField(max_length=50, blank=True, null=True)
    serino = models.CharField(max_length=125, blank=True, null=True)
    odemetarihi = models.DateField(blank=True, null=True)
    tutar = models.FloatField(blank=True, null=True)
    ceknotu = models.CharField(max_length=250, blank=True, null=True)
    cekno = models.AutoField(primary_key=True)
    islemtur = models.CharField(max_length=15, blank=True, null=True)
    tarih = models.DateField(blank=True, null=True)
    durum = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        
        db_table = 'cekislem'


class Cekmusteri(models.Model):
    adsoyad = models.CharField(max_length=50, blank=True, null=True)
    bankaad = models.CharField(max_length=50, blank=True, null=True)
    serino = models.CharField(max_length=125, blank=True, null=True)
    odemetarihi = models.DateField(blank=True, null=True)
    tutar = models.FloatField(blank=True, null=True)
    ceknotu = models.CharField(max_length=250, blank=True, null=True)
    cekno = models.AutoField(primary_key=True)
    islemtur = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        
        db_table = 'cekmusteri'


class Cins(models.Model):
    cinsno = models.AutoField(db_column='CINSNO', primary_key=True)  # Field name made lowercase.
    cins = models.CharField(db_column='CINS', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'cins'


class Depo(models.Model):
    depono = models.AutoField(db_column='DEPONO', primary_key=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    adres = models.CharField(db_column='ADRES', max_length=150, blank=True, null=True)  # Field name made lowercase.
    aciklama = models.CharField(db_column='ACIKLAMA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    stokmiktari = models.IntegerField(db_column='STOKMIKTARI', blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    depoad = models.CharField(db_column='DEPOAD', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'depo'


class Depoaktar(models.Model):
    depoid = models.AutoField(db_column='DEPOID', primary_key=True)  # Field name made lowercase.
    urunid = models.IntegerField(db_column='URUNID', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    depoad = models.CharField(db_column='DEPOAD', max_length=35, blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    uruncinsi = models.CharField(max_length=40, blank=True, null=True)
    depo2 = models.CharField(max_length=50, blank=True, null=True)
    mevcutadet = models.FloatField(blank=True, null=True)
    mevcutadet2 = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'depoaktar'


class Depomiktar(models.Model):
    girisid = models.AutoField(db_column='GIRISID', primary_key=True)
    depoid = models.IntegerField(db_column='DEPOID', blank=True, null=True)  # Field name made lowercase.
    urunid = models.IntegerField(db_column='URUNID', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    depoad = models.CharField(db_column='DEPOAD', max_length=35, blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    uruncinsi = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        
        db_table = 'depomiktar'


class Firma(models.Model):
    firmakodu = models.IntegerField(db_column='FIRMAKODU', primary_key=True)  # Field name made lowercase.
    firmadi = models.CharField(db_column='FIRMADI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='TELEFON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ceptelefon = models.CharField(db_column='CEPTELEFON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    adres = models.CharField(db_column='ADRES', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sehir = models.CharField(db_column='SEHIR', max_length=20, blank=True, null=True)  # Field name made lowercase.
    yetkili = models.CharField(db_column='YETKILI', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'firma'


class Gelir(models.Model):
    giderno = models.AutoField(primary_key=True)
    gideradi = models.CharField(max_length=50, blank=True, null=True)
    tutar = models.FloatField(blank=True, null=True)
    tarih = models.DateField()
    tur = models.CharField(max_length=20, blank=True, null=True)
    firmakodu = models.IntegerField()

    class Meta:
        
        db_table = 'gelir'


class GelirCopy(models.Model):
    giderno = models.AutoField(primary_key=True)
    gideradi = models.CharField(max_length=50, blank=True, null=True)
    tutar = models.FloatField(blank=True, null=True)
    tarih = models.DateField()
    tur = models.CharField(max_length=20, blank=True, null=True)
    firmakodu = models.IntegerField()

    class Meta:
        
        db_table = 'gelir_copy'


class Gelirler(models.Model):
    geliradi = models.CharField(max_length=50)
    firmakodu = models.IntegerField()

    class Meta:
        
        db_table = 'gelirler'


class Gider(models.Model):
    giderno = models.AutoField(primary_key=True)
    gideradi = models.CharField(max_length=50, blank=True, null=True)
    tutar = models.FloatField(blank=True, null=True)
    tarih = models.DateField()
    tur = models.CharField(max_length=20, blank=True, null=True)
    firmakodu = models.IntegerField()

    class Meta:
        
        db_table = 'gider'


class Giderler(models.Model):
    giderad = models.CharField(max_length=50)
    firmakodu = models.IntegerField()

    class Meta:
        
        db_table = 'giderler'


class Gurup(models.Model):
    gurupid = models.AutoField(db_column='GURUPID', primary_key=True)  # Field name made lowercase.
    gurup = models.CharField(db_column='GURUP', unique=True, max_length=40, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'gurup'


class Kasa(models.Model):
    kasano = models.AutoField(db_column='KASANO', primary_key=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    cekno = models.IntegerField(blank=True, null=True)
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    islemtur = models.CharField(db_column='ISLEMTUR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    giristur = models.CharField(db_column='GIRISTUR', max_length=15, blank=True, null=True)  # Field name made lowercase.
    aciklama = models.CharField(db_column='ACIKLAMA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    veresiyealis = models.FloatField(db_column='VERESIYEALIS', blank=True, null=True)  # Field name made lowercase.
    veresiyesat = models.FloatField(db_column='VERESIYESAT', blank=True, null=True)  # Field name made lowercase.
    kredikartli = models.FloatField(db_column='KREDIKARTLI', blank=True, null=True)  # Field name made lowercase.
    nakitsat = models.FloatField(db_column='NAKITSAT', blank=True, null=True)  # Field name made lowercase.
    nakital = models.FloatField(db_column='NAKITAL', blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    k_kartlialis = models.FloatField(blank=True, null=True)
    notlar = models.CharField(max_length=200, blank=True, null=True)
    indirim = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'kasa'


class Kullanici(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    kad = models.CharField(db_column='KAD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    pass_field = models.CharField(db_column='PASS', max_length=25, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    yetki = models.CharField(db_column='YETKI', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    yaciklama = models.CharField(db_column='Yaciklama', max_length=254, blank=True, null=True)  # Field name made lowercase.
    durum = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'kullanici'


class Marka(models.Model):
    markaad = models.CharField(max_length=50, blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'marka'


class Musteri(models.Model):
    musterino = models.AutoField(db_column='MUSTERINO', primary_key=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='TELEFON', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mevki = models.CharField(db_column='MEVKI', max_length=35, blank=True, null=True)  # Field name made lowercase.
    adres = models.CharField(db_column='ADRES', max_length=150, blank=True, null=True)  # Field name made lowercase.
    aciklama = models.CharField(db_column='ACIKLAMA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    alinan = models.FloatField(db_column='ALINAN', blank=True, null=True)  # Field name made lowercase.
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    bakiye = models.FloatField(db_column='BAKIYE', blank=True, null=True)  # Field name made lowercase.
    gorev = models.CharField(db_column='GOREV', max_length=25, blank=True, null=True)  # Field name made lowercase.
    gurup = models.CharField(db_column='GURUP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    sinir = models.IntegerField(db_column='SINIR', blank=True, null=True)  # Field name made lowercase.
    gurupid = models.IntegerField(db_column='GURUPID', blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(db_column='MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    adsoyad = models.CharField(db_column='ADSOYAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vergidairesi = models.CharField(max_length=75, blank=True, null=True)
    vergino = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        
        db_table = 'musteri'


class Notlar(models.Model):
    notid = models.AutoField(db_column='NOTID', primary_key=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    nots = models.CharField(db_column='NOTS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    durum = models.IntegerField(db_column='DURUM', blank=True, null=True)  # Field name made lowercase.
    baslik = models.CharField(db_column='BASLIK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'notlar'


class Plasiyer(models.Model):
    pno = models.IntegerField(blank=True, null=True)
    satisno = models.IntegerField(blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)
    plasiyer = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        
        db_table = 'plasiyer'


class Renk(models.Model):
    renkno = models.AutoField(db_column='RENKNO', primary_key=True)  # Field name made lowercase.
    renk = models.CharField(db_column='RENK', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'renk'


class Retiketi(models.Model):
    urunad = models.CharField(max_length=60)
    renk = models.CharField(max_length=50, blank=True, null=True)
    beden = models.CharField(max_length=50, blank=True, null=True)
    birim = models.CharField(max_length=50, blank=True, null=True)
    toplammiktar = models.IntegerField(blank=True, null=True)
    alisfiyati = models.FloatField(blank=True, null=True)
    satisfiyati = models.FloatField(blank=True, null=True)
    uruncinsi = models.CharField(max_length=50, blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)
    barkod = models.CharField(max_length=50)
    ikincisatfiyat = models.FloatField(blank=True, null=True)
    kkartli = models.FloatField(blank=True, null=True)
    iskonto = models.FloatField(blank=True, null=True)
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=22, blank=True, null=True)
    eskifiyat1 = models.FloatField(blank=True, null=True)
    eskifiyat2 = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'retiketi'


class Satis(models.Model):
    satisno = models.AutoField(db_column='SATISNO', primary_key=True)  # Field name made lowercase.
    musterino = models.IntegerField(db_column='MUSTERINO', blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    smsmusteri = models.CharField(max_length=75, blank=True, null=True)
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    fiyat2 = models.FloatField(db_column='FIYAT2', blank=True, null=True)  # Field name made lowercase.
    kdv = models.FloatField(db_column='KDV', blank=True, null=True)  # Field name made lowercase.
    iskonto = models.FloatField(db_column='ISKONTO', blank=True, null=True)  # Field name made lowercase.
    topind = models.FloatField(blank=True, null=True)
    toplam = models.FloatField(db_column='TOPLAM', blank=True, null=True)  # Field name made lowercase.
    alisfiyati = models.FloatField(db_column='ALISFIYATI', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    bakiyeno = models.IntegerField(db_column='BAKIYENO', blank=True, null=True)  # Field name made lowercase.
    kartutar = models.FloatField(db_column='KARTUTAR', blank=True, null=True)  # Field name made lowercase.
    depoadi = models.CharField(db_column='DEPOADI', max_length=35, blank=True, null=True)  # Field name made lowercase.
    tur = models.CharField(db_column='TUR', max_length=35, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    uruncinsi = models.CharField(db_column='URUNCINSI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    musteriad = models.CharField(max_length=40, blank=True, null=True)
    secim = models.CharField(max_length=2, blank=True, null=True)
    renk = models.CharField(max_length=50, blank=True, null=True)
    beden = models.CharField(max_length=50, blank=True, null=True)
    kkartli = models.FloatField(db_column='KKARTLI', blank=True, null=True)  # Field name made lowercase.
    plasiyer = models.CharField(max_length=50, blank=True, null=True)
    stok = models.FloatField(blank=True, null=True)
    sezon = models.CharField(max_length=50, blank=True, null=True)
    marka = models.CharField(max_length=50, blank=True, null=True)
    takipno = models.IntegerField(db_column='TakipNo', blank=True, null=True)  # Field name made lowercase.
    faturano = models.IntegerField(db_column='FaturaNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'satis'


class Satisbekle(models.Model):
    satisno = models.AutoField(db_column='SATISNO', primary_key=True)  # Field name made lowercase.
    musterino = models.IntegerField(db_column='MUSTERINO', blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    fiyat2 = models.FloatField(blank=True, null=True)
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    kdv = models.FloatField(db_column='KDV', blank=True, null=True)  # Field name made lowercase.
    indirim = models.FloatField(blank=True, null=True)
    iskonto = models.FloatField(db_column='ISKONTO', blank=True, null=True)  # Field name made lowercase.
    toplam = models.FloatField(db_column='TOPLAM', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=50, blank=True, null=True)
    bakiyeno = models.IntegerField(db_column='BAKIYENO', blank=True, null=True)  # Field name made lowercase.
    kartutari = models.FloatField(db_column='KARTUTARI', blank=True, null=True)  # Field name made lowercase.
    depoadi = models.CharField(db_column='DEPOADI', max_length=35, blank=True, null=True)  # Field name made lowercase.
    tur = models.CharField(db_column='TUR', max_length=35, blank=True, null=True)  # Field name made lowercase.
    renk = models.CharField(db_column='RENK', max_length=33, blank=True, null=True)  # Field name made lowercase.
    beden = models.CharField(db_column='BEDEN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uruncinsi = models.CharField(db_column='URUNCINSI', max_length=44, blank=True, null=True)  # Field name made lowercase.
    plasiyer = models.CharField(max_length=44, blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)
    kkartli = models.FloatField(db_column='KKARTLI', blank=True, null=True)  # Field name made lowercase.
    alisfiyati = models.FloatField(db_column='ALISFIYATI', blank=True, null=True)  # Field name made lowercase.
    smsmusteri = models.CharField(max_length=50, blank=True, null=True)
    stok = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'satisbekle'


class Satisbekle2(models.Model):
    satisno = models.AutoField(db_column='SATISNO', primary_key=True)  # Field name made lowercase.
    musterino = models.IntegerField(db_column='MUSTERINO', blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    fiyat2 = models.FloatField(blank=True, null=True)
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    indirim = models.FloatField(blank=True, null=True)
    kdv = models.FloatField(db_column='KDV', blank=True, null=True)  # Field name made lowercase.
    iskonto = models.FloatField(db_column='ISKONTO', blank=True, null=True)  # Field name made lowercase.
    toplam = models.FloatField(db_column='TOPLAM', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=50, blank=True, null=True)
    bakiyeno = models.IntegerField(db_column='BAKIYENO', blank=True, null=True)  # Field name made lowercase.
    kartutari = models.FloatField(db_column='KARTUTARI', blank=True, null=True)  # Field name made lowercase.
    depoadi = models.CharField(db_column='DEPOADI', max_length=35, blank=True, null=True)  # Field name made lowercase.
    tur = models.CharField(db_column='TUR', max_length=35, blank=True, null=True)  # Field name made lowercase.
    renk = models.CharField(db_column='RENK', max_length=33, blank=True, null=True)  # Field name made lowercase.
    beden = models.CharField(db_column='BEDEN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uruncinsi = models.CharField(db_column='URUNCINSI', max_length=44, blank=True, null=True)  # Field name made lowercase.
    plasiyer = models.CharField(max_length=44, blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)
    kkartli = models.FloatField(db_column='KKARTLI', blank=True, null=True)  # Field name made lowercase.
    alisfiyati = models.FloatField(db_column='ALISFIYATI', blank=True, null=True)  # Field name made lowercase.
    smsmusteri = models.CharField(max_length=50, blank=True, null=True)
    stok = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'satisbekle2'


class Satistemp(models.Model):
    satisno = models.AutoField(db_column='SATISNO', primary_key=True)  # Field name made lowercase.
    musterino = models.IntegerField(db_column='MUSTERINO', blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    fiyat2 = models.FloatField(blank=True, null=True)
    indirim = models.FloatField(blank=True, null=True)
    verilen = models.FloatField(db_column='VERILEN', blank=True, null=True)  # Field name made lowercase.
    kdv = models.FloatField(db_column='KDV', blank=True, null=True)  # Field name made lowercase.
    iskonto = models.FloatField(db_column='ISKONTO', blank=True, null=True)  # Field name made lowercase.
    toplam = models.FloatField(db_column='TOPLAM', blank=True, null=True)  # Field name made lowercase.
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=50, blank=True, null=True)
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    bakiyeno = models.IntegerField(db_column='BAKIYENO', blank=True, null=True)  # Field name made lowercase.
    kartutari = models.FloatField(db_column='KARTUTARI', blank=True, null=True)  # Field name made lowercase.
    depoadi = models.CharField(db_column='DEPOADI', max_length=35, blank=True, null=True)  # Field name made lowercase.
    tur = models.CharField(db_column='TUR', max_length=35, blank=True, null=True)  # Field name made lowercase.
    renk = models.CharField(db_column='RENK', max_length=33, blank=True, null=True)  # Field name made lowercase.
    beden = models.CharField(db_column='BEDEN', max_length=15, blank=True, null=True)  # Field name made lowercase.
    uruncinsi = models.CharField(db_column='URUNCINSI', max_length=44, blank=True, null=True)  # Field name made lowercase.
    plasiyer = models.CharField(max_length=44, blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)
    kkartli = models.FloatField(db_column='KKARTLI', blank=True, null=True)  # Field name made lowercase.
    alisfiyati = models.FloatField(db_column='ALISFIYATI', blank=True, null=True)  # Field name made lowercase.
    stok = models.FloatField(blank=True, null=True)

    class Meta:
        
        db_table = 'satistemp'


class Sezon(models.Model):
    sezon = models.CharField(max_length=50, blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'sezon'


class Smsmusteri(models.Model):
    adsoyad = models.CharField(db_column='Adsoyad', max_length=55, blank=True, null=True)  # Field name made lowercase.
    telefon = models.CharField(db_column='Telefon', max_length=16, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'smsmusteri'


class Stok(models.Model):
    stokno = models.AutoField(db_column='STOKNO', primary_key=True)  # Field name made lowercase.
    cinsno = models.IntegerField(db_column='CINSNO', blank=True, null=True)  # Field name made lowercase.
    urunno = models.IntegerField(db_column='URUNNO', blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=25, blank=True, null=True)  # Field name made lowercase.
    urunad = models.CharField(db_column='URUNAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    uruncins = models.CharField(db_column='URUNCINS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    islemtur = models.CharField(db_column='ISLEMTUR', max_length=15, blank=True, null=True)  # Field name made lowercase.
    carino = models.IntegerField(db_column='CARINO', blank=True, null=True)  # Field name made lowercase.
    islemno = models.IntegerField(db_column='ISLEMNO', blank=True, null=True)  # Field name made lowercase.
    aciklama = models.CharField(db_column='ACIKLAMA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fiyat = models.FloatField(db_column='FIYAT', blank=True, null=True)  # Field name made lowercase.
    fiyat2 = models.FloatField(db_column='FIYAT2', blank=True, null=True)  # Field name made lowercase.
    girisdepo = models.CharField(db_column='GIRISDEPO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cikisdepo = models.CharField(db_column='CIKISDEPO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    stokyer = models.CharField(db_column='STOKYER', max_length=35, blank=True, null=True)  # Field name made lowercase.
    renk = models.CharField(db_column='RENK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    beden = models.CharField(db_column='BEDEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    miktar = models.FloatField(db_column='MIKTAR', blank=True, null=True)  # Field name made lowercase.
    toplamtutar = models.FloatField(db_column='TOPLAMTUTAR', blank=True, null=True)  # Field name made lowercase.
    kasiyer = models.CharField(db_column='KASIYER', max_length=25, blank=True, null=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    saat = models.TimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'stok'

class Uetiket(models.Model):
    urunad = models.CharField(max_length=60)
    renk = models.CharField(max_length=50, blank=True, null=True)
    beden = models.CharField(max_length=50, blank=True, null=True)
    birim = models.CharField(max_length=50, blank=True, null=True)
    toplammiktar = models.IntegerField(blank=True, null=True)
    alisfiyati = models.FloatField(blank=True, null=True)
    satisfiyati = models.FloatField(blank=True, null=True)
    uruncinsi = models.CharField(max_length=50, blank=True, null=True)
    firmakodu = models.IntegerField(blank=True, null=True)
    barkod = models.CharField(max_length=50)
    ikincisatfiyat = models.FloatField()
    kkartli = models.FloatField()
    iskonto = models.FloatField()
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=20, blank=True, null=True)
    eskifiyat1 = models.FloatField(blank=True, null=True)
    eskifiyat2 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'uetiket'


class Urun(models.Model):
    urunno = models.AutoField(db_column='URUNNO', primary_key=True)  # Field name made lowercase.
    firmakodu = models.IntegerField(blank=True, null=True)
    renk = models.CharField(db_column='RENK', max_length=50, blank=True, null=True)  # Field name made lowercase.
    beden = models.CharField(db_column='BEDEN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birim = models.CharField(db_column='BIRIM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    uruncinsi = models.CharField(db_column='URUNCINSI', max_length=50, blank=True, null=True)  # Field name made lowercase.
    toplammiktar = models.FloatField(db_column='TOPLAMMIKTAR', blank=True, null=True)  # Field name made lowercase.
    tarih = models.DateField(db_column='TARIH', blank=True, null=True)  # Field name made lowercase.
    saat = models.TimeField(db_column='SAAT', blank=True, null=True)  # Field name made lowercase.
    alisfiyati = models.FloatField(db_column='ALISFIYATI', blank=True, null=True)  # Field name made lowercase.
    satisfiyati = models.FloatField(db_column='SATISFIYATI', blank=True, null=True)  # Field name made lowercase.
    toptanci = models.CharField(db_column='TOPTANCI', max_length=75, blank=True, null=True)  # Field name made lowercase.
    alistutari = models.FloatField(db_column='ALISTUTARI', blank=True, null=True)  # Field name made lowercase.
    satistutari = models.FloatField(db_column='SATISTUTARI', blank=True, null=True)  # Field name made lowercase.
    satistutari2 = models.FloatField(db_column='SATISTUTARI2', blank=True, null=True)  # Field name made lowercase.
    satisfiyati2 = models.FloatField(db_column='SATISFIYATI2', blank=True, null=True)  # Field name made lowercase.
    kdv = models.FloatField(db_column='KDV', blank=True, null=True)  # Field name made lowercase.
    risk = models.IntegerField(db_column='RISK', blank=True, null=True)  # Field name made lowercase.
    iskonto = models.FloatField(db_column='ISKONTO', blank=True, null=True)  # Field name made lowercase.
    urunadi = models.CharField(db_column='URUNADI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    uyari = models.IntegerField(db_column='UYARI', blank=True, null=True)  # Field name made lowercase.
    barkod = models.CharField(db_column='BARKOD', max_length=30, blank=True, null=True)  # Field name made lowercase.
    kkartli = models.FloatField(blank=True, null=True)
    marka = models.CharField(max_length=50, blank=True, null=True)
    sezon = models.CharField(max_length=50, blank=True, null=True)
    secili = models.CharField(max_length=6, blank=True, null=True)
    urunkodu = models.CharField(db_column='URUNKODU', max_length=15, blank=True, null=True)  # Field name made lowercase.
    kdvsizfiyat = models.FloatField(blank=True, null=True)
    plasiyer = models.CharField(max_length=50, blank=True, null=True)
    eskifiyat1 = models.FloatField(blank=True, null=True)
    eskifiyat2 = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'urun'