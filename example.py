import lib.deprem as deprem #1.0

#Burada değişkenleri ataya bilirsiniz
veriboyut1 = deprem.veriboyutu(1)
veriboyut2 = deprem.veriboyutu(2)

deprem.depremveri() # anlık verileri sadece bir kere yazar
deprem.veriboyutu(1) #gelen veri boyutunu söyler 1-veriler için 2-zaman için kullanılır
deprem.sondepreptarih() # anlık son deprem tarihini ve saatini yazar
deprem.deprepolcer(5,True) # 5sn de bir anlık verileri yeniler / (5) = 5sn (5, True) = veri boyutu işler

#NOT : bu python kütphanei geliştirilmesi devam etmektedir kullanılan özeliklrt tamamen deneyseldir.
# Hatalar ve eksiklikler bulunmaktadır. Fakat zaman ilde düzeltilip yenilenecektir son hali için takip ediniz.
