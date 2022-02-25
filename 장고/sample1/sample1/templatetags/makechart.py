from django import template

register=template.Library()

@register.filter
def ranges(n):
    return range(0,n)
    
@register.simple_tag
def pick_data(list,k,i,j):
    if (i*k)+j<len(list):
        return list[(i*k)+j]
    else:
        return ''