Title: My First Blog Post
Author: Enrique Rendon
Date: 2019-10-4 12:10
Category: blog
Tags: python, markdown, pelican
Slug: my-first-blog-post
Status: published

Blog post content goes here

Keyword	| Required?	| Usage
--- | --- | ---
Title	| Yes	| title of the blog post
Author	| Yes	| author of the blog post
Date	| Yes	| published date in the format YYYY-mm-dd hh:mm
Modified	| No	| last edit date in the format YYYY-mm-dd hh:mm
Category	| Yes	| general topic of the blog post
Tags	| No	| topics covered in the blog post separated by a comma
Summary	| No	| brief one or two sentence synopsis of the blog post
Slug	| No	| name of the .html file to be generated. If none is defined the slug will be the post's title separated by "-" symbols
Status	| No	| choose one of published, draft or hidden


Metadata | Description
--- | ---
title | Title of the article or page
date | Publication date (e.g., YYYY-MM-DD HH:SS)
modified | Modification date (e.g., YYYY-MM-DD HH:SS)
tags | Content tags, separated by commas
keywords | Content keywords, separated by commas (HTML content only)
category | Content category (one only — not multiple)
slug | Identifier used in URLs and translations
author | Content author, when there is only one
authors | Content authors, when there are multiple
summary | Brief description of content for index pages
lang | Content language ID (en, fr, etc.)
translation | Is content is a translation of another (true or false)
status | Content status: draft, hidden, or published
template | Name of template to use to generate content (without extension)
save_as | Save content to this relative file path
url | URL to use for this article/page


Basic markdown examples are shown below

This text is **bold**
This text is also __bold__

This text is *italic*
This text is also _italic_

This text is **_italic and bold_**

# An h1 heading
## An h2 heading
### An h3 heading...
###### An h6 heading

A list with numbers:
1. One
2. Two
3. Three

A list with bullets:
* Bullet
* Bullet
* Bullet

Here's a blockquote:

>Simple is better than complex

Here's a table:

| Column1 | Column 2 | Column 3
|---|---|---|
| Value 1 | Value 2 | Value 3 |
| Value 4 | Value 5 | Value 6 |
| Value 7 | Value 8 | Value 9 |


Images can be displayed in Markdown.  
Text within the square brackets is the image name. The path to the image goes between the round brackets.  
The {static} tag indicates the image is stored in the content folder. This setting can be changed in pelicanconf.py.

![python logo]({static}/images/python_icon.png)

Links to downloadable content such as PDF files are written similarly to image files but with no ! symbol at the beginning.

[Pelican Documentation]({static}/docs/pelican.pdf)

A link to a different blog post on our website is written exactly the same.  
Text within the square brackets can be clicked on to travel to the website between the curly brackets.
The {filename} tag indicates we want to follow the link to a webpage rather than the static file it was generated from.

[First Post]({filename}/articles/first_article.md)

Or we can link to another external website by supplying the web address.

[Python Package Index](https://pypi.org)



Code blocks are preceeded by an indent, three : symbols and the name of the language.  
All of the following code will be highlighted while the text is indented.

    :::python3
    def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        return func(*args, **kwargs).lower()
    return wrapper_do_twice

    @do_twice
    def say_whee(some_text):
        print(some_text)

    x = 'Whee!'
    say_whee(x)
