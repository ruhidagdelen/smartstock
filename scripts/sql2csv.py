from db2csv.models import Cins,Retiketi,Kasa,Satis,Stok,Uetiket,Urun 
# SqlDB django modellerine donusturuldu ve modellerden import edildi
import pandas as pd

# Elizmizde olan sql dosyalarini pandas ve diger gerekli platformlarda kullanabilmek
# icin csv formatina donusturme islemi

# Generic bir fonksyon yazmak yerine DB'deki her tablo farkli oldugundan
# ve tablolardi butun sutunlara ihtiyac olmadigindan modeller manuel olarak cekildi
# bu sebeple butun fonksyonlarin calisma mantiklari ayni olmakla beraber kullandiklari
# fieldlar birbirlerinden farkli
# yorumlar tek fonksyon uzerinden anlatilmis olup digerlerine gerek duyulmadi

def types(obj):
	# DB'deki cins tablosu
	types = [] # bir dictionary yarattik

	for ele in obj: # for dongusu ile cins tablosundaki istedigimiz sutunlar dictionary'e eklendi
		types.append({"type_id":ele.cinsno,"type":ele.cins})

	df = pd.DataFrame(types,columns=["type_id","type"]) # bu verilerle datafram olusturuldu
	df = df.fillna(value="blank") # bos olan satir varsa "blank" degeri ile dolduruldu
	df.to_csv('types.csv',index=False) # yeni csv dosyasina aktardik


def labelR(obj):
	labelR = []
	
	for ele in retiketi:
		labelR.append({"product_id":ele.id,
			"barcode":ele.barkod,
			"product_name":ele.urunad,
			"type":ele.uruncinsi,
			"purchase_price":ele.alisfiyati,
			"selling_price":ele.satisfiyati,
			"selling_wcard":ele.kkartli})

	df = pd.DataFrame(labelR,columns=["product_id",
		"barcode",
		"product_name",
		"type",
		"purchase_price",
		"selling_price",
		"selling_wcard"])
	df = df.fillna(value="blank")
	df.to_csv('scripts/labelR.csv',index=False)


def case(obj):
	case = []

	for ele in kasa:
		case.append({"process_id":ele.kasano,
			"process_type":ele.islemtur,
			"selling_wcard":ele.kredikartli,
			"selling_wcash":ele.nakitsat,
			"buyback":ele.nakital,
			"date":ele.tarih,
			"hour":ele.saat})

	df = pd.DataFrame(case,columns=["process_id",
		"process_type",
		"selling_wcard",
		"selling_wcash",
		"buyback",
		"date",
		"hour"])
	df = df.fillna(value="blank")
	df.to_csv('scripts/case.csv',index=False)


def transactions(obj):
	transaction = []
	cins = Cins.objects.all()
	satis = Satis.objects.all()

	for ele in satis:
		transaction.append({"transaction_id":ele.satisno,
			"barcode":ele.barkod,
			"product_id":ele.urunno,
			"type":ele.uruncinsi,
			"product_name":ele.urunad,
			"purchase_price":ele.alisfiyati,
			"selling_price":ele.fiyat,
			"process_type":ele.tur,
			"follow_id":ele.takipno,
			"cashier":ele.kasiyer,
			"date":ele.tarih,
			"hour":ele.saat})

	df = pd.DataFrame(transaction,columns=["transaction_id",
		"barcode",
		"product_id",
		"type",
		"product_name",
		"purchase_price",
		"selling_price",
		"process_type",
		"follow_id",
		"cashier","date",
		"hour"])	
	df = df.fillna(value="blank")
	df.to_csv('scripts/transactions.csv',index=False)


def stock(obj):
	stock = []

	for ele in stock:
		stock.append({"stock_id":ele.stokno,
			"barcode":ele.barkod,
			"type":ele.uruncins,
			"product_name":ele.urunad,
			"price":ele.fiyat,
			"process_type":ele.islemtur,
			"cashier":ele.kasiyer,
			"date":ele.tarih,
			"hour":ele.saat})

	df = pd.DataFrame(stock,columns=["stock_id",
		"barcode",
		"type",
		"product_name",
		"price",
		"process_type",
		"cashier",
		"date",
		"hour"])	
	df = df.fillna(value="blank")
	df.to_csv('scripts/stock.csv',index=False)

	
def labelU(obj):
	labelU = []
	
	for ele in uetiket:
		labelU.append({"product_id":ele.id,
			"barcode":ele.barkod,
			"product_name":ele.urunad,
			"type":ele.uruncinsi,
			"purchase_price":ele.alisfiyati,
			"selling_price":ele.satisfiyati,
			"selling_wcard":ele.kkartli})

	df = pd.DataFrame(labelU,columns=["product_id",
		"barcode",
		"product_name",
		"type",
		"purchase_price",
		"selling_price",
		"selling_wcard"])
	df = df.fillna(value="blank")
	df.to_csv('scripts/labelU.csv',index=False)


def product(obj):
	products = []

	for ele in urun:
		products.append({"product_id":ele.urunno,
			"barcode":ele.barkod,
			"product_name":ele.urunadi,
			"type":ele.uruncinsi,
			"purchase_price":ele.alisfiyati,
			"selling_price":ele.satisfiyati,
			"price_without_taxes":ele.kdvsizfiyat,
			"selling_wcard":ele.kkartli,
			"date":ele.tarih,
			"hour":ele.saat})

	df = pd.DataFrame(products,columns=["product_id",
		"barcode",
		"product_name",
		"type",
		"purchase_price",
		"selling_price",
		"price_without_taxes",
		"selling_wcard",
		"date",
		"hour"])
	df = df.fillna(value="blank")
	df.to_csv('scripts/products.csv',index=False)




cins = Cins.objects.all() # Db'deki verilerin ice aktarimi
types(cins) # fonsyon cagirilarak gerceklenen is

retiketi = Retiketi.objects.all()
labelR(retiketi)

kasa = Kasa.objects.all()
case(kasa)

satis = Satis.objects.all()
transactions(satis)

stok = Stok.objects.all()
stock(stok)

uetiket = Uetiket.objects.all()
labelU(uetiket)

urun = Urun.objects.all()
product(urun)
