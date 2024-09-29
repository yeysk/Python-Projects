# İKİNCİ DERECEDEN DENKLEM ÇÖZEN PROGRAM
## PROJE TANIMI 
Bu program, kullanıcı tarafından katsayıları girilen ikinci dereceden bir denklemin köklerini hesaplar.
## KULLANIM
Program kullanıcıdan denklemin katsayıları olan a,b, ve c değerlerini girmesini ister ve kökleri hesaplar.Geçerli bir değer girilmediği takdirde, kullanıcıya bir uyarı mesajı göstererek tekrar giriş yapmasını ister.
### ADIMLAR
1. **Katsayıların Girilmesi**:
-Program kullanıcıdan sırasıyla a,b ve c katsayılarını girmesini ister.Her katsayı için bir değer girişi yapıldıktan sonra sıradaki katsayı için değer girişi istemeden önce program girilen değerin geçerli olup olmadığını kontrol eder.Geçerliyse sıradaki katsayı için giriş istenir.
2. **Diskriminant Değerinin Hesaplanması**:
-Katsayıların sorunsuz bir şekilde girilmesinin ardından, program b^2 – 4*a*c formülünü kullanarak denklemin diskriminantını hesaplar ve matematiksel kurallara göre diskriminant değerini kontrol eder.(Diskriminant > 0 ise; iki farklı reel kök, Diskriminant < 0 ise; reel kök yok, Diskriminant = 0 ise; bir tane reel kök var.) 
3. **Köklerin Hesaplanması**:
-Reel kökler var ise bunlar (-b ± √D) / (2a) matematiksel formülleri ile hesaplanır işlem sonlanır.
