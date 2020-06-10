# casper-backinstock
Noooo, [Casper UK](https://casper.com/uk/en) are going out of business! 😢

What's that? ***60%*** off ***EVERYTHING?!*** Awesome!

Oh, it's all out of stock.

>https://casper.com/uk/en/inspiration/faqs/
> ######2. Will Casper restock any products that are currently sold out?
> We will not be restocking Casper products marked as “sold out.” For Casper products listed as “out of stock,” please continue to check our website for updates as we will be restocking in limited quantities this month only. If a product is not listed on our site, it is no longer available.

Well screw that, I want some damn sheets!

### Setup: 
```
python3 -m venv venv
pip install -r requirements.txt
```

### Usage: 
```
python run.py
```

### Configuration:

Add some products to `favourite_products` to get a notification when they are listed as in stock.

### Example output:

```
pillow:
+---------+------------+------------+------+--------+--------------+----------------+----------------+
| product |   title    |    size    | type | colour |    price     | discount_price | naive_in_stock |
+---------+------------+------------+------+--------+--------------+----------------+----------------+
| pillow  |  Standard  |  standard  |      |        | Out of Stock |      n/a       |     False      |
| pillow  | Super King | super-king |      |        | Out of Stock |      n/a       |     False      |
+---------+------------+------------+------+--------+--------------+----------------+----------------+
bedding:
+--------------------+---------------------------+-----------------------+--------------+-------------+--------------+----------------+----------------+
|      product       |           title           |         size          |     type     |   colour    |    price     | discount_price | naive_in_stock |
+--------------------+---------------------------+-----------------------+--------------+-------------+--------------+----------------+----------------+
|       sheets       |    Single 90 X 190 CM     |        single         | fitted-sheet | White/White |     £45      |     £18.00     |      True      |
|       sheets       |   EU Single 90 X 200 CM   |   eu-single-90x200    | fitted-sheet | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |    Double 135 X 190 CM    |        double         | fitted-sheet | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |  EU Double 140 X 200 CM   |   eu-double-140x200   | fitted-sheet | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |           King            |         king          | fitted-sheet | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |   EU King 160 X 200 CM    |    eu-king-160x200    | fitted-sheet | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |        Super King         |      super-king       | fitted-sheet | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |    Single 90 X 190 CM     |        single         | fitted-sheet | White/Slate |     £45      |     £18.00     |      True      |
|       sheets       |   EU Single 90 X 200 CM   |   eu-single-90x200    | fitted-sheet | White/Slate |     £45      |     £18.00     |      True      |
|       sheets       |    Double 135 X 190 CM    |        double         | fitted-sheet | White/Slate | Out of Stock |      n/a       |     False      |
|       sheets       |  EU Double 140 X 200 CM   |   eu-double-140x200   | fitted-sheet | White/Slate | Out of Stock |      n/a       |     False      |
|       sheets       |           King            |         king          | fitted-sheet | White/Slate | Out of Stock |      n/a       |     False      |
|       sheets       |   EU King 160 X 200 CM    |    eu-king-160x200    | fitted-sheet | White/Slate |     £55      |     £22.00     |      True      |
|       sheets       |        Super King         |      super-king       | fitted-sheet | White/Slate | Out of Stock |      n/a       |     False      |
|       sheets       |    Single 140 X 200 CM    |  single-140-x-200-cm  | duvet-cover  | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |    Double 200 X 200 CM    |  double-200-x-200-cm  | duvet-cover  | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |     King 225 X 220 CM     |   king-225-x-220-cm   | duvet-cover  | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |  Super King 260 X 220 CM  | super-king-260x220-cm | duvet-cover  | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |    Single 140 X 200 CM    |  single-140-x-200-cm  | duvet-cover  | White/Slate |     £70      |     £28.00     |      True      |
|       sheets       |    Double 200 X 200 CM    |  double-200-x-200-cm  | duvet-cover  | White/Slate |     £75      |     £30.00     |      True      |
|       sheets       |     King 225 X 220 CM     |   king-225-x-220-cm   | duvet-cover  | White/Slate | Out of Stock |      n/a       |     False      |
|       sheets       |  Super King 260 X 220 CM  | super-king-260x220-cm | duvet-cover  | White/Slate |     £95      |     £38.00     |      True      |
|       sheets       |         Standard          |       standard        |  pillowcase  | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |        Super King         |      super-king       |  pillowcase  | White/White | Out of Stock |      n/a       |     False      |
|       sheets       |         Standard          |       standard        |  pillowcase  | White/Slate | Out of Stock |      n/a       |     False      |
|       sheets       |        Super King         |      super-king       |  pillowcase  | White/Slate | Out of Stock |      n/a       |     False      |
|       duvet        |    Single 140 X 200 CM    |  single-140-x-200-cm  |              |             | Out of Stock |      n/a       |     False      |
|       duvet        |    Double 200 X 200 CM    |  double-200-x-200-cm  |              |             | Out of Stock |      n/a       |     False      |
|       duvet        |     King 225 X 220 CM     |   king-225-x-220-cm   |              |             | Out of Stock |      n/a       |     False      |
|       duvet        |  Super King 260 X 220 CM  | super-king-260x220-cm |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector |    Single 90 X 190 CM     |        single         |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector |   EU Single 90 X 200 CM   |   eu-single-90x200    |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector | Small Double 120 X 190 CM |     small-double      |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector |    Double 135 X 190 CM    |        double         |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector |  EU Double 140 X 200 CM   |   eu-double-140x200   |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector |           King            |         king          |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector |   EU King 160 X 200 CM    |    eu-king-160x200    |              |             | Out of Stock |      n/a       |     False      |
| mattress-protector |        Super King         |      super-king       |              |             | Out of Stock |      n/a       |     False      |
+--------------------+---------------------------+-----------------------+--------------+-------------+--------------+----------------+----------------+
```
