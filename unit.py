import json


def load_candidates():
    """которая загрузит данные из файла"""
    with open('candidates.json', mode='r', encoding='utf-8') as f:
        candidates = json.load(f)
    print(candidates)


def get_all():
    '''которая покажет всех кандидатов'''
    pass


def get_by_pk(pk):
    '''которая вернет кандидата по pk'''
    pass

def get_by_skill(skill_name):
    '''которая вернет кандидатов по навыку'''
    pass
