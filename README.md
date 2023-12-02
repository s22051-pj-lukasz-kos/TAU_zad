# Testowanie automatyczne (TAU)

## Laboratorium 1

Program w Java 11. Testy w JUnit5.

## Laboratorium 2

### Scenariusz testowy 1 (test_first_set)

- Strona: https://www.selenium.dev/selenium/web/web-form.html
- Kliknięcie w pole Text Input i wypełnienie go tekstem. Oszacowanie czy tekst się zgadza. 
- Kliknięcie w pole Password i wypełnienie go tekstem. Oszacowanie czy tekst się zgadza.
- Kliknięcie w pole Textarea i wypełnienie go tekstem. Oszacowanie czy tekst się zgadza. 
- Kliknięcie w Dropdown (select) i wybranie opcji "Two". Oszacowanie czy wartość się zgadza. 
- Kliknięcie w pole Dropdown (datalist) i wpisanie "Los". Oszacowanie czy fropdown zawiera tylko jeden element. 
- Kliknięcie w przycisk Submit i oszacowanie czy załadowała się kolejna strona. 

### Scenariusz testowy 2 (test_second_set)

- Strona: https://smakliter.pl/
- Kliknięcie w przycisk "Rozumiem" w banerze informującym o cookies
- Wpisanie w wyszukiwarkę "umówmy" i kliknięcie przycisku szukania
- Znalezienie książki "Umówmy się na Polskę"
- Dodanie jej do koszyka
- Kliknięcie przycisku "Przejdź do koszyka"
- Upewnienie się, że jesteś na odpowiedniej podstronie (/koszyk)