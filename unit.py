import json


def load_candidates():
    """которая загрузит данные из файла"""
    with open('candidates.json', mode='r', encoding='utf-8') as f:
        candidates = json.load(f)
    return candidates


def get_all(candidates):
    """которая покажет всех кандидатов"""
    for i in candidates:
        candidates_list = i['name']
        return candidates_list



def get_by_pk(pk):
    """которая вернет кандидата по pk"""
    pass

def get_by_skill(skill_name):
    """которая вернет кандидатов по навыку"""
    pass
