# django-jeaves

Django [EAV] using `JSONField`

# Features/requirements
- Uses one `django.contrib.postgres.JSONField` (PostgreSQL jsonb field) per model.
- Django 1.9, 1.10, 1.11 (with their supported python versions)
- PostgreSQL >= 9.4 and Psycopg2 >= 2.5.4.

# Running the tests

`tox`


# Rationale

At Zostera, we tried some different approaches to store attributes for our records.
While existing solutions using a `Unit`, `Attribute` and `ObjectAttribute` models did work,
they resulted in performance issues while retrieving big lists with a lot of attributes.

This project is basically some nice syntax around the idea outlined in
[this blogpost](http://coussej.github.io/2016/01/14/Replacing-EAV-with-JSONB-in-PostgreSQL/).


# Related projects

- [django-eavkit](https://github.com/sakkada/django-eavkit)
- [django-eav](https://github.com/mvpdev/django-eav)
- [django-dynamic-model](https://github.com/dobarkod/django-dynamic-model) (abandoned)


[EAV]: https://en.wikipedia.org/wiki/Entity%E2%80%93attribute%E2%80%93value_model
