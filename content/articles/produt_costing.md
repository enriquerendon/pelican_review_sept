Title: SAP Product Costing (CO-PC)
Author: Enrique Rendon
Date: 2019-10-30 16:28
Category: blog
Tags: SAP, markdown, pelican
Slug: my-sap-co-pc-notes
Status: published
Summary: A summary of CO-PC notes and experiences.
Lang: en
Translation: false

### Purchased Items
- Products that you buy and consume or sell without any transformation/manufacturing.
### Manufactured Products
- Products that required transformation. From Raw --> Finished.
-
### Different Between Price & Cost

- Price:
	- Money that you pay/collect when buying/selling products to/from vendors/customers.
- Cost:
		- Is the value of your inventory/stocks in your accounting books.
		- This could include freight, customs, duties, handling, insurance, assembly, etc. (Landed Cost)
		- Anything required in order to be ready for use.

### Inventory Methods
- [V]   Moving average price/periodic unit price
- [S]   Standard price

![accounting 1]({static}/images/MM03_accounting_1.png "Display Material >> Accounting 1")

### Moving Average
- First In First Out (FIFO)
- Last In Last Out (LIFO)

The formula for moving average:

$$
Moving Average = \frac{Total Stock Value}{Total Stock Quantity}
$$

### Standard Costing
- Actual Costing (Material Ledger)




***************

Headers
---------------------------

# Header 1

## Header 2

### Header 3

Styling
---------------------------

*Emphasize*  _emphasize_

**Strong**  __strong__

==Marked text.==

~~Mistaken text.~~

> Quoted text.

H~2~O is a liquid.

2^10^ is 1024.

Lists
---------------------------

- Item
 * Item
 + Item

1. Item 1
2. Item 2
3. Item 3

- [ ] Incomplete item
- [x] Complete item

Links
---------------------------

A [link](http://example.com).

An image: ![Alt](img.jpg)

A sized image: ![Alt](img.jpg =60x50)

Code
---------------------------

Some `inline code`.

```
// A code block
var foo = 'bar';
```

```javascript
// An highlighted block
var foo = 'bar';
```

Tables
---------------------------

Item | Value
-------- | -----
Computer | $1600
Phone | $12
Pipe | $1

| Column 1 | Column 2 |
|:--------:| -------------:|
| centered | right-aligned |

Definition lists
---------------------------

Markdown
:  Text-to-HTML conversion tool Authors
:  John
:  Luke Footnotes
---------------------------

Some text with a footnote.[^1]

[^1]: The footnote.

Abbreviations
---------------------------

Markdown converts text to HTML.

*[HTML]: HyperText Markup Language

LaTeX math
---------------------------

The Gamma function satisfying $\Gamma(n) = (n-1)!\quad\forall
n\in\mathbb N$ is via the Euler integral

$$
\Gamma(z) = \int_0^\infty t^{z-1}e^{-t}dt\,.
$$
