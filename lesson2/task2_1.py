#Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайтов Superjob и HH. Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
#- Наименование вакансии.
#- Предлагаемую зарплату (отдельно минимальную и максимальную).
#- Ссылку на саму вакансию.
#- Сайт, откуда собрана вакансия.

#По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.

#Можно выполнить по желанию один любой вариант или оба при желании и возможности.

from lxml import html
import requests

position = input('Введите искомую вакансию: ')
url = 'https://www.superjob.ru/vacancy/search/'
site = 'https://www.superjob.ru'
header={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',}
params = {'page': '',}

req = requests.get(url, params=params, headers=header)
dom = html.fromstring(req.content)
last_page=int(dom.xpath("//a[contains(@class,'f-test-button-')]/span/span/span/text()")[-2])
vacancy_list = []
for page in range(1,last_page+1):
        params['page'] = page
        req = requests.get(url, params=params, headers=header)

        dom = html.fromstring(req.content)
        vacances = dom.xpath("//div[contains(@class,'f-test-vacancy-item')]")
        for vacancy in vacances:
            vacancy_inf={}
            salary_processing = []
            name = vacancy.xpath(".//span/a[contains(@class,'f-test-link-')]/text()")[0]
            if name == 'Руководитель отела тендерных продаж':
                i=1
            if position.lower() in name.lower():
                vacancy_inf['name']=name
                href = vacancy.xpath(".//span/a[contains(@class,'f-test-link-')]/@href")[0]
                vacancy_inf['href']=''.join((site, href))
                salary = vacancy.xpath(".//div[contains(@class,'f-test-text-company-item-salary')]/span/text()")
                for i in range(len(salary)):
                    if salary[i].replace(u'\xa0', u' ') != " ":
                        salary_processing.append(salary[i].replace(u'\xa0', u' '))
                min_salary ='none'
                max_salary ='none'
                if 'от' in salary_processing:
                    min_salary = salary_processing[1]
                elif 'до' in salary_processing:
                    max_salary = salary_processing[1]
                elif len(salary_processing)==1 or len(salary_processing)==3:
                    min_salary = salary_processing[0]
                else:
                   min_salary = salary_processing[0]
                   max_salary = salary_processing[2]
                if '₽' in min_salary: min_salary=min_salary[:-2]
                if '₽' in max_salary: max_salary=max_salary[:-2]
                vacancy_inf['min_salary']=min_salary
                vacancy_inf['max_salary']=max_salary
                vacancy_inf['site']=site
                vacancy_list.append(vacancy_inf)
print(vacancy_list)
