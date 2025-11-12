# Avito-Feed-Processor

## Description

This Python tool automates the process of bulk uploading product listings to Avito (a leading Russian classifieds platform). It transforms raw product data from a client's e-commerce feed into formatted XML files ready for Avito's bulk upload system.

## Key Functionalities

*   **Data Processing:** Reads and modifies product data from the client's e-commerce feed.
*   **Intermediate XLSX Export:** Generates intermediate Excel files for data analysis and manual adjustments by managers.
*   **Promotion-Specific Files:** Creates specialized XLSX files for marketing campaigns like "Хватамба".
*   **XML Generation:** Produces final XML feed files compatible with Avito's bulk upload for 20 different client accounts and cities.
*   **Telegram Notifications:** Includes a monitoring script that sends status updates to a dedicated Telegram channel. It notifies about the script's start, successful completion of XML generation, and any critical errors, keeping the team informed.

## Tech Stack

*   Python
*   OpenPyXL
*   XML (lxml/ElementTree)
*   bs4
*   Telegram Bot API (for notifications)

## Project Context & Challenges

This project was developed and maintained solo over two years, directly adapting to evolving business requirements. It ran reliably on a Linux server for the entire duration. As a result, its architecture reflects iterative development rather than a top-down design. The initial plan included a full rewrite using the official Avito API and a refined architecture; however, the client opted to continue using this stable, production-proven version.

## Why It's Here

This repository showcases my ability to:

*   Develop long-term, business-critical automation tools that run reliably in a production environment (Linux server).
*   Implement monitoring and alerting systems (via Telegram Bot API) to keep stakeholders informed.
*   Effectively work directly with clients and adapt to their changing needs.
*   Process and transform complex e-commerce data.
*   Integrate with third-party platforms via their data formats (XML, XLSX).

---

## Описание

Данный инструмент на Python автоматизирует процесс массовой выгрузки товарных объявлений на Avito. Он преобразует сырые данные из фида интернет-магазина клиента в форматированные XML-файлы, готовые для автозагрузки в систему Avito.

## Ключевые функции

*   **Обработка данных:** Чтение и модификация данных товаров из фида интернет-магазина.
*   **Промежуточный экспорт в XLSX:** Генерация промежуточных Excel-файлов для анализа данных и ручного исправления менеджерами.
*   **Файлы для акций:** Создание специализированных XLSX-файлов для маркетинговых кампаний, таких как "Хватамба".
*   **Генерация XML:** Создание финальных XML-фидов, совместимых с системой массовой загрузки Avito для 20 различных личных кабинетов и городов клиента.
*   **Telegram-уведомления:** Включен скрипт мониторинга, который отправляет статусы выполнения в выделенный Telegram-канал. Он сообщает о начале работы скрипта, успешном завершении формирования XML-файлов или о критических ошибках, держа команду в курсе событий.

## Стек технологий

*   Python
*   OpenPyXL
*   XML (lxml/ElementTree)
*   bs4
*   Telegram Bot API (для уведомлений)

## Контекст проекта и вызовы

Этот проект разрабатывался и поддерживался в одиночку в течение двух лет, постоянно адаптируясь под бизнес-требования клиента. Программа стабильно работала на Linux-сервере на протяжении всего срока эксплуатации и скорее всего работает до сих пор. В результате, его архитектура отражает итеративную разработку, а не строгое проектное планирование. Изначальный план включал полную переработку с использованием официального API Avito и переработанной архитектуры, однако клиент предпочел остаться на старой версии.

## Почему этот проект здесь

Этот репозиторий демонстрирует мои способности:

*   Разрабатывать долгосрочные, бизнес-критичные инструменты автоматизации, стабильно работающие в production-окружении (Linux server).
*   Внедрять системы мониторинга и оповещения (через Telegram Bot API) для информирования стейкхолдеров.
*   Эффективно работать напрямую с клиентами и адаптироваться к их меняющимся потребностям.
*   Обрабатывать и преобразовывать сложные данные из e-commerce.
*   Интегрироваться со сторонними платформами через их форматы данных (XML, XLSX).