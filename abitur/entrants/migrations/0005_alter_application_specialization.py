# Generated by Django 4.2.7 on 2023-12-16 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrants', '0004_alter_application_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='specialization',
            field=models.CharField(choices=[('АТФ', (('АТФ', 'Автомобили, тракторы, мобильные и технологические комплексы (Автоматизированное проектирование автомобилей)'), ('АТФ', 'Автомобили, тракторы, мобильные и технологические комплексы (Автомобилестроение(электроника))'), ('АТФ', 'Автомобили, тракторы, мобильные и технологические комплексы (Грузовые и легковые автомобили)'), ('АТФ', 'Автомобили, тракторы, мобильные и технологические комплексы (Колесные машины и специализированное транспортно-технологическое оборудование и системы)'), ('АТФ', 'Автомобили, тракторы, мобильные и технологические комплексы (Тракторы и мобильные комплексы)'), ('АТФ', 'Автомобили, тракторы, мобильные и технологические комплексы (Электрические и автономные транспортные средства)'), ('АТФ', 'Гидропневмосистемы мобильных и технологических машин и оборудования (Инжиниринг гидравлических и пневматических систем мобильных машин и оборудования)'), ('АТФ', 'Силовые установки (Поршневые двигатели внутреннего сгорания)'), ('АТФ', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Техническая эксплуатация автомобилей и автосервис)'), ('АТФ', 'Технологии транспортных процессов (Организация перевозок и управление на автомобильном и городском транспорте)'), ('АТФ', 'Эксплуатация дорожно-транспортной инфраструктуры (Интеллектуальная дорожно-транспортная инфраструктура)'), ('АТФ', 'Организация дорожного движения и транспортное планирование (Организация и безопасность дорожного движения)'), ('АТФ', 'Инженерная экономика (Транспорт)'), ('АТФ', 'Транспортная логистика (Транспортно-логистические системы и управление цепями поставок)'))), ('ФИТР', (('ФИТР', 'Программная инженерия'), ('ФИТР', 'Автоматизация технологических процессов и производств (Автоматизированные электроприводы)'), ('ФИТР', 'Робототехнические системы (Промышленные роботы и робототехнические комплексы)'), ('ФИТР', 'Информационные системы и технологии (Информационные системы и технологии в проектировании и производстве)'), ('ФИТР', 'Автоматизация технологических процессов и производств (Автоматизация технологических процессов и производств в энергетике)'), ('ФИТР', 'Автоматизация технологических процессов и производств (Автоматизация технологических процессов и производств в приборостроении и радиоэлектронике)'))), ('ФГДЭ', (('ФГДЭ', 'Машины и оборудование для горнодобывающих производств (Горная электромеханика)'), ('ФГДЭ', 'Разработка месторождений полезных ископаемых (Открытые горные работы)'), ('ФГДЭ', 'Разработка месторождений полезных ископаемых (Подземные горные работы)'))), ('МСФ', (('МСФ', 'Автоматизация технологических процессов и производств (Интеллектуальные приборы, машины и производства)'), ('МСФ', 'Автоматизация технологических процессов и производств (Компьютерная мехатроника)'), ('МСФ', 'Автоматизация технологических процессов и производств (Цифровое машиностроительное производство)'), ('МСФ', 'Технология машиностроения, металлорежущие станки и инструменты (Высокоэнергетические технологии обработки деталей)'), ('МСФ', 'Технология машиностроения, металлорежущие станки и инструменты (Инжиниринг технологического оборудования)'), ('МСФ', 'Технология машиностроения, металлорежущие станки и инструменты (Инструментальное обеспечение производства)'), ('МСФ', 'Технология машиностроения, металлорежущие станки и инструменты (Технологическое обеспечение машиностроительного производства)'), ('МСФ', 'Инженерная экономика (Бизнес-процессы промышленных предприятий)'), ('МСФ', 'Инженерная экономика (Цифровое производство)'))), ('МТФ', (('МТФ', 'Технологии высокотемпературной обработки металлов (Инжиниринг технологических процессов в металлургическом производстве)'), ('МТФ', 'Технологии высокотемпературной обработки металлов (Компьютерное проектирование литейных и металлургических процессов)'), ('МТФ', 'Технологии высокотемпературной обработки металлов (Цифровое металловедение и термическая обработка)'), ('МТФ', 'Инженерно-техническое проектирование и производство материалов и изделий из них (Аддитивные технологии в литейном производстве)'), ('МТФ', 'Инженерно-техническое проектирование и производство материалов и изделий из них (Деформационные технологии и оборудование)'), ('МТФ', 'Инженерно-техническое проектирование и производство материалов и изделий из них (Материаловедение в машиностроении)'), ('МТФ', 'Инженерно-техническое проектирование и производство материалов и изделий из них (Машины и технология литейного производства)'), ('МТФ', 'Инженерно-техническое проектирование и производство материалов и изделий из них (Оборудование и технология сварочного производства)'))), ('ФММП', (('ФММП', 'Экономика и управление (Экономика и управление на предприятии промышленности)'), ('ФММП', 'Бизнес-администрирование (Бизнес-администрирование организации)'), ('ФММП', 'Маркетинг (Маркетинг предприятий промышленности)'), ('ФММП', 'Инженерная экономика (Инновационные проекты на промышленном предприятии)'), ('ФММП', 'Инженерная экономика (Организация внешнеэкономической деятельности обрабатывающей промышленности)'), ('ФММП', 'Инженерная экономика (Управление дизайн-проектами на промышленном предприятии)'), ('ФММП', 'Оборудование и технологии упаковочного производства, торговли и экспозиционно-рекламных объектов (Торговое оборудование и технологии)'))), ('ЭФ', (('ЭФ', 'Электроэнергетика и электротехника (Релейная защита и автоматика)'), ('ЭФ', 'Электроэнергетика и электротехника (Электрические установки, электростанции и подстанции)'), ('ЭФ', 'Электроэнергетика и электротехника (Электроснабжение)'), ('ЭФ', 'Электроэнергетика и электротехника (Электроэнергетические системы и сети)'), ('ЭФ', 'Теплоэнергетика и теплотехника (Автоматизация и управление теплоэнергетическими процессами)'), ('ЭФ', 'Теплоэнергетика и теплотехника (Промышленная теплоэнергетика)'), ('ЭФ', 'Теплоэнергетика и теплотехника (Тепловые электрические станции)'), ('ЭФ', 'Проектирование и эксплуатация атомных электрических станций'), ('ЭФ', 'Инженерная экономика (Электроэнергетика и теплоэнергетика)\t'))), ('ФТУГ', (('ФТУГ', 'Экономика и управление'), ('ФТУГ', 'Менеджмент'), ('ФТУГ', 'Инженерная экономика (Экономика и цифровые технологии на промышленном предприятии)'), ('ФТУГ', 'Таможенное дело'), ('ФТУГ', 'Оборудование и технологии упаковочного производства, торговли и экспозиционно-рекламных объектов (Упаковочное производство)'), ('ФТУГ', 'Оборудование и технологии вакуумной, компрессорной и низкотемпературной техники (Низкотемпературная техника)'), ('ФТУГ', 'Инженерная экономика (Экономика и экономическая безопасность промышленного предприятия)'), ('ФТУГ', 'Теплоэнергетика и теплотехника (Энергоэффективные технологии и энергетический менеджмент)'))), ('ИПФ', (('ИПФ', 'Оборудование и технологии вакуумной, компрессорной и низкотемпературной техники (Вакуумная и компрессорная техника)'), ('ИПФ', 'Инженерно-педагогическая деятельность (Автомобилестроение)'), ('ИПФ', 'Инженерно-педагогическая деятельность (Машиностроение)'), ('ИПФ', 'Инженерно-педагогическая деятельность (Прикладное программирование)'))), ('ФЭС', (('ФЭС', 'Водные транспортные средства (Судостроение и техническая эксплуатация водного транспорта)'), ('ФЭС', 'Строительство зданий и сооружений (Гидротехническое строительство)'), ('ФЭС', 'Строительство зданий и сооружений (Строительство зданий и сооружений тепловой и атомной энергетики)'), ('ФЭС', 'Инженерные сети, оборудование зданий и сооружений (Водоснабжение, водоотведение и охрана водных ресурсов)'), ('ФЭС', 'Инженерные сети, оборудование зданий и сооружений (Теплогазоснабжение, вентиляция и охрана воздушного бассейна)'), ('ФЭС', 'Инженерная экономика (Коммунальное и водное хозяйство)'))), ('СФ', (('СФ', 'Техническая эксплуатация зданий и сооружений (Эксплуатация объектов жилищно-коммунального хозяйства)'), ('СФ', 'Экспертиза и управление недвижимостью'), ('СФ', 'Строительство зданий и сооружений (Производство строительных изделий и конструкций)'), ('СФ', 'Строительство зданий и сооружений (Промышленное и гражданское строительство)'), ('СФ', 'Инженерная экономика (Архитектура, строительство и экономика недвижимости)'))), ('ПСФ', (('ПСФ', 'Метрология, стандартизация и контроль качества (Метрология,стандартизация и контроль качества в машиностроении и приборостроении)'), ('ПСФ', 'Информационно-измерительные приборы и системы (Информационно-измерительная техника и технологии)'), ('ПСФ', 'Информационно-измерительные приборы и системы (Информационные системы и технология неразрушающего контроля и диагностики)'), ('ПСФ', 'Информационно-измерительные приборы и системы (Механические и электромеханические приборы и системы)'), ('ПСФ', 'Информационно-измерительные приборы и системы (Технология и оборудование ювелирного производства)'), ('ПСФ', 'Оптико-электронная и лазерная техника (Оптические и оптико-электронные приборы и комплексы)'), ('ПСФ', 'Технические системы обеспечения безопасности'), ('ПСФ', 'Биомедицинская инженерия (Технические средства диагностики и лечения)\t'), ('ПСФ', 'Микро- и наносистемная техника'))), ('ФТК', (('ФТК', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Эксплуатация и технический сервис подьемно-транспортных, дорожно-строительных и технологических машин строительного комплекса)'), ('ФТК', 'Геодезия'), ('ФТК', 'Строительство транспортных коммуникаций (Автомобильные дороги)'), ('ФТК', 'Строительство транспортных коммуникаций (Мосты, транспортные тоннели и метрополитены)'))), ('СТФ', (('СТФ', 'Спортивная инженерия (Проектирование и производство спортивной техники)'), ('СТФ', 'Спортивная инженерия (Техническое обеспечение эксплуатации спортивных объектов)'))), ('ВТФ', (('ВТФ', 'Экономика и управление (Финансовое обеспечение и экономика боевой и хозяйственной деятельности войск) - ВВ'), ('ВТФ', 'Экономика и управление (Финансовое обеспечение и экономика боевой и хозяйственной деятельности войск) - ВС муж. пола'), ('ВТФ', 'Экономика и управление (Финансовое обеспечение и экономика боевой и хозяйственной деятельности войск) - ВС жен. пола'), ('ВТФ', 'Экономика и управление (Финансовое обеспечение и экономика боевой и хозяйственной деятельности войск) -ГПК'))), ('ВТФ ВСРБ', (('ВТФ ВСРБ', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Дорожно-строительные машины и оборудование специального назначения)'), ('ВТФ ВСРБ', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Техническая эксплуатация автомобильной техники)'), ('ВТФ ВСРБ', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Эксплуатация и ремонт многоцелевых гусеничных и колесных машин)'), ('ВТФ ВСРБ', 'Строительство зданий и сооружений (Промышленное и военное строительство)'))), ('ВТФ ГПК', (('ВТФ ГПК', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Дорожно-строительные машины и оборудование специального назначения)'), ('ВТФ ГПК', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Техническая эксплуатация автомобильной техники)'), ('ВТФ ГПК', 'Строительство зданий и сооружений (Промышленное и военное строительство)'))), ('ВТФ ВС', (('ВТФ ВС', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Дорожно-строительные машины и оборудование специального назначения)'), ('ВТФ ВС', 'Эксплуатация наземных транспортных и технологических машин и комплексов (Техническая эксплуатация автомобильной техники)'), ('ВТФ ВС', 'Строительство зданий и сооружений (Промышленное и военное строительство)')))], default='Не выбрано', max_length=255, verbose_name='Специальность'),
        ),
    ]