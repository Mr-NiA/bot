from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
import time
import random

token = "0c9b03301bfe63ff9189fd733be9aa1928f72e6a0238534a698d8d7cf5520e326134cf7130319c26aa3d3"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)
    if response == 'меню':
        keyboard.add_button('Купить', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('О боте', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_openlink_button('Сделанные заказы', "https://yadi.sk/d/ts1Z2bFrmuvARA")
        keyboard.add_line()
        keyboard.add_openlink_button('Для связи', "https://vk.com/n__i__a")

    elif response == 'купить':

        keyboard.add_button('Купоны', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Через посредника', color=VkKeyboardColor.PRIMARY)
        keyboard.add_line()
        keyboard.add_button('Цена', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Правила', color=VkKeyboardColor.NEGATIVE)
        keyboard.add_line()
        keyboard.add_button('Меню', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Оплатить', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard

def send_message(vk_session, id_type, id, message = None, attachment = None, keyboard = None) :
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        print(str(datetime.strftime(datetime.now(), "%H:%M:%S")))
        print(str(event.text))
        print(event.user_id)
        response = event.text.lower()
        keyboard = create_keyboard(response)
        if event.from_user and not event.from_me:
            if response == 'меню':
                send_message(vk_session, 'user_id', event.user_id, message= '==========📖Меню📖==========', keyboard=keyboard)
            elif response == 'цена':
                send_message(vk_session, 'user_id', event.user_id, message= '==========🎲Купоны🎲=========='
                                                                            '\nКолво - цена в рублях'
                                                                            '\n🔸1 - 130 🔹'
                                                                            '\n🔸2 - 250 🔹'
                                                                            '\n🔸3 - 380 🔹'
                                                                            '\n🔸4 - 510 🔹'
                                                                            '\n🔸5 - 640 🔹'
                                                                            '\n🔸6 - 760 🔹'
                                                                            '\n🔸7 - 880 🔹'
                                                                            '\n🔸8 - 1000🔹'
                                                                            '\n🔸9 - 1100🔹'
                                                                            '\n🔸10-1200🔹'
                                                                            '\n\n⚠Можно использовать только один купон одновременно.\n'
                                                                            '\n==🎅Заказ через посредника🎅==\nСкидка 50% - 12% за работу')
            elif response == 'купить':
                send_message(vk_session, 'user_id', event.user_id, message='======📝Выберете услугу📝======', keyboard=keyboard)
            elif response == 'правила':
                send_message(vk_session, 'user_id', event.user_id, message='======❗️Общие условия❗️======'
                                                                           '\n\n❗️3м лицам информацию не передаю (статья 13.11 КоАП РФ, за пренебрежение 152-ФЗ «О персональных данных»).'
                                                                           '\n❗️Не несу ответственности за переход не по ссылкам данного бота, заказ у других людей или переводы не на мои счета.'
                                                                           '\n❗️При попытке обмана, подделывания скринов,деньги не возвращаются.'
                                                                           '\n❗️Никаким разводом на деньги, обманом продавцов,снятия с чужих счетов и подобной чернухойне занимаюсь.'
                                                                           '\n\n====❗️Условия для купонов❗️===='
                                                                           '\n\n❗️Если купон(ы) не приходят в течении пары дней, деньги возвращаются в полном объеме.'
                                                                           '\n❗️Не несу ответственности за ваши действия с купоном, не выдаю замены( если информации в боте недостаточно,лучше лишний раз спросите для уточнения'
                                                                           '\n👉 vk.com/n__i__a )'
                                                                           '\n\n==❗️Условия посредничества❗️=='
                                                                           '\n\n🚧 В случае отмены заказа (продавцом или лично вами), деньги возвращаю в полном объеме в кратчайшие сроки ❗️После отправки товара, отменить заказ будет нельзя.'
                                                                           '\n❗️Не несу ответственности за посылки, отправляемые продавцами.'
                                                                           '\n❗️Если с товаром что-то не так при получении, бывают казусы (не работает или не то количество), пишите мне, я открываю спор.'
                                                                           '\n❗️Возврат средств происходит в том объеме, который предлагает продавец или делается перезаказ.'
                                                                           '\n❗️Вы вправе потребовать переписку с продавцом, и я вам её скину.')
            elif response == 'о боте':
                send_message(vk_session, 'user_id', event.user_id, message='😼В данном боте вы можете купить купоны на 500р для своего аккаунта на AliExpress (можно оплатить до 50%) '
                                                                           'или заказать товар со скидкой 50% до 1000р.')
            elif response == 'купоны':
                send_message(vk_session, 'user_id', event.user_id, message=
'=========💢О купонах💢=========\n\n'
'\n🔹Купон(ы) каждый номиналом 500 рублей.'
'\n🔹Купон(ы) можно приобрести на свой аккаунт AliExpress, если его нет, то можете заказачать через посредника.'
'\n🔹Купон(ы) действительны 14 дней с момента получения.'
'\n🔹После использования купона у вас есть 20 дней, чтобы оплатить товар со скидкой.'
'\n🔹После использования купона, его нельзя будет вернуть, так что не тратьте зря.'
'\n🔹Купон не действует на доставку (но можно выбирать платную),\n поэтому включайте в фильтре *бесплатная доставка*.'
'\n🔹Купон действует как на сумму товаров, так и на одиночные.'
'\n🔹Количество купонов на один аккаунт максимум 10 в месяц.'
'\n🔹Купон может быть применен к товарам и до 1000, оплата также 50% мах.'
'\n✅Рекомендую покупать в пределах тысячи, иначе теряете выгоду.'
'\n☣️Доп информацию вы получите после оплаты😌')
            elif response == 'оплатить':
                send_message(vk_session, 'user_id', event.user_id, message=
'\n========💵Реквизиты💵========\n\n'
'‼️Оплачивая, вы принимаете условия в разделе 🗒Правила🗒\n'
'✅Сбербанк 5469520025312018\n'
'✅QIWI qiwi.com/n/MRNIAX\n'
'✅ЯД money.yandex.ru/to/4100115148133019\n'
'📝В комментарии укажите ваш id vk или ссылку, а также сообщите 👉 vk.com/n__i__a об оплате.\n'
'📞После проверки оплаты, вы получите доп инструкции.\n')
            elif response == 'через посредника':
                send_message(vk_session, 'user_id', event.user_id, message=
'🎅Заказ через посредника (c моих личных аккаунтов) со скидкой 50%\n\n'
'🍿Товаров может быть много, главное, чтобы стоимость любого одного не превышала 1000 (после 1000 скидка мах 500).\n\n'
'\n1️⃣Прежде, чем заказать, вы принимается условия в разделе "Правила", обговаривается товар (присылаете ваши ссылки на товар),'
' далее я пересылаю скриншот со скидкой (бывают случаи, когда скидка достигает 65%) ➖ 12% от цены заказа за работу.'
'\n\n📱Для заказа 👉 vk.com/n__i__a с пометкой "Хочу сделать заказ".\n'
'\nПримеры:\n'
'1000*0.5+1000*0.12 = 620р ваша цена со скидкой (товар за 1000р)\n'
'600*0.62=372р (товар за 600р)\n'
'250*0.62=155р (товар за 250р)\n\n'
'⎥⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎥'
'\n👍Для тех, кому много БуКаВ.\n'
'Я — посредник между вами и вашим заказом для уменьшения стоимость товара, все остальное, как обычно на AliExpress.\n'
'🌊Максимально прозрачный процесс.'
'\n🎫Скрины работ 👉 yadi.sk/d/ts1Z2bFrmuvARA'
'\n📱Для заказа 👉 vk.com/n__i__a с пометкой "Хочу сделать заказ".'
'\n🤔Остались вопросы, читайте дальше.\n'
'⎥⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎥\n'
'\n2️⃣После обговорки заказа, Вы пишите адрес и на кого высылать, скидываете деньги на qiwi/ЯД/сбербанк.онлайн/Paypal/могу выставить счет на любого оператора : МТС, Tele2 и иные (все мои способы оплаты подтверждены паспортом, дабы избежать обмана).\n'
'\n3️⃣Я оплачиваю товар и после того, как будет выдан трек-номер (0-3 дней, как обычно на АлиЭкспересс), я скидываю его вам для удобства отслеживания (бывают посылки без отслеживания).\n'
'\n4️⃣Когда посылка придёт, забираете на почте с паспортом (стандартная процедура получения посылок).\n')
            elif response == '1342865411':
                send_message(vk_session,'user_id', event.user_id, message=
                '\n===⚠Небольшое дополнение⚠===\n'
'\n⚠️Купон возвращается, после отмены всех товаров на которые он применен.\n'
'\n⚠️Что бы купить товар по меньшей цене, чем тысяча, для этого надо набрать товаров, ценой ~1000+, выбрать оплатить наличными, и дальше оплатить.'
'После сформирования заказа, скидка будет распределена на те товары которые выбрали с -50%, оплачивайте (картой или любым другом способом), только те, которые хотите.'
'Такам образом можно добрать товары, если нет 1000.\n'                
'\nТовар для дополнения:'                
'\na.aliexpress.ru/_eNsxbz - наклейки 9 рублей'
'\na.aliexpress.ru/_eLM7Sb - наклейки 61 рубль\n'
'\n⚠Для начисления купонов, скиньте ссылку-приглашение'
'. Как получить?Посмотрите видео 👇'
'\nyadi.sk/i/RzIPyAO2ISjjsg'
'\nВыглядит вот так  👇'
'\nhttps://a.aliexpress.ru/_eP2zCx\n'
'\n✅После его получения скидываете vk.com/n__i__a и ожидаете оплаченное количество купонов.\n'
'\n😬Если возникли какие-то проблемы, пишите 👆\n')
            elif response == 'закрыть':
                send_message(vk_session,'user_id', event.user_id, message= 'Закрыть',keyboard=keyboard)
            elif response == 'если':
                send_message(vk_session,'user_id', event.user_id, message= ' ',keyboard=keyboard)
            elif response == 'да':
                send_message(vk_session, 'user_id', event.user_id, message='купоны')
            elif response == 'нет':
                send_message(vk_session, 'user_id', event.user_id, message='через посредника')
