# DVACHERS Travel

Practical travel guides and independently installable [Agent Skills](https://agentskills.io/). First release: **Indonesia Visa on Arrival (VOA) extension**, eVisa, SIMPONI, GoPay QRIS and refundable onward tickets, with a verified Palembang case.

Проверенный тревел-опыт: инструкции для людей и навыки для AI-ассистентов. Начинаем с **продления VOA в Индонезии**. Одна репа, из которой можно установить только нужные навыки.

[Читать с телефона](https://kostia7alania.ru/dvachers-travel/) · [Гайд в GitHub](skills/indonesia-voa-extension/references/guide.ru.md) · [Предложить исправление](https://github.com/kostia7alania/dvachers-travel/issues/new/choose)

<a id="install"></a>

## Выбрать и установить

Открыть список навыков и выбрать нужные в интерактивном режиме:

```sh
npx skills add kostia7alania/dvachers-travel
```

Посмотреть список без установки:

```sh
npx skills add kostia7alania/dvachers-travel --list
```

Установить только продление индонезийской VOA:

```sh
npx skills add kostia7alania/dvachers-travel --skill indonesia-voa-extension
```

Для Codex во всех проектах:

```sh
npx skills add kostia7alania/dvachers-travel --skill indonesia-voa-extension -a codex -g
```

По умолчанию установка относится к текущему проекту; `-g` устанавливает в каталог пользователя. CLI требует Node.js 22.20 или новее. Когда навыков станет больше, выбирайте их в меню или повторяйте `--skill NAME`. Сейчас опубликован один завершённый навык; пустых навыков для будущих стран нет.

Команды и поддерживаемые клиенты: [Vercel Skills](https://github.com/vercel-labs/skills). Формат навыка не добавляет браузер, почту, календарь или право действовать от вашего имени. Codex использовался в исходном кейсе; работа во всех перечисленных сторонним установщиком клиентах здесь не подтверждена.

## Доступные навыки

| Навык | Что помогает сделать | Проверенный опыт |
| --- | --- | --- |
| [indonesia-voa-extension](skills/indonesia-voa-extension/SKILL.md) | Найти текущий ITK, подготовить документы, проверить офис и оплату, пройти исправление `UPDATE PENDING`, подтвердить новый e-ITK и настроить напоминание об отмене билета | Palembang, октябрь 2026 |

**Indonesia / Bali visa extension:** общая точка входа eVisa одна, но требования конкретного офиса нужно проверять. Наш подтверждённый кейс относится к Palembang. Он не доказывает требования всех офисов Бали, включая Ngurah Rai.

## Без установки, в обычном чате

Откройте [гайд](skills/indonesia-voa-extension/references/guide.ru.md) или [текст для начала чата](chat-starter.ru.md). Его можно читать с телефона и передать своему ассистенту. Доступ к сайту, аккаунтам и инструментам зависит от вашего клиента; текст инструкции сам его не создаёт.

Важное из первого кейса:

- Подача, оплата, явка и выдача нового e-ITK проверяются отдельно. `Paid` не означает, что продление выдали.
- В нашем платёжном меню был SIMPONI. GoPay принял QR после экспорта той же матрицы в PNG с белой рамкой; это один подтверждённый обход, а не универсальная неисправность GoPay.
- Офис запросил один общий PDF через `UPDATE PENDING` → `Main Document`. Состав документов нужно сверять со своим запросом.
- `Refundable` не обещает возврат всей суммы покупки. Проверяются премии, комиссии, способ выплаты и строгий срок запроса.

Подробности, даты и официальные источники находятся в гайде и references. Реальные паспорта, заявки, платёжные коды, QR и чеки в репозиторий не входят.

## Как пополнять

Прошли процедуру или нашли изменение? [Создайте предложение](https://github.com/kostia7alania/dvachers-travel/issues/new/choose): страна, офис, дата, что изменилось, результат и публичный источник. Без номера паспорта, брони, биллинга и личных документов.

Исправления проходят проверку. Официальное правило, личный опыт и непроверенное сообщение сохраняются как разные типы сведений. [Правила вклада](CONTRIBUTING.md).

Новые процедуры будут отдельными навыками в этой репе. Места, карты и истории добавим по мере появления проверенных материалов; готовых списков Google Maps пока нет.

## For English-speaking contributors

The first detailed human guide is in Russian; the agent instructions and evidence references are in English. Contributions and corrections in either language are welcome. Include the country, responsible office, date, observed outcome and a public primary source. Separate official requirements from personal reports. Do not upload identity documents, private account links or payment identifiers.

## Лицензия и поддержка

Собственные тексты и инструкции: [CC BY-SA 4.0](LICENSE.md). Код проверки и оформление сайта: [MIT](LICENSE-CODE). Чужие материалы сохраняют свои условия использования; ссылка на источник не передаёт права на его содержимое.

Это независимый общественный проект, не сервис иммиграции, GoPay или Traveloka. Актуальные требования проверяются по официальным источникам и ответственному офису.
