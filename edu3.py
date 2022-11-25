from jinja2 import Template
from markupsafe import escape

# cars = [{'model': 'Ауди', 'price': 23000},
#        {'model': 'Шкода', 'price': 17300},
#        {'model': 'Вольво', 'price': 44300},
#        {'model': 'Фольксваген', 'price': 21300}]
#
# tpl = "Суммарная цена автомобилей {{ (cs | max(attribute='price')).model }}"
# tpl = "Автомобиль {{ cs | random }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)


# persons = [{'name': 'Алексей', 'old': 18, 'weight': 78.5},
#           {'name': 'Николай', 'old': 28, 'weight': 82.3},
#           {'name': 'Иван', 'old': 33, 'weight': 94.0}
#           ]
#
# tpl = '''
# {%- for u in users -%}
# {% filter upper %}{{u.name}}{% endfilter %}
# {% endfor -%}
# '''

# tm = Template(tpl)
# msg = tm.render(users=persons)

# html = '''
# {% macro input(name, value='', type='text', size=20) -%}
#    <input type="{{ type }}" name="{{ name }} value="{{ value|e }}" size="{{ size }}">
# {%- endmacro%}
#
# <p>{{ input('username') }}
# <p>{{ input('email') }}
# <p>{{ input('password') }}
# '''

# tm = Template(html)
# msg = tm.render()

persons = [{'name': 'Алексей', 'old': 18, 'weight': 78.5},
           {'name': 'Николай', 'old': 28, 'weight': 82.3},
           {'name': 'Иван', 'old': 33, 'weight': 94.0}
           ]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)
