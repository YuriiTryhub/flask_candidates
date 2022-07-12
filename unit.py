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
    candidates = load_candidates()
    for j in candidates:
        if pk == j['pk']:
            candidate_pk = f"{j['name']}"
            return candidate_pk


def get_by_skill(skill_name):
    """которая вернет кандидатов по навыку"""
    pass
