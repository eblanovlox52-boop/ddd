from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

TOKEN = "8774284929:AAE_GuhHr0jan3J6r4RcVQZ5hMDukW0RTXs"
ADMIN_ID = 8519899945

# Хранилище отзывов и топа (в реальном проекте лучше использовать БД)
reviews_list = []
top_users = {}

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("⭐ ЗВЁЗДЫ", callback_data="cat_stars")],
        [InlineKeyboardButton("🖼 NFT", callback_data="cat_nft")],
        [InlineKeyboardButton("🏠 АРЕНДА NFT", callback_data="cat_rent")],
        [InlineKeyboardButton("🎁 ПОДАРКИ", callback_data="cat_gifts")],
        [InlineKeyboardButton("💎 TON", callback_data="cat_ton")],
        [InlineKeyboardButton("👑 PREMIUM", callback_data="cat_premium")],
        [InlineKeyboardButton("🎓 ОСИНТ", callback_data="cat_osint")],
        [InlineKeyboardButton("🔒 ДЭФ", callback_data="cat_def")],
        [InlineKeyboardButton("⭐ ОТЗЫВЫ", callback_data="reviews")],
        [InlineKeyboardButton("📞 ПОДДЕРЖКА", callback_data="support")],
        [InlineKeyboardButton("👤 ПРОФИЛЬ", callback_data="profile")],
        [InlineKeyboardButton("🏆 ТОП КЛИЕНТОВ", callback_data="top")],
        [InlineKeyboardButton("❤️ J", callback_data="fun")]
    ]
    
    await update.message.reply_text(
        "╔══════════════════════════════════╗\n"
        "║     ✨ ДОБРО ПОЖАЛОВАТЬ ✨        ║\n"
        "║         GRAVINDES STORE           ║\n"
        "╚══════════════════════════════════╝\n\n"
        "🔥 САМЫЕ НИЗКИЕ ЦЕНЫ!\n\n"
        "👤 Владелец: @Gravindes\n"
        "⭐ 1000+ довольных клиентов\n\n"
        "👇 ВЫБЕРИ КАТЕГОРИЮ 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    
    if query.data == "back":
        await start(update, context)
        return
    
    # ========== КАТЕГОРИИ ТОВАРОВ ==========
    if query.data == "cat_stars":
        keyboard = [[InlineKeyboardButton(f"{n}⭐ - {p}₽", callback_data=f"buy_{n}") for n, p in [(100,110),(150,160),(200,250),(250,270),(300,350)]] + [[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]
        await query.edit_message_text("⭐ ЗВЁЗДЫ\n\nВыбери количество:", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    
    if query.data == "cat_nft":
        keyboard = [
            [InlineKeyboardButton("🖼 Обычный - 400₽", callback_data="buy_nft_common")],
            [InlineKeyboardButton("🖼 Обычный+ - 700₽", callback_data="buy_nft_plus")],
            [InlineKeyboardButton("🖼 Обычный++ - 1000₽", callback_data="buy_nft_pro")],
            [InlineKeyboardButton("🎨 Редкий - 1500₽", callback_data="buy_nft_rare")],
            [InlineKeyboardButton("👑 Легендарный - 2000₽", callback_data="buy_nft_legend")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("🖼 NFT\n\nВыбери NFT:", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    
    if query.data == "cat_rent":
        keyboard = [
            [InlineKeyboardButton("🏠 7 дней - 100⭐", callback_data="rent_7d")],
            [InlineKeyboardButton("🏠 30 дней - 300⭐", callback_data="rent_30d")],
            [InlineKeyboardButton("🏠 90 дней - 700⭐", callback_data="rent_90d")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("🏠 АРЕНДА NFT\n\nВыбери срок:", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    
    if query.data == "cat_gifts":
        keyboard = [
            [InlineKeyboardButton("🎁 Обычный - 400₽", callback_data="gift_common")],
            [InlineKeyboardButton("🎁 Улучшенный - 700₽", callback_data="gift_rare")],
            [InlineKeyboardButton("🎁 Премиум - 1000₽", callback_data="gift_premium")],
            [InlineKeyboardButton("🎁 Редкий - 1500₽", callback_data="gift_epic")],
[InlineKeyboardButton("🎁 Легендарный - 2000₽", callback_data="gift_legend")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("🎁 ПОДАРКИ\n\nВыбери подарок:", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    
    if query.data == "cat_ton":
        keyboard = [
            [InlineKeyboardButton("💎 1 TON - 300₽", callback_data="ton_1")],
            [InlineKeyboardButton("💎 5 TON - 1450₽", callback_data="ton_5")],
            [InlineKeyboardButton("💎 10 TON - 2800₽", callback_data="ton_10")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("💎 TON\n\nВыбери количество:", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    
    if query.data == "cat_premium":
        keyboard = [
            [InlineKeyboardButton("👑 1 месяц - 250₽", callback_data="prem_1m")],
            [InlineKeyboardButton("👑 3 месяца - 700₽", callback_data="prem_3m")],
            [InlineKeyboardButton("👑 6 месяцев - 1300₽", callback_data="prem_6m")],
            [InlineKeyboardButton("👑 12 месяцев - 2500₽", callback_data="prem_12m")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("👑 PREMIUM\n\nВыбери срок:", reply_markup=InlineKeyboardMarkup(keyboard))
        return
    
    if query.data == "cat_osint":
        await query.edit_message_text(
            "🎓 ОБУЧЕНИЕ ОСИНТ\n\n"
            "Полный курс по OSINT\n"
            "💰 ЦЕНА: 1500₽\n\n"
            "💳 ОПЛАТА: Т-Банк 2200 7021 4230 2590\n\n"
            "✅ После оплаты пришли чек @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return
    
    if query.data == "cat_def":
        await query.edit_message_text(
            "🔒 ДЭФ НАВСЕГДА\n\n"
            "Защита аккаунта навсегда\n"
            "💰 ЦЕНА: 1000₽\n\n"
            "💳 ОПЛАТА: Т-Банк 2200 7021 4230 2590\n\n"
            "✅ После оплаты пришли чек @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return
    
    # ========== ОТЗЫВЫ ==========
    if query.data == "reviews":
        keyboard = [
            [InlineKeyboardButton("✍️ НАПИСАТЬ ОТЗЫВ", callback_data="write_review")],
            [InlineKeyboardButton("⭐ ЧИТАТЬ ОТЗЫВЫ", callback_data="read_reviews")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text(
            "⭐ ОТЗЫВЫ\n\n"
            "Оставь отзыв или почитай чужие\n\n"
            "👇 ВЫБЕРИ ДЕЙСТВИЕ 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return
    
    if query.data == "write_review":
        context.user_data["awaiting_review"] = True
        await query.edit_message_text(
            "✍️ НАПИСАТЬ ОТЗЫВ\n\n"
            "Напиши свой отзыв одним сообщением.\n\n"
            "📝 Пример: «Отличный магазин! Всё быстро!»\n\n"
            "✅ Отправь сообщение прямо сейчас!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="reviews")]])
        )
        return
    
    if query.data == "read_reviews":
        if reviews_list:
            reviews_text = "\n\n".join(reviews_list[-5:])  # последние 5 отзывов
            await query.edit_message_text(
                f"⭐ ОТЗЫВЫ КЛИЕНТОВ ⭐\n\n{reviews_text}\n\n─────────────────\n📝 Хочешь оставить отзыв? Нажми «Написать отзыв»",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="reviews")]])
            )
        else:
            await query.edit_message_text(
                "⭐ ОТЗЫВЫ КЛИЕНТОВ ⭐\n\nПока нет отзывов. Будь первым! ✍️\n\nНапиши свой отзыв — возможно, получишь скидку!",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="reviews")]])
            )
        return
# ========== ПОДДЕРЖКА ==========
    if query.data == "support":
        await query.edit_message_text(
            "📞 ПОДДЕРЖКА\n\n👤 @Gravindes\n⏰ 24/7\n⚡ Ответ 2-5 минут\n\n🔒 Гарантия возврата средств",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return
    
    # ========== ПРОФИЛЬ ==========
    if query.data == "profile":
        await query.edit_message_text(
            f"👤 ПРОФИЛЬ\n\n🆔 ID: {user.id}\n📝 Имя: {user.first_name}\n📝 Username: @{user.username if user.username else 'нет'}\n💰 Баланс: 0₽\n\n⭐ Статус: Обычный клиент",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return
    
    # ========== ТОП КЛИЕНТОВ ==========
    if query.data == "top":
        if top_users:
            sorted_top = sorted(top_users.items(), key=lambda x: x[1], reverse=True)[:10]
            top_text = "🏆 ТОП КЛИЕНТОВ 🏆\n\n"
            for i, (uid, amount) in enumerate(sorted_top, 1):
                top_text += f"{i}. @{uid} — {amount}₽\n"
            top_text += "\n🔥 Стань лучшим клиентом! Делай заказы и попади в топ!"
            await query.edit_message_text(
                top_text,
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
            )
        else:
            await query.edit_message_text(
                "🏆 ТОП КЛИЕНТОВ 🏆\n\nПока никого нет. Вы можете занять первое место!\n\n🔥 Делай заказы и попади в топ!",
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
            )
        return
    
    # ========== J ==========
    if query.data == "fun":
        await query.edit_message_text(
            "❤️ J ❤️\n\n@Gravindes желает тебе отличного дня! 🚀",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return
    
    # ========== ОБРАБОТКА ПОКУПОК ==========
    if query.data.startswith(("buy_", "rent_", "gift_", "ton_", "prem_")):
        product_name = query.data
        # Добавляем в топ (увеличиваем сумму покупки)
        username = user.username if user.username else user.first_name
        top_users[username] = top_users.get(username, 0) + 500  # +500₽ за покупку
        
        await query.edit_message_text(
            f"✅ ЗАКАЗ ПРИНЯТ ✅\n\n📦 Товар: {product_name}\n\n"
            f"💳 ОПЛАТА НА КАРТУ:\n🏦 Т-Банк\n💳 2200 7021 4230 2590\n\n"
            f"✅ После оплаты пришли чек @Gravindes\n\n"
            f"⚡ Доставка 1-5 минут\n🔒 Гарантия возврата\n\n❤️ Спасибо за заказ!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 В МЕНЮ", callback_data="back")]])
        )
        await context.bot.send_message(ADMIN_ID, f"🛒 НОВЫЙ ЗАКАЗ!\n📦 {product_name}\n👤 {user.first_name}\n🆔 {user.id}\n📝 @{username}")
        return

# Обработчик сообщений (для отзывов)
async def handle_message(update: Update, context):
    user = update.effective_user
    text = update.message.text
    
    if context.user_data.get("awaiting_review"):
        username = user.username if user.username else user.first_name
        reviews_list.append(f"«{text}» — @{username}")
        await context.bot.send_message(ADMIN_ID, f"⭐ НОВЫЙ ОТЗЫВ!\n👤 {user.first_name}\n📝 @{username}\n📝 {text}")
        await update.message.reply_text(
            "✅ СПАСИБО ЗА ОТЗЫВ!\n\n"
            "Твой отзыв отправлен владельцу.\n"
            "Лучшие отзывы публикуются в разделе «Читать отзывы».\n\n"
            "👇 Нажми /start чтобы продолжить"
        )
        context.user_data["awaiting_review"] = False
        return
    
    await update.message.reply_text(
        "🤖 Я бот-магазин GRAVINDES STORE\n\n"
        "📞 Для заказа товаров используй кнопки меню\n"
        "👤 Связь с продавцом: @Gravindes\n\n"
        "👇 Нажми /start чтобы открыть меню"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.
add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("✅ GRAVINDES STORE ЗАПУЩЕН!")
app.run_polling()

