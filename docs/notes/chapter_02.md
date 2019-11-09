# base.html
The `block` control statement defines the place where the derived templates can insert themselves. Blocks are given a *unique name*, which derived templates can reference when they provide their content.

# index.html
The `extends` statement establishes the inheritance link between the two templates, so that Jinja2 knows that when it is asked to render `index.html` it needs to embed it inside `base.html`. The two templates have matching `block` statements with name  `content`, and this is how Jinja2 knows how to combine the two templates into one. Now if I need to create additional pages for the application, I can create them as derived templates from the same base.html template, and that is how I can have all the pages of the application sharing the same look and feel without duplication.
