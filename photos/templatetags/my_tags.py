from django import template
from django.template.base import VariableNode
from django.contrib.auth import get_user_model
register = template.Library() # 우리가 만든 함수를 템플리에서 사용할 수 있도록 등록해주는 역할

@register.filter(name='did_like') 
def did_like(photo, user):
    return photo.like_set.filter(user=user, status=True).exists()



@register.tag(name='addnim')
def add_nim(parser, token):
    nodelist = parser.parse(('end_add_nim'))
    parser.delete_first_token()

    return NimNode(nodelist)


class NimNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist
        self.user_class = get_user_model()

    def render(self, context):
        outputs = []
        for node in self.nodelist:
            if not isinstance(node, VariableNode):
                outputs.append(node.render(context))
                continue

            obj = node.filter_expression.resolve(context)
            
            if not isinstance(obj, self.user_class):
                outputs.append(node.render(context))
                continue
                
            outputs.append('{}님'.format(node.render(context)))

        return ''.join(outputs)