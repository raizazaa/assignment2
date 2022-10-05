# PBP Assignment 5: Web Design Using HTML, CSS, and CSS Framework

[Heroku Application](https://raaassignment2.herokuapp.com/todolist/)

## What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?

Inline: Class style css that only applies to one HTML tag. It's recommended if you want to differentiate one tag from the other, but it's not optimal if the project is big and styling the tags one by one.
</br>
Internal: Class style css that applies to one HTML page. It is used if you want to style one whole page and you don't need to upload more css files as it is in the HTML file itself. But, changes only applies to one page, not good if you want to apply css to multiple HTML files.
</br>
External: Class style css that uses external .css file. Advantages are that the HTML file is smaller, loading speed is much faster compared to the other methods, and you can use the same css rule to multiple HTML files. Though it will take time before the page be perfect because it need to call the css file.

## Describe the HTML5 tags that you know.
<ul>
  <li>h$: multiple header tags</li>
  <li>button: use to create button</li>
  <li>table: use to create table</li>
  <li>body: defines the page's body</li>
  <li>br: single line break</li>
  <li>img: represent an image</li>
</ul>

## Describe the types of CSS selectors you know.
<ul>
  <li>Simple selectors (select elements based on name, id, class)</li>
  <li>Combinator selectors (select elements based on a specific relationship between them)</li>
  <li>Pseudo-class selectors (select elements based on a certain state)</li>
  <li>Pseudo-elements selectors (select and style a part of an element)</li>
  <li>Attribute selectors (select elements based on an attribute or attribute value)</li>
</ul>
source: https://www.w3schools.com/css/css_selectors.asp

## Explain how you would implement the checklist above.
First, I added lines to the base.html in the root templates to include Bootstrap’s CSS and JS. Then, I tried to customize the HTML page by external CSS with style.css in the static/css folder (such as changing background colors, alignment, and the likes). I changed the table format into card format by using the tag card and container. To make it responsive, I made div classes for row and column and @media in the css file. I used [this site](https://www.w3schools.com/HOWTO/howto_css_column_cards.asp) as guidance.