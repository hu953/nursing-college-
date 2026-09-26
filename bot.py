import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

# التوكن الخاص بك
API_TOKEN = '8716480166:AAGgiw2_q2iwn7afWoca2LjE5UH5Yaz5PBM'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 تصفح المحاضرات حسب الجامعة", callback_data="browse_unis")
    builder.button(text="🔍 البحث السريع عن محاضرة", callback_data="search_lecture")
    builder.button(text="📤 رفـع محاضرة جديدة", callback_data="upload_lecture")
    builder.adjust(1)
    
    await message.answer(
        f"أهلاً بك يا **{message.from_user.first_name}** في بوت مكتبة التمريض العراقية المركزية 🩺.\n\n"
        "هذا البوت يجمع ملازم ومحاضرات كليات التمريض في عموم العراق. اختر ما يناسبك للبدء:",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "browse_unis")
async def process_browse_unis(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    unis = ["جامعة بغداد", "جامعة الكوفة", "جامعة الموصل", "جامعة البصرة", "جامعة بابل"]
    
    for uni in unis:
        builder.button(text=uni, callback_data=f"uni_{uni}")
    
    builder.button(text="⬅️ القائمة الرئيسية", callback_data="main_menu")
    builder.adjust(2)
    
    await callback.message.edit_text(
        "اختر اسم الجامعة أو الكلية المطلوبة:",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data == "main_menu")
async def process_main_menu(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    builder.button(text="📚 تصفح المحاضرات حسب الجامعة", callback_data="browse_unis")
    builder.button(text="🔍 البحث السريع عن محاضرة", callback_data="search_lecture")
    builder.button(text="📤 رفـع محاضرة جديدة", callback_data="upload_lecture")
    builder.adjust(1)
    
    await callback.message.edit_text(
        "أهلاً بك مجدداً في القائمة الرئيسية. اختر ما يناسبك:",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
