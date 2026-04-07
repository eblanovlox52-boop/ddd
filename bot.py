from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

TOKEN = "8774284929:AAE_GuhHr0jan3J6r4RcVQZ5hMDukW0RTXs"
ADMIN_ID = 8519899945

reviews = []
top_clients = {}

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("⭐ ЗВЁЗДЫ", callback_data="stars")],
        [InlineKeyboardButton("🖼 NFT", callback_data="nft")],
        [InlineKeyboardButton("🏠 АРЕНДА NFT", callback_data="rent")],
        [InlineKeyboardButton("🎁 ПОДАРКИ", callback_data="gifts")],
        [InlineKeyboardButton("💎 TON", callback_data="ton")],
        [InlineKeyboardButton("👑 PREMIUM", callback_data="premium")],
        [InlineKeyboardButton("🎓 ОСИНТ", callback_data="osint")],
        [InlineKeyboardButton("🔒 ДЭФ", callback_data="def")],
        [InlineKeyboardButton("⭐ ОТЗЫВЫ", callback_data="reviews_menu")],
        [InlineKeyboardButton("📞 ПОДДЕРЖКА", callback_data="support")],
        [InlineKeyboardButton("👤 ПРОФИЛЬ", callback_data="profile")],
        [InlineKeyboardButton("🏆 ТОП", callback_data="top")],
        [InlineKeyboardButton("❤️ J", callback_data="fun")]
    ]
    await update.message.reply_text(
        "✨ ДОБРО ПОЖАЛОВАТЬ В GRAVINDES STORE ✨\n\n"
        "🔥 САМЫЕ НИЗКИЕ ЦЕНЫ!\n"
        "👤 Владелец: @Gravindes\n\n"
        "👇 ВЫБЕРИ КАТЕГОРИЮ",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button_handler(update: Update, context):
    query = update.callback_query
    await query.answer()
    user = query.from_user
    username = f"@{user.username}" if user.username else user.first_name

    if query.data == "back":
        await start(update, context)
        return

    if query.data == "stars":
        keyboard = [
            [InlineKeyboardButton("100⭐ - 110₽", callback_data="buy_100")],
            [InlineKeyboardButton("150⭐ - 160₽", callback_data="buy_150")],
            [InlineKeyboardButton("200⭐ - 250₽", callback_data="buy_200")],
            [InlineKeyboardButton("250⭐ - 270₽", callback_data="buy_250")],
            [InlineKeyboardButton("300⭐ - 350₽", callback_data="buy_300")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("⭐ ВЫБЕРИ КОЛИЧЕСТВО ЗВЁЗД:", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if query.data == "nft":
        keyboard = [
            [InlineKeyboardButton("Обычный - 400₽", callback_data="buy_nft_common")],
            [InlineKeyboardButton("Обычный+ - 700₽", callback_data="buy_nft_plus")],
            [InlineKeyboardButton("Редкий - 1500₽", callback_data="buy_nft_rare")],
            [InlineKeyboardButton("Легендарный - 2000₽", callback_data="buy_nft_legend")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("🖼 ВЫБЕРИ NFT:", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if query.data == "rent":
        keyboard = [
            [InlineKeyboardButton("7 дней - 100⭐", callback_data="rent_7")],
            [InlineKeyboardButton("30 дней - 300⭐", callback_data="rent_30")],
            [InlineKeyboardButton("90 дней - 700⭐", callback_data="rent_90")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("🏠 ВЫБЕРИ СРОК АРЕНДЫ:", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if query.data == "gifts":
        keyboard = [
            [InlineKeyboardButton("Обычный - 400₽", callback_data="gift_common")],
            [InlineKeyboardButton("Улучшенный - 700₽", callback_data="gift_rare")],
            [InlineKeyboardButton("Премиум - 1000₽", callback_data="gift_premium")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("🎁 ВЫБЕРИ ПОДАРОК:", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if query.data == "ton":
        keyboard = [
[InlineKeyboardButton("1 TON - 300₽", callback_data="ton_1")],
            [InlineKeyboardButton("5 TON - 1450₽", callback_data="ton_5")],
            [InlineKeyboardButton("10 TON - 2800₽", callback_data="ton_10")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("💎 ВЫБЕРИ КОЛИЧЕСТВО TON:", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if query.data == "premium":
        keyboard = [
            [InlineKeyboardButton("1 месяц - 250₽", callback_data="prem_1")],
            [InlineKeyboardButton("3 месяца - 700₽", callback_data="prem_3")],
            [InlineKeyboardButton("6 месяцев - 1300₽", callback_data="prem_6")],
            [InlineKeyboardButton("12 месяцев - 2500₽", callback_data="prem_12")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("👑 ВЫБЕРИ ПЕРИОД PREMIUM:", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if query.data == "osint":
        await query.edit_message_text(
            "🎓 ОБУЧЕНИЕ ОСИНТ\n\n💰 ЦЕНА: 1500₽\n\n💳 ОПЛАТА:\n🏦 Т-Банк\n💳 2200 7021 4230 2590\n\n✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return

    if query.data == "def":
        await query.edit_message_text(
            "🔒 ДЭФ НАВСЕГДА\n\n💰 ЦЕНА: 1000₽\n\n💳 ОПЛАТА:\n🏦 Т-Банк\n💳 2200 7021 4230 2590\n\n✅ ПОСЛЕ ОПЛАТЫ ПРИШЛИ ЧЕК @Gravindes",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return

    if query.data == "reviews_menu":
        keyboard = [
            [InlineKeyboardButton("✍️ НАПИСАТЬ ОТЗЫВ", callback_data="write_review")],
            [InlineKeyboardButton("⭐ ЧИТАТЬ ОТЗЫВЫ", callback_data="read_reviews")],
            [InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]
        ]
        await query.edit_message_text("⭐ ОТЗЫВЫ\n\nОставь отзыв или почитай чужие:", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if query.data == "write_review":
        context.user_data["awaiting_review"] = True
        await query.edit_message_text(
            "✍️ НАПИСАТЬ ОТЗЫВ\n\nНапиши свой отзыв одним сообщением:",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="reviews_menu")]])
        )
        return

    if query.data == "read_reviews":
        if reviews:
            text = "⭐ ОТЗЫВЫ КЛИЕНТОВ ⭐\n\n" + "\n\n".join(reviews[-5:])
            await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="reviews_menu")]]))
        else:
            await query.edit_message_text("⭐ ОТЗЫВЫ\n\nПока нет отзывов. Будь первым!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="reviews_menu")]]))
        return

    if query.data == "support":
        await query.edit_message_text(
            "📞 ПОДДЕРЖКА\n\n👤 @Gravindes\n⏰ 24/7\n⚡ Ответ 2-5 минут",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return

    if query.data == "profile":
        await query.edit_message_text(
            f"👤 ПРОФИЛЬ\n\n🆔 ID: {user.id}\n📝 Имя: {user.first_name}\n📝 Username: {username}\n💰 Баланс: 0₽",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]])
        )
        return

    if query.data == "top":
        if top_clients:
            sorted_top = sorted(top_clients.items(), key=lambda x: x[1], reverse=True)[:10]
            text = "🏆 ТОП КЛИЕНТОВ 🏆\n\n"
            for i, (name, amount) in enumerate(sorted_top, 1):
                text += f"{i}. {name} — {amount}₽\n"
            await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]))
        else:
            await query.
edit_message_text("🏆 ТОП КЛИЕНТОВ\n\nПока никого нет. Ты можешь занять первое место!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]))
        return

    if query.data == "fun":
        await query.edit_message_text("❤️ J ❤️\n\n@Gravindes желает тебе отличного дня! 🚀", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 НАЗАД", callback_data="back")]]))
        return

    if query.data.startswith(("buy_", "rent_", "gift_", "ton_", "prem_")):
        product_name = query.data
        top_clients[username] = top_clients.get(username, 0) + 500
        await query.edit_message_text(
            f"✅ ЗАКАЗ ПРИНЯТ!\n\n📦 Товар: {product_name}\n\n💳 ОПЛАТА:\n🏦 Т-Банк\n💳 2200 7021 4230 2590\n\n✅ После оплаты пришли чек @Gravindes\n\n❤️ Спасибо за заказ!",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙 В МЕНЮ", callback_data="back")]])
        )
        await context.bot.send_message(ADMIN_ID, f"🛒 НОВЫЙ ЗАКАЗ!\n📦 {product_name}\n👤 {user.first_name}\n📝 {username}")
        return

async def handle_message(update: Update, context):
    user = update.effective_user
    username = f"@{user.username}" if user.username else user.first_name
    
    if context.user_data.get("awaiting_review"):
        reviews.append(f"«{update.message.text}» — {username}")
        await context.bot.send_message(ADMIN_ID, f"⭐ НОВЫЙ ОТЗЫВ!\n👤 {user.first_name}\n📝 {update.message.text}")
        await update.message.reply_text("✅ СПАСИБО ЗА ОТЗЫВ!\n\n👇 Нажми /start")
        context.user_data["awaiting_review"] = False
        return
    
    await update.message.reply_text("👇 Нажми /start чтобы открыть меню")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

print("✅ GRAVINDES STORE ЗАПУЩЕН!")
app.run_polling()
