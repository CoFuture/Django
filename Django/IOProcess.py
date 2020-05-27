from api.network.FCMAnswer import FCMAnswer
from api.network.IAnswer import IAnswer


# 在这里拿到名称检索的name
def fullNameSearch(name):
    f = FCMAnswer()
    conditons = {}
    print("======================", f.getCompanyLabel(conditons, name), "==============")
    pass


# 在这里拿到条件检索的 key:value
def conditionSearch(conditions):
    f = FCMAnswer()
    company_name = conditions.pop('company_name')
    conditions.pop('csrfmiddlewaretoken')
    # 空字段用0填充
    for (key, value) in conditions.items():
        if len(value) == 0:
            conditions[key] = 0
        pass
    # print("========", conditions, "==========")

    # 币种金额处理 汇率euro：7.6324  dollar：7.0215
    regcapcur_type = conditions.pop('regcapcur_type')
    if regcapcur_type == 'money_dollar':
        conditions['regcapcur'] = int(conditions['regcapcur'] * 7.0215)
    elif regcapcur_type == 'money_euro':
        conditions['regcapcur'] = int(conditions['regcapcur'] * 7.6324)
    else:
        pass

    investnum_type = conditions.pop('investnum_type')
    if investnum_type == 'money_dollar':
        conditions['investnum'] = int(conditions['investnum'] * 7.0215)
    elif investnum_type == 'money_euro':
        conditions['investnum'] = int(conditions['investnum'] * 7.6324)
    else:
        pass

    regcap_type = conditions.pop('regcap_type')
    if regcap_type == 'money_dollar':
        conditions['regcap'] = int(conditions['regcap'] * 7.0215)
    elif regcap_type == 'money_euro':
        conditions['regcap'] = int(conditions['regcap'] * 7.6324)
    else:
        pass

    money_type_taxes = conditions.pop('money_type_taxes')
    if money_type_taxes == 'money_dollar':
        conditions['taxunpaidnum'] = int(conditions['taxunpaidnum'] * 7.0215)
    elif money_type_taxes == 'money_euro':
        conditions['taxunpaidnum'] = int(conditions['taxunpaidnum'] * 7.6324)
    else:
        pass

    # 省级市级处理
    if conditions['is_jnsn'] == 'level_province':
        conditions['is_jnsn'] = 2
    elif conditions['is_jnsn'] == 'level_city':
        conditions['is_jnsn'] = 1
    else:
        pass

    # 投资比例处理
    invest_total = 0
    for i in range(16):
        invest_total += int(conditions['inv' + str(i)])

    if invest_total != 0:
        for i in range(16):
            conditions['inv' + str(i)] = int(conditions['inv' + str(i)]) / invest_total

    # 产品通过率处理
    conditions['passpercent'] = conditions['passpercent'] / 100

    # conditions在这里拿到
    print("=========conditions============", conditions)
    print("========", f.getCompanyLabel(conditions, company_name), "==========")

    pass