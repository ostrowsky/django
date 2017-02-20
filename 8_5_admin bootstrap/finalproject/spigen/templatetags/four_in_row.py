from django import template
register = template.Library()

@register.simple_tag
def is_fourth(counter):
    return (counter%4) == 0 and counter != 0

#register.filter('is_fourth', is_fourth)

if __name__ == '__main__':
    for i in range(25):
        print(i, is_fourth(i))

