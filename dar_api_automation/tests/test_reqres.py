import allure


@allure.suite('Тестирование вебсайта reqres.in')
class TestReqres:
    @allure.title('Авторизация')
    @allure.step('Авторизовать пользователя')
    @allure.description('Яркий пример авторизации пользователя на сайте')
    @allure.severity(allure.severity_level.NORMAL)
    def test_auth(self, url):
        res = url.login()
        if res.status_code != 200:
            raise Exception("Unable to authorize using given credentials")

    @allure.title('Регистрация')
    @allure.step('Зарегистрировать пользователя')
    @allure.description('Яркий пример регистрации пользователя на сайте')
    @allure.severity(allure.severity_level.NORMAL)
    def test_register(self, url):
        res = url.register()
        assert res.status_code == 200
        result = res.json()
        result = result['id']
        assert result == 4

    @allure.title('Создание')
    @allure.step('Создать пользователя')
    @allure.description('Яркий пример создания пользователя на сайте')
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user(self, url):
        res = url.create_user()
        assert res.status_code == 201
        result = res.json()
        result = result['name']
        assert result == "morpheus"

    @allure.title('Список')
    @allure.step('Получить список пользователей')
    @allure.description('Яркий пример получения списка пользователей на сайте')
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_list(self, url):
        res = url.list_of_users()
        assert res.status_code == 200
