import time
print('КВЕСТ')
print('Познание высоты программирования(на Python)')
name = input('Приветствую! Для начала квеста прошу указать своё НАСТОЯЩЕЕ имя: ')
floor = int(input('Прекрасно, а также прошу указать свой пол: 1 - мужской, 2 - женский'))
print('Всё, благодарю, а теперь прошу сосредоточиться на атмосфере 6338-й группы по EasyCode(шучу, у нас хорошая атмосфера))')
time.sleep(3)
if floor == 1:
    print('Дописывая очередной код ты не уследил за временем и сам не заметил, как закрыл глаза, а затем и вовсе уснул. Очнувшись от щекотных ударов по твоей щеке, что позже, как оказалось, это был долждь, ты огляделся по сторонам и, как оказалось, попал в какую-то пустошь. Чтож, удачи тебе!')
    time.sleep(18)
    print('...')
    time.sleep(2)         
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)              
    choise1 = input('''Дождь с молниями, никого в округе. Какая-то черная темень, равнина с какими то огрызками чего-то. Все это очень пугает, а огрызки напоминают код. Ты шел по развалившимся кодам, которые кто-то погрыз, попробуешь разобраться в коде?''')
    if choise1 == 'да':
        choise2 = input('В попытках разобраться в коде ты ничего не понял, но зато на тебя кто-то идёт, окутанный в черные лохмотья и весь истрепанный, будешь убегать?')
    elif choise1 == 'нет':
        choise2 = input('Ты решил не разбираться в коде, но теперь твоему взору открылось еще больше кодов...и все они тоже избиты и потрёпаны. Вдруг среди них вышел человек в черной мантии, идущий прямо на тебя и махая тебе рукой. Будешь убегать?')               
        if choise2 == 'да':
            choise3 = input('Испугавшись человека в черном ты начал убегать, но споткнулся об камень, упал и потерял сознание... Очнулся ты лишь спустя некоторое время, услышав рядом шаги и хруст веток под звуки капающего дождя.')
            time.sleep(7)
            print('- Ты как?')
            time.sleep(3)
            print('- Вы кто?')
            time.sleep(3)
            choise3 = input('Перед вами стоял тот самый человек в черном, от которого вы решили убежать. На лицо ему 23 года, кудрявые волосы и утомленный вид лица. Он протягивает тебе руку. Протянуть в ответ свою руку?')
        elif choise2 == 'нет':
            choise3 = input('Поняв, что человек не представляет из себя опасности, ты пошел к нему навстречу, но тут молния ударила прям рядом с вами. Успев среагировать ты отпрыгнули прямо в остатки кода и по вам ударило током... Странно... К вам подошел тот самый человек. Он протягивает вам руку чтобы вы встали, примите его помощь?')   
            if choise3 == 'да':
                print('Ты протянул свою руку человеку в черном. Он поднял вас резким движением и спросил:')
                time.sleep(5)
                print('- Ты как попал сюда? Что ты вообще тут делаешь?')    
                time.sleep(3)
                print('- Я сам не понял как здесь оказался, помню, только, как писал код, а затем просто уснул.')
                time.sleep(6)
                print('- Ну ты даешь... Ладно, здесь и не такое случалось.')    
                time.sleep(3)
                print('- А что здесь случилось-то?') 
                time.sleep(3)
                print('- Хр... Дай расскажу все, но только спрошу как тебя зовут.')
                time.sleep(6)
                print(f'- {name}')     
                time.sleep(3)
                print('- Чтож, мое имя Михаил, но можешь звать просто Миша, и с моей группой произошло просто нечто... Один из учеников решил познать полностью программирование на Python, но... Это того не стоило. Он реально попробовал код, и когда он его прожевал, в него вселился какой-то монстр. Он начал трепать все наши коды, испугал всех одногруппников, от чего все разбежались, он написал программу на виртуальной клавиатуре чтобы пошел дождь с большими тучами, которые закрыли нам небо. Теперь я брожу в поисках своих учеников, а он... Арсений, тот монстр, испарился, но я не уверен, что он пропал. Он поджидает момента чтобы напасть, ведь теперь он полностью познал программирование на питоне и...')
                time.sleep(26)
                print('Не успел Михаил договорить, как большущая молния ударила по некому коду, прогремел взрыв, и тут показался он... Огромное существо, ливитирующее в воздхе, представляющее из себя некую черную массу, расхохоталось во весь голос, что молния снова ударила, но уже ближе к тебе.')    
                time.sleep(10)
                print('- КАК ЖЕ ВЫ ГЛУПЫ, ХРУПКИЕ СОЗДАНИЯ, ВЫ ПРОСТО НЕ ПОНИМАЕТЕ, ЧЕГО Я ДОБИЛСЯ. Я ТЕПЕРЬ МОГУ ВСЕ, АБСОЛЮТНО ВСЕ!!!...')
                time.sleep(10)    
                choise4 = input('Плохая погода так и нагоняла мрачной атмосферы в этот день. Арсений явно не в разуме, если конечно его можно так назвать, но... За злым монстром прячется обычный пацан, который лишь желал научиться программированию на питоне в считанные секунды. Короче, его надо привести в порядок, но это пока первая часть, дальше будет интереснее, поэтому жди продолжения)) Это НЕ КОНЕЦ')
            elif choise3 == 'нет':
                print('Решив встать самостоятельно вы еще раз оглянули это место. Здесь попрежнему идет дождь, а молнии бьют где-то далеко всё чаще и чаще.')
                time.sleep(5)
                print('Ты протянул свою руку человеку в черном. Он поднял вас резким движением и спросил:')
                time.sleep(6)
                print('- Ты как? Все в порядке? Можешь меня не бояться, я не причиню тебе зла.')
                time.sleep(6)
                print('Все хорошо')
                time.sleep(3)
                print('- Ладно... Ты как попал сюда? Что ты вообще тут делаешь?')    
                time.sleep(3)
                print('- Я сам не понял как здесь оказался, помню, только, как писал код, а затем просто уснул.')
                time.sleep(6)
                print('- Ну ты даешь... Ладно, здесь и не такое случалось.')    
                time.sleep(3)
                print('- А что здесь случилось-то?') 
                time.sleep(3)
                print('- Хр... Дай расскажу все, но только спрошу как тебя зовут.')
                time.sleep(6)
                print(f'- {name}')     
                time.sleep(3)
                print('- Чтож, мое имя Михаил, но можешь звать просто Миша, и с моей группой произошло просто нечто... Один из учеников решил познать полностью программирование на Python, но... Это того не стоило. Он реально попробовал код, и когда он его прожевал, в него вселился какой-то монстр. Он начал трепать все наши коды, испугал всех одногруппников, от чего все разбежались, он написал программу на виртуальной клавиатуре чтобы пошел дождь с большими тучами, которые закрыли нам небо. Теперь я брожу в поисках своих учеников, а он... Арсений, тот монстр, испарился, но я не уверен, что он пропал. Он поджидает момента чтобы напасть, ведь теперь он полностью познал программирование на питоне и...')
                time.sleep(28)
                print('Не успел Михаил договорить, как большущая молния ударила по некому коду, прогремел взрыв, и тут показался он... Огромное существо, ливитирующее в воздхе, представляющее из себя некую черную массу, расхохоталось во весь голос, что молния снова ударила, но уже ближе к тебе.')    
                time.sleep(10)
                print('- КАК ЖЕ ВЫ ГЛУПЫ, ХРУПКИЕ СОЗДАНИЯ, ВЫ ПРОСТО НЕ ПОНИМАЕТЕ, ЧЕГО Я ДОБИЛСЯ. Я ТЕПЕРЬ МОГУ ВСЕ, АБСОЛЮТНО ВСЕ!!!...')
                time.sleep(10)    
                choise4 = print('Плохая погода так и нагоняла мрачной атмосферы в этот день. Арсений явно не в разуме, если конечно его можно так назвать, но... За злым монстром прячется обычный пацан, который лишь желал научиться программированию на питоне в считанные секунды. Короче, его надо привести в порядок, но это пока первая часть, дальше будет интереснее, поэтому жди продолжения)) Это НЕ КОНЕЦ')
elif floor == 2:
    print('Дописывая очередной код ты не уследила за временем и сама не заметила, как закрыла глаза, а затем и вовсе уснула. Очнувшись от щекотных ударов по твоей щеке, что позже, как оказалось, это был долждь, ты огляделась по сторонам и, как оказалось, попала в какую-то пустошь. Чтож, удачи тебе!')
    time.sleep(15)
    print('...')
    time.sleep(2)         
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)              
    choise1 = input('''Дождь с молниями, никого в округе. Какая-то черная темень, равнина с какими то огрызками чего-то. Все это очень пугает, а огрызки напоминают код. Ты шла по развалившимся кодам, которые кто-то погрыз, попробуешь разобраться в коде?''')
    if choise1 == 'да':
        choise2 = input('В попытках разобраться в коде ты ничего не поняла, но зато на тебя кто-то идёт, окутанный в черные лохмотья и весь истрепанный, будешь убегать?')
    elif choise1 == 'нет':
        choise2 = input('Ты решила не разбираться в коде, но теперь твоему взору открылось еще больше кодов...и все они тоже избиты и потрёпаны. Вдруг среди них вышел человек в черной мантии, идущий прямо на тебя и махая тебе рукой. Будешь убегать?')               
        if choise2 == 'да':
            choise3 = input('Испугавшись человека в черном ты начала убегать, но споткнулась об камень, упала и потерял сознание... Очнулась ты лишь спустя некоторое время, услышав рядом шаги и хруст веток под звуки капающего дождя.')
            time.sleep(7)
            print('- Ты как?')
            time.sleep(2)
            print('- Вы кто?')
            time.sleep(2)
            choise3 = input('Перед вами стоял тот самый человек в черном, от которого вы решили убежать. На лицо ему 23 года, кудрявые волосы и утомленный вид лица. Он протягивает тебе руку. Протянуть в ответ свою руку?')
        elif choise2 == 'нет':
            choise3 = input('Поняв, что человек не представляет из себя опасности, ты пошла к нему навстречу, но тут молния ударила прям рядом с вами. Успев среагировать ты отпрыгнула прямо в остатки кода и по вам ударило током... Странно... К вам подошел тот самый человек. Он протягивает вам руку чтобы вы встали, примите его помощь?')   
            if choise3 == 'да':
                print('Ты протянула свою руку человеку в черном. Он поднял вас резким движением и спросил:')
                time.sleep(5)
                print('- Ты как попала сюда? Что ты вообще тут делаешь?')    
                time.sleep(3)
                print('- Я сама не поняла как здесь оказалась, помню, только, как писала код, а затем просто уснула.')
                time.sleep(5)
                print('- Ну ты даешь... Ладно, здесь и не такое случалось.')    
                time.sleep(3)
                print('- А что здесь случилось-то?') 
                time.sleep(3)
                print('- Хр... Дай расскажу все, но только спрошу как тебя зовут.')
                time.sleep(3)
                print(f'- {name}')     
                time.sleep(3)
                print('- Чтож, мое имя Михаил, но можешь звать просто Миша, и с моей группой произошло просто нечто... Один из учеников решил познать полностью программирование на Python, но... Это того не стоило. Он реально попробовал код, и когда он его прожевал, в него вселился какой-то монстр. Он начал трепать все наши коды, испугал всех одногруппников, от чего все разбежались, он написал программу на виртуальной клавиатуре чтобы пошел дождь с большими тучами, которые закрыли нам небо. Теперь я брожу в поисках своих учеников, а он... Арсений, тот монстр, испарился, но я не уверен, что он пропал. Он поджидает момента чтобы напасть, ведь теперь он полностью познал программирование на питоне и...')
                time.sleep(26)
                print('Не успел Михаил договорить, как большущая молния ударила по некому коду, прогремел взрыв, и тут показался он... Огромное существо, ливитирующее в воздхе, представляющее из себя некую черную массу, расхохоталось во весь голос, что молния снова ударила, но уже ближе к тебе.')    
                time.sleep(10)
                print('- КАК ЖЕ ВЫ ГЛУПЫ, ХРУПКИЕ СОЗДАНИЯ, ВЫ ПРОСТО НЕ ПОНИМАЕТЕ, ЧЕГО Я ДОБИЛСЯ. Я ТЕПЕРЬ МОГУ ВСЕ, АБСОЛЮТНО ВСЕ!!!...')
                time.sleep(10)    
                choise4 = input('Плохая погода так и нагоняла мрачной атмосферы в этот день. Арсений явно не в разуме, если конечно его можно так назвать, но... За злым монстром прячется обычный пацан, который лишь желал научиться программированию на питоне в считанные секунды. Короче, его надо привести в порядок, но это пока первая часть, дальше будет интереснее, поэтому жди продолжения)) Это НЕ КОНЕЦ')
            elif choise3 == 'нет':
                print('Решив встать самостоятельно вы еще раз оглянули это место. Здесь попрежнему идет дождь, а молнии бьют где-то далеко всё чаще и чаще.')
                time.sleep(7)
                print('Ты протянула свою руку человеку в черном. Он поднял вас резким движением и спросил:')
                time.sleep(6)
                print('- Ты как? Все в порядке? Можешь меня не бояться, я не причиню тебе зла.')
                time.sleep(6)
                print('Все хорошо')
                time.sleep(3)
                print('- Ладно... Ты как попала сюда? Что ты вообще тут делаешь?')    
                time.sleep(3)
                print('- Я сама не поняла как здесь оказалась, помню, только, как писала код, а затем просто уснула.')
                time.sleep(6)
                print('- Ну ты даешь... Ладно, здесь и не такое случалось.')    
                time.sleep(3)
                print('- А что здесь случилось-то?') 
                time.sleep(3)
                print('- Хр... Дай расскажу все, но только спрошу как тебя зовут.')
                time.sleep(5)
                print(f'- {name}')     
                time.sleep(3)
                print('- Чтож, мое имя Михаил, но можешь звать просто Миша, и с моей группой произошло просто нечто... Один из учеников решил познать полностью программирование на Python, но... Это того не стоило. Он реально попробовал код, и когда он его прожевал, в него вселился какой-то монстр. Он начал трепать все наши коды, испугал всех одногруппников, от чего все разбежались, он написал программу на виртуальной клавиатуре чтобы пошел дождь с большими тучами, которые закрыли нам небо. Теперь я брожу в поисках своих учеников, а он... Арсений, тот монстр, испарился, но я не уверен, что он пропал. Он поджидает момента чтобы напасть, ведь теперь он полностью познал программирование на питоне и...')
                time.sleep(26)
                print('Не успел Михаил договорить, как большущая молния ударила по некому коду, прогремел взрыв, и тут показался он... Огромное существо, ливитирующее в воздхе, представляющее из себя некую черную массу, расхохоталось во весь голос, что молния снова ударила, но уже ближе к тебе.')    
                time.sleep(10)
                print('- КАК ЖЕ ВЫ ГЛУПЫ, ХРУПКИЕ СОЗДАНИЯ, ВЫ ПРОСТО НЕ ПОНИМАЕТЕ, ЧЕГО Я ДОБИЛСЯ. Я ТЕПЕРЬ МОГУ ВСЕ, АБСОЛЮТНО ВСЕ!!!...')
                time.sleep(10)    
                choise4 = print('Плохая погода так и нагоняла мрачной атмосферы в этот день. Арсений явно не в разуме, если конечно его можно так назвать, но... За злым монстром прячется обычный пацан, который лишь желал научиться программированию на питоне в считанные секунды. Короче, его надо привести в порядок, но это пока первая часть, дальше будет интереснее, поэтому жди продолжения)) Это НЕ КОНЕЦ')

  