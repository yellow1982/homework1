class User:
    def __init__(self):
        self.nickname = str("")
        self.password = hash("")
        self.age = int()

    def __str__(self):
        return str(self.nickname)


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title)
        self.duration: int
        self.duration = int(duration)
        self.adult_mode = adult_mode
        self.time_now = 0


class UrTube:
    current_user = None

    def __init__(self):
        self.users = []
        self.videos = []

    def register(self, name, password, age):
        user = User()
        user.nickname = name
        user.password = password
        user.age = age
        if not self.users:
            self.users.append(user)
            self.current_user = user
        else:
            for u in self.users:
                if str(user) == str(u):
                    print(f"Пользователь {name} уже существует")
                    break
                else:
                    self.users.append(user)
                    self.current_user = user
                    break

    def log_in(self, login, password):
        for usr in self.users:
            if login == str(usr) and hash(password) == hash(usr.password):
                self.current_user = usr
                break
            elif login == usr and hash(password) != hash(usr.password):
                print("Не верный пароль!!!")
                break
            else:
                print("Такого пользователя не существует")
                break

    def add(self, *args):
        for vid in args:
            vid_is_exists = False
            for v in self.videos:
                if vid.title == v.title:
                    print("Такое видео уже существует.")
                    vid_is_exists = True
                    break
            if vid_is_exists:
                break
            else:
                self.videos.append(vid)

    def get_videos(self, word):
        search_list = []
        for vid in self.videos:
            str_lower = str(vid.title).lower()
            if word.lower() in str_lower:
                search_list.append(vid.title)
        if not search_list:
            return "По Вашему запросу ничего не найдено."
        else:
            return search_list

    def watch_video(self, title_for_play):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")

        else:
            for vid in self.videos:
                if vid.title == title_for_play:
                    if vid.adult_mode and self.current_user.age < 18:
                        print("Вам нет 18 лет. Пожалуйста, покиньте страницу")
                    else:
                        while vid.time_now < vid.duration:
                            print(vid.time_now + 1, end=" ")
                            vid.time_now += 1
                        print("Конец видео")

    def log_out(self):
        self.current_user = None


if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    #
    ## Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    #
    ## Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
 
