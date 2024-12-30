# CryptoImager

Program kodujący hasła/dowolny tekst w obrazach za pomocą LSB.
Jak to ma działać (przynajmniej w mojej głowie):
> Program ma posiadać kilka warstw zabezpieczeń
> 1. Najpierw podajemy tekst do zapisania w obrazku
> 2. Wybieramy obrazek gdzie mają być zapisane dane
> 3. Podajemy secret key dekodujący dane
> 4. Pogram wgrywa dane do obrazka
> 5. Program podaje nam ciąg liczb/ciąg znaków który odpowiada lokalizacji danych bitów zapisanych w obrazku z wiadomością
> Nasz secret key jest odpowiedzialny za dekodowanie samej wiadomości
> Dodatkowy, powiedzmy seed, jest kolejną warstwą zabezpieczeń, w nim jest zapisana informacja na których pikselach znajduje się nasza informacja
> Przy dekodowaniu musimy też podać w jakiej kolejności mają być ułożone nasze bity, żeby wyszła nasza wiadomość.
> Na końcu kiedy mamy już naszą wiadomość w bitach i przekonwertujemy ją na str to wchodzi dopiero nasze hasło które dekoduje wiadomość na czytelną dla człowieka 
